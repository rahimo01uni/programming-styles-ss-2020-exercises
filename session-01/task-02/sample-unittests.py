import unittest
import sys
import io

# Import the 'main function from word_index.py as wi_main
from word_index import main as wi_main


class TestPythonVersion(unittest.TestCase):

    def test_python_version(self):
        """ This is a simple example of a unittest that checks if you are running the right version of Python """
        self.assertEqual(sys.version_info.major, 3, msg="You are not running python 3")
        self.assertEqual(sys.version_info.minor, 7, msg="You are not running python 3.7")


class TestWordIndex(unittest.TestCase):
    """ See https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print for more details """

    def setUp(self):
        """ Create a StringIO object and redirect stdout to it """
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        """ Reset the original stdout to avoid polluting the environment """
        sys.stdout = sys.__stdout__
        del self.capturedOutput

    def test_output_is_not_none(self):
        # Execute
        wi_main()

        # Copy the value to a string. Note that at this point you cannot print anything to console,
        # use the debugger instead
        output = self.capturedOutput.getvalue()

        # Check the output is not None
        self.assertIsNotNone(output, msg="Output cannot be None")

        # Check the output is not empty
        self.assertNotEqual(output, '', msg="Output cannot be empty")

if __name__ == '__main__':
    unittest.main()


