import unittest
import os
import json
from Src.utils import Utils


class TestUtils(unittest.TestCase):
    
    def setUp(self):
        # Set up a temporary file path
        self.test_file = "test_tasks.json"
    
    def tearDown(self):
        # Clean up the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_save_tasks_to_file(self):
        data = [
            {"id": 1, "description": "Task 1", "completed": False},
            {"id": 2, "description": "Task 2", "completed": True},
        ]
        Utils.save_tasks_to_file(self.test_file, data)
        with open(self.test_file, 'r') as file:
            content = json.load(file)
        self.assertEqual(content, data)
    
    def test_load_tasks_from_file(self):
        data = [
            {"id": 1, "description": "Task 1", "completed": False},
            {"id": 2, "description": "Task 2", "completed": True},
        ]
        with open(self.test_file, 'w') as file:
            json.dump(data, file, indent=4)
        loaded_data = Utils.load_tasks_from_file(self.test_file)
        self.assertEqual(loaded_data, data)
    
    def test_load_tasks_from_file_non_existent(self):
        # Loading from a file that does not exist should return an empty list
        loaded_data = Utils.load_tasks_from_file("non_existent_file.json")
        self.assertEqual(loaded_data, [])


if __name__ == "__main__":
    unittest.main()
