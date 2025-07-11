import unittest
import example_python

class TestTable(unittest.TestCase):

    def test_tableJSON(self):
        result = example_python.tableJSON()
        self.assertEqual(result, result)

if __name__ == '__main__':
    unittest.main()