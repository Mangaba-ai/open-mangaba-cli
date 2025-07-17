import unittest
from unittest.mock import patch, MagicMock
from src.agents import create_agent
from src.tools import PythonTool, ShellTool, FileSystemTool, WebSearchTool

class TestAgents(unittest.TestCase):

    @patch('src.google.load_config')
    @patch('src.google.genai.configure')
    def test_create_google_agent(self, mock_configure, mock_load_config):
        """Test creating a Google agent."""
        mock_load_config.return_value = {'GOOGLE_API_KEY': 'test_key'}
        tools = [PythonTool(), ShellTool()]
        
        agent = create_agent('google', tools=tools, verbose=True)
        self.assertIsNotNone(agent)
        mock_configure.assert_called_once_with(api_key='test_key')

    @patch('src.openai.load_config')
    def test_create_openai_agent(self, mock_load_config):
        """Test creating an OpenAI agent."""
        mock_load_config.return_value = {'OPENAI_API_KEY': 'test_key'}
        tools = [PythonTool(), ShellTool()]
        
        agent = create_agent('openai', tools=tools, verbose=True)
        self.assertIsNotNone(agent)

    def test_create_agent_invalid_provider(self):
        """Test creating an agent with invalid provider."""
        with self.assertRaises(ValueError) as context:
            create_agent('invalid_provider')
        
        self.assertIn('Unknown LLM provider', str(context.exception))

    @patch('src.google.load_config')
    def test_create_agent_missing_api_key(self, mock_load_config):
        """Test creating an agent with missing API key."""
        mock_load_config.return_value = {}  # No API key
        
        with self.assertRaises(ValueError) as context:
            create_agent('google')
        
        self.assertIn('GOOGLE_API_KEY not found', str(context.exception))

if __name__ == '__main__':
    unittest.main()
