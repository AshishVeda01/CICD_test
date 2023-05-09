import unittest

from sample import sum


class CheckSum(unittest.TestCase):
    def test_list_int(self):
        print("testing sample code")
        print("test2")  
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
