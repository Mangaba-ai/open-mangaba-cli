from abc import ABC, abstractmethod

class LLM(ABC):
    """A base class for all LLMs."""

    @abstractmethod
    def complete(self, prompt, **kwargs):
        """Generate a completion for a given prompt."""
        pass
