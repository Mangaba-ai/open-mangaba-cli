import unittest
import os
from src.tools import PythonTool, ShellTool, FileSystemTool, WebSearchTool

class TestTools(unittest.TestCase):

    def test_python_tool(self):
        tool = PythonTool()
        result = tool.use(code="print('Hello from Python')")
        self.assertIn('Hello from Python', result)

    def test_shell_tool(self):
        tool = ShellTool()
        # Test a simple command that works on both Windows and Linux
        if os.name == 'nt':  # Windows
            result = tool.use(command="echo Hello from Shell")
        else:
            result = tool.use(command="echo Hello from Shell")
        self.assertIn('Hello from Shell', result)

    def test_filesystem_tool_write_read_delete(self):
        tool = FileSystemTool()
        test_file = 'test_file.txt'
        test_content = 'This is a test file content.'

        # Write
        write_result = tool.use(operation='write', path=test_file, content=test_content)
        self.assertIn(f'Successfully wrote to {test_file}', write_result)

        # Read
        read_result = tool.use(operation='read', path=test_file)
        self.assertEqual(read_result.strip(), test_content)

        # Clean up
        os.remove(test_file)

    def test_filesystem_tool_list(self):
        tool = FileSystemTool()
        # Create a dummy file to ensure list sees something
        dummy_file = 'dummy_for_list_test.txt'
        with open(dummy_file, 'w') as f:
            f.write('dummy')

        list_result = tool.use(operation='list', path='.')
        self.assertIn(dummy_file, list_result)

        # Clean up
        os.remove(dummy_file)

    # Note: WebSearchTool test is commented out because it relies on external network access
    # and can be flaky in automated tests. It's better to test manually or with mocks.
    # def test_web_search_tool(self):
    #     tool = WebSearchTool()
    #     query = "Gemini AI"
    #     result = tool.use(query=query)
    #     self.assertIsInstance(result, str)
    #     self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
