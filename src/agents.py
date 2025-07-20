from .google import Google
from .openai import OpenAI

def create_agent(llm_provider, tools=None, verbose=False, project_root=None):
    """Create an agent with the given LLM provider and tools."""
    if llm_provider == 'google':
        return Google(tools=tools, verbose=verbose, project_root=project_root)
    elif llm_provider == 'openai':
        # Assuming OpenAI class will also be updated to accept project_root
        return OpenAI(tools=tools, verbose=verbose, project_root=project_root)
    else:
        raise ValueError(f'Unknown LLM provider: {llm_provider}')
