import unittest
import json
from UTS import read, write, dataeaa, terserahMauBukaApa

class TestDataeaa(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_file.json'

    def test_read(self):
        # Test if the function returns an empty list when the file is not found
        self.assertEqual(read(self.test_file), [])

        # Test if the function returns the correct data when the file is found
        test_data = [{"Feedback": "Test feedback"}]
        write(test_data, self.test_file)
        self.assertEqual(read(self.test_file), test_data)

    def test_write(self):
        # Test if the function writes the data correctly to the file
        test_data = [{"Feedback": "Test feedback"}]
        write(test_data)
        with open(self.test_file, 'r') as file:
            self.assertEqual(json.read(file), test_data)
    
    def test_operasi_tidak_valid(self):
        with self.assertRaises(ValueError):
            terserahMauBukaApa('3')

    def test_dataeaa(self):
        # Test if the main function runs without errors
        dataeaa()

if __name__ == '__main__':
    unittest.main()

