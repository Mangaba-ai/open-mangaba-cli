from openai import OpenAI as OpenAIClient
from .llm import LLM
from .config import load_config
import json

class OpenAI(LLM):
    """A class for interacting with OpenAI's API."""

    def __init__(self, tools=None, verbose=False, project_root=None):
        config = load_config()
        api_key = config.get('OPENAI_API_KEY')
        if not api_key:
            raise ValueError('OPENAI_API_KEY not found in config')
        self.client = OpenAIClient(api_key=api_key)
        self.tools = tools or []
        self.verbose = verbose
        self.project_root = project_root
        self.tool_functions = self._prepare_tool_functions()

    def _prepare_tool_functions(self):
        """Prepare tool functions for OpenAI function calling."""
        functions = []
        for tool in self.tools:
            if hasattr(tool, 'name'):
                function_def = {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    }
                }
                
                # Add specific parameters based on tool type
                if tool.name == "python":
                    function_def["parameters"]["properties"]["code"] = {
                        "type": "string",
                        "description": "Python code to execute"
                    }
                    function_def["parameters"]["required"] = ["code"]
                elif tool.name == "shell":
                    function_def["parameters"]["properties"]["command"] = {
                        "type": "string",
                        "description": "Shell command to execute"
                    }
                    function_def["parameters"]["required"] = ["command"]
                elif tool.name == "filesystem":
                    function_def["parameters"]["properties"].update({
                        "operation": {
                            "type": "string",
                            "enum": ["read", "write", "list"],
                            "description": "File system operation to perform"
                        },
                        "path": {
                            "type": "string",
                            "description": "File or directory path"
                        },
                        "content": {
                            "type": "string",
                            "description": "Content to write (for write operation)"
                        }
                    })
                    function_def["parameters"]["required"] = ["operation", "path"]
                elif tool.name == "web_search":
                    function_def["parameters"]["properties"]["query"] = {
                        "type": "string",
                        "description": "Search query"
                    }
                    function_def["parameters"]["required"] = ["query"]
                
                functions.append(function_def)
        return functions

    def complete(self, prompt, **kwargs):
        """Generate a completion for a given prompt."""
        try:
            messages = [{"role": "user", "content": prompt}]
            
            # Prepare the request parameters
            request_params = {
                "model": "gpt-3.5-turbo",
                "messages": messages,
                "max_tokens": kwargs.get('max_tokens', 1000),
                "temperature": kwargs.get('temperature', 0.7)
            }
            
            # Add function calling if tools are available
            if self.tool_functions:
                request_params["functions"] = self.tool_functions
                request_params["function_call"] = "auto"
            
            response = self.client.chat.completions.create(**request_params)
            
            # Handle function calls
            message = response.choices[0].message
            
            if hasattr(message, 'function_call') and message.function_call:
                return self._handle_function_call(message, messages)
            else:
                # Create a simple response object that mimics the expected interface
                class SimpleResponse:
                    def __init__(self, text):
                        self.text = text
                
                return SimpleResponse(message.content)
                
        except Exception as e:
            if self.verbose:
                print(f"Error in OpenAI completion: {e}")
            raise e
    
    def _handle_function_call(self, message, messages):
        """Handle function calls from OpenAI."""
        function_call = message.function_call
        function_name = function_call.name
        function_args = json.loads(function_call.arguments)
        
        if self.verbose:
            print(f"OpenAI is calling function: {function_name} with args: {function_args}")
        
        # Find and execute the corresponding tool
        tool_result = None
        for tool in self.tools:
            if tool.name == function_name:
                if function_name == "python":
                    python_params = {'code': function_args.get('code', '')}
                    if self.project_root:
                        python_params['working_directory'] = self.project_root
                    tool_result = tool.use(**python_params)
                elif function_name == "shell":
                    tool_result = tool.use(command=function_args.get('command', ''))
                elif function_name == "filesystem":
                    tool_result = tool.use(
                        operation=function_args.get('operation'),
                        path=function_args.get('path'),
                        content=function_args.get('content')
                    )
                elif function_name == "web_search":
                    tool_result = tool.use(query=function_args.get('query', ''))
                break
        
        if tool_result is None:
            tool_result = f"Error: Tool {function_name} not found or failed to execute"
        
        # Add the function call and result to the conversation
        messages.append({
            "role": "assistant",
            "content": None,
            "function_call": {
                "name": function_name,
                "arguments": function_call.arguments
            }
        })
        messages.append({
            "role": "function",
            "name": function_name,
            "content": str(tool_result)
        })
        
        # Get the final response
        final_response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        class SimpleResponse:
            def __init__(self, text):
                self.text = text
        
        return SimpleResponse(final_response.choices[0].message.content)
