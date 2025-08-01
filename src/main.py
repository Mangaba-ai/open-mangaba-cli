import click
import json
import os
import sys
from .config import load_config, save_config
from .agents import create_agent
from .tools import PythonTool, ShellTool, FileSystemTool, WebSearchTool, CalculatorTool

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
AGENTS_FILE = os.path.join(DATA_DIR, 'agents.json')
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')

def ensure_data_dir():
    """Ensure the data directory exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data(file_path):
    """Load data from JSON file with error handling."""
    try:
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        click.echo(f"Error: Invalid JSON in {file_path}: {e}", err=True)
        return {}
    except Exception as e:
        click.echo(f"Error loading {file_path}: {e}", err=True)
        return {}

def save_data(data, file_path):
    """Save data to JSON file with error handling."""
    try:
        ensure_data_dir()
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        click.echo(f"Error saving to {file_path}: {e}", err=True)
        return False
    return True

def create_tools(tool_names, verbose=False):
    """Create a list of tools from a list of tool names."""
    tools = []
    if not tool_names:
        return tools

    if 'python' in tool_names:
        tools.append(PythonTool(verbose=verbose))
    if 'shell' in tool_names:
        tools.append(ShellTool(verbose=verbose))
    if 'filesystem' in tool_names:
        tools.append(FileSystemTool(verbose=verbose))
    if 'web_search' in tool_names:
        tools.append(WebSearchTool(verbose=verbose))
    if 'calculator' in tool_names:
        tools.append(CalculatorTool(verbose=verbose))
    return tools

@click.group()
def cli():
    """A CLI tool for creating and managing LLM agents."""
    click.echo("""
 __  __    _    _   _  ____    _    ____    _    
