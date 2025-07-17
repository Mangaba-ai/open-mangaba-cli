from .google import Google
from .openai import OpenAI

def create_agent(llm_provider, tools=None, verbose=False):
    """Create an agent with the given LLM provider and tools."""
    if llm_provider == 'google':
        return Google(tools=tools, verbose=verbose)
    elif llm_provider == 'openai':
        return OpenAI(tools=tools, verbose=verbose)
    else:
        raise ValueError(f'Unknown LLM provider: {llm_provider}')
