from abc import ABC, abstractmethod
import subprocess
import os
from googlesearch import search
import click # Import click for echo

class Tool(ABC):
    """A base class for all tools."""

    def __init__(self, name, description, verbose=False):
        self.name = name
        self.description = description
        self.verbose = verbose

    @abstractmethod
    def use(self, **kwargs):
        """Use the tool."""
        pass

class PythonTool(Tool):
    """A tool for executing Python code."""

    def __init__(self, verbose=False):
        super().__init__('python', 'Execute Python code', verbose=verbose)

    def use(self, code, working_directory='.'):
        """Execute the given Python code."""
        if self.verbose:
            click.echo(f"[PythonTool] Executing Python code in '{working_directory}':\n---\n{code}\n---")
        try:
            output = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, cwd=working_directory)
            decoded_output = output.decode('utf-8')
            if self.verbose:
                click.echo(f"[PythonTool] Output:\n---\n{decoded_output}\n---")
            return decoded_output
        except subprocess.CalledProcessError as e:
            error_output = e.output.decode('utf-8')
            if self.verbose:
                click.echo(f"[PythonTool] Error executing Python code:\n---\n{error_output}\n---")
            return error_output

class ShellTool(Tool):
    """A tool for executing shell commands."""

    def __init__(self, verbose=False):
        super().__init__('shell', 'Execute a shell command', verbose=verbose)

    def use(self, command):
        """Execute the given shell command."""
        if self.verbose:
            click.echo(f"[ShellTool] Executing shell command:\n---\n{command}\n---")
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            decoded_output = output.decode('utf-8')
            if self.verbose:
                click.echo(f"[ShellTool] Output:\n---\n{decoded_output}\n---")
            return decoded_output
        except subprocess.CalledProcessError as e:
            error_output = e.output.decode('utf-8')
            if self.verbose:
                click.echo(f"[ShellTool] Error executing shell command:\n---\n{error_output}\n---")
            return error_output

class FileSystemTool(Tool):
    """A tool for interacting with the file system."""

    def __init__(self, verbose=False):
        super().__init__('filesystem', 'Interact with the file system', verbose=verbose)

    def use(self, operation, path, content=None):
        """Perform a file system operation."""
        if self.verbose:
            click.echo(f"[FileSystemTool] Performing operation '{operation}' on path '{path}'")
        if operation == 'read':
            return self._read_file(path)
        elif operation == 'write':
            return self._write_file(path, content)
        elif operation == 'list':
            return self._list_directory(path)
        else:
            if self.verbose:
                click.echo(f"[FileSystemTool] Unknown operation: {operation}")
            return f"Unknown operation: {operation}"

    def _read_file(self, path):
        try:
            with open(path, 'r') as f:
                content = f.read()
            if self.verbose:
                click.echo(f"[FileSystemTool] Read content from '{path}':\n---\n{content[:200]}...\n---") # Show first 200 chars
            return content
        except Exception as e:
            if self.verbose:
                click.echo(f"[FileSystemTool] Error reading file '{path}': {e}")
            return str(e)

    def _write_file(self, path, content):
        try:
            with open(path, 'w') as f:
                f.write(content)
            if self.verbose:
                click.echo(f"[FileSystemTool] Successfully wrote to '{path}'")
            return f"Successfully wrote to {path}"
        except Exception as e:
            if self.verbose:
                click.echo(f"[FileSystemTool] Error writing to file '{path}': {e}")
            return str(e)

    def _list_directory(self, path):
        try:
            files = os.listdir(path)
            if self.verbose:
                click.echo(f"[FileSystemTool] Listed directory '{path}': {files}")
            return "\n".join(files)
        except Exception as e:
            if self.verbose:
                click.echo(f"[FileSystemTool] Error listing directory '{path}': {e}")
            return str(e)

class CalculatorTool(Tool):
    """A tool for evaluating mathematical expressions."""

    def __init__(self, verbose=False):
        super().__init__('calculator', 'Evaluate a mathematical expression', verbose=verbose)

    def use(self, expression):
        """Evaluate the given mathematical expression."""
        if self.verbose:
            click.echo(f"[CalculatorTool] Evaluating expression: {expression}")
        try:
            # Sanitize the expression to prevent security risks
            allowed_chars = "0123456789+-*/(). "
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            result = eval(expression)
            if self.verbose:
                click.echo(f"[CalculatorTool] Result: {result}")
            return str(result)
        except Exception as e:
            if self.verbose:
                click.echo(f"[CalculatorTool] Error evaluating expression: {e}")
            return str(e)

class WebSearchTool(Tool):
    """A tool for searching the web."""

    def __init__(self, verbose=False):
        super().__init__('web_search', 'Search the web for a given query', verbose=verbose)

    def use(self, query):
        """Perform a web search."""
        if self.verbose:
            click.echo(f"[WebSearchTool] Searching for: '{query}'")
        try:
            results = list(search(query, num_results=5))
            if self.verbose:
                click.echo(f"[WebSearchTool] Found {len(results)} results.")
                for i, res in enumerate(results):
                    click.echo(f"  {i+1}. {res}")
            return "\n".join(results)
        except Exception as e:
            if self.verbose:
                click.echo(f"[WebSearchTool] Error during web search: {e}")
            return str(e)