|  \/  |  / \  | \ | |/ ___|  / \  | __ )  / \   
| |\/| | / _ \ |  \| | |  _  / _ \ |  _ \ / _ \  
| |  | |/ ___ \| |\  | |_| |/ ___ \| |_) / ___ \ 
|_|  |_/_/   \_\_| \_\____/_/   \_\____/_/   \_\
""")
    pass

@cli.group()
def config():
    """Manage the configuration."""
    pass

@config.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    """Set a configuration key-value pair."""
    config = load_config()
    config[key] = value
    save_config(config)
    click.echo(f"Set {key} to {value}")

@config.command()
@click.argument('key')
def get(key):
    """Get a configuration value."""
    config = load_config()
    value = config.get(key)
    if value:
        click.echo(value)
    else:
        click.echo(f"Key {key} not found")

@cli.group()
def agent():
    """Manage agents."""
    pass

@agent.command()
@click.option('--name', prompt='Agent name', help='The name of the agent.')
@click.option('--llm-provider', default='google', help='The LLM provider to use.')
def create(name, llm_provider):
    """Create a new agent."""
    agents = load_data(AGENTS_FILE)
    if name in agents:
        click.echo(f"Agent {name} already exists.")
        return
    agents[name] = {'llm_provider': llm_provider, 'tools': []}
    save_data(agents, AGENTS_FILE)
    click.echo(f"Agent {name} created successfully.")

@agent.command()
@click.argument('name')
def delete(name):
    """Delete an agent."""
    agents = load_data(AGENTS_FILE)
    if name not in agents:
        click.echo(f"Agent {name} not found.")
        return
    del agents[name]
    save_data(agents, AGENTS_FILE)
    click.echo(f"Agent {name} deleted successfully.")

@agent.command()
@click.argument('name')
@click.argument('tool_name')
def add_tool(name, tool_name):
    """Add a tool to an agent."""
    agents = load_data(AGENTS_FILE)
    if name not in agents:
        click.echo(f"Agent {name} not found.")
        return

    if 'tools' not in agents[name]:
        agents[name]['tools'] = []

    if tool_name not in agents[name]['tools']:
        agents[name]['tools'].append(tool_name)
        save_data(agents, AGENTS_FILE)
        click.echo(f"Tool {tool_name} added to agent {name}.")
    else:
        click.echo(f"Tool {tool_name} already exists for agent {name}.")

@agent.command()
def list():
    """List all agents."""
    agents = load_data(AGENTS_FILE)
    if not agents:
        click.echo("No agents found.")
        return
    for name, agent_data in agents.items():
        click.echo(f"- {name} (LLM: {agent_data['llm_provider']})")

@cli.group()
def task():
    """Manage tasks."""
    pass

@task.command()
@click.option('--name', prompt='Task name', help='The name of the task.')
@click.option('--agent', prompt='Agent name', help='The agent to assign the task to.')
@click.option('--prompt', prompt='Prompt', help='The prompt for the task.')
def create(name, agent, prompt):
    """Create a new task."""
    tasks = load_data(TASKS_FILE)
    if name in tasks:
        click.echo(f"Task {name} already exists.")
        return
    tasks[name] = {'agent': agent, 'prompt': prompt}
    save_data(tasks, TASKS_FILE)
    click.echo(f"Task {name} created successfully.")

@task.command()
@click.argument('name')
def delete(name):
    """Delete a task."""
    tasks = load_data(TASKS_FILE)
    if name not in tasks:
        click.echo(f"Task {name} not found.")
        return
    del tasks[name]
    save_data(tasks, TASKS_FILE)
    click.echo(f"Task {name} deleted successfully.")

@task.command()
def list():
    """List all tasks."""
    tasks = load_data(TASKS_FILE)
    if not tasks:
        click.echo("No tasks found.")
        return
    for name, task_data in tasks.items():
        click.echo(f"- {name} (Agent: {task_data['agent']})")

@cli.command()
@click.argument('task_name')
@click.option('--verbose', is_flag=True, help='Enable verbose output for tool execution.')
@click.option('--steps', default=1, help='Number of steps to run the task.')
def run(task_name, verbose, steps):
    """Run a task."""
    try:
        # Load and validate task
        tasks = load_data(TASKS_FILE)
        if not tasks:
            click.echo("Error: No tasks found. Create a task first.", err=True)
            return
        
        if task_name not in tasks:
            click.echo(f"Error: Task '{task_name}' not found.", err=True)
            available_tasks = list(tasks.keys())
            if available_tasks:
                click.echo(f"Available tasks: {', '.join(available_tasks)}")
            return
        
        task_data = tasks[task_name]
        agent_name = task_data.get('agent')
        prompt = task_data.get('prompt')
        
        if not agent_name or not prompt:
            click.echo(f"Error: Task '{task_name}' is missing required data (agent or prompt).", err=True)
            return

        # Load and validate agent
        agents = load_data(AGENTS_FILE)
        if not agents:
            click.echo("Error: No agents found. Create an agent first.", err=True)
            return
            
        if agent_name not in agents:
            click.echo(f"Error: Agent '{agent_name}' not found.", err=True)
            available_agents = list(agents.keys())
            if available_agents:
                click.echo(f"Available agents: {', '.join(available_agents)}")
            return
        
        agent_data = agents[agent_name]
        llm_provider = agent_data.get('llm_provider')
        
        if not llm_provider:
            click.echo(f"Error: Agent '{agent_name}' is missing LLM provider configuration.", err=True)
            return

        # Validate API keys
        config = load_config()
        if llm_provider == 'google' and not config.get('GOOGLE_API_KEY'):
            click.echo("Error: GOOGLE_API_KEY not configured. Use 'python -m src.main config set GOOGLE_API_KEY YOUR_KEY'", err=True)
            return
        elif llm_provider == 'openai' and not config.get('OPENAI_API_KEY'):
            click.echo("Error: OPENAI_API_KEY not configured. Use 'python -m src.main config set OPENAI_API_KEY YOUR_KEY'", err=True)
            return

        if verbose:
            click.echo(f"Running task '{task_name}' with agent '{agent_name}' using {llm_provider} provider...")
            click.echo(f"Prompt: {prompt}")
            click.echo("-" * 50)

        # Create tools and agent
        tool_names = agent_data.get('tools', [])
        tools = create_tools(tool_names, verbose=verbose)

        project_root = os.path.abspath(os.path.join(DATA_DIR, '..'))
        agent = create_agent(llm_provider, tools=tools, verbose=verbose, project_root=project_root)
        
        # Execute task in a loop for the number of steps
        last_response = ""
        for i in range(steps):
            click.echo(f"--- Step {i+1}/{steps} ---")
            
            # Combine original prompt with the last response to maintain context
            current_prompt = f"{prompt}\n\nPrevious step's result:\n{last_response}"
            response = agent.complete(current_prompt)
            
            # Handle response based on type
            if hasattr(response, 'text'):
                response_text = response.text
                click.echo(response_text)
            elif hasattr(response, 'content'):
                response_text = response.content
                click.echo(response_text)
            else:
                response_text = str(response)
                click.echo(response_text)
            
            # Update last_response for the next step
            last_response = response_text


    except ValueError as e:
        click.echo(f"Configuration error: {e}", err=True)
        sys.exit(1)
    except ImportError as e:
        click.echo(f"Missing dependency: {e}", err=True)
        click.echo("Please install required packages: pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        click.echo("\nTask execution interrupted by user.", err=True)
        sys.exit(1)
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        click.echo(error_message, err=True)
        with open("error.log", "w", encoding='utf-8') as f:
            f.write(error_message + "\n")
            if verbose:
                import traceback
                tb_str = traceback.format_exc()
                click.echo("Full traceback:")
                click.echo(tb_str)
                f.write("Full traceback:\n")
                f.write(tb_str)
        sys.exit(1)

if __name__ == '__main__':
    cli()
