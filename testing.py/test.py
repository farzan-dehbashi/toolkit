import unittest
import main_code

class MyTestCase(unittest.TestCase):
    def test_converter(self):
        actual_result = main_code.convert_gender('M')
        expected_result = 'MALE'
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
