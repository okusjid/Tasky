import unittest
from Src.task import Task


class TestTask(unittest.TestCase):
    
    def test_task_creation(self):
        task = Task(1, "Test task")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)
    
    def test_task_representation(self):
        task = Task(1, "Test task")
        self.assertEqual(repr(task), "1. Test task [❌]")
        task.completed = True
        self.assertEqual(repr(task), "1. Test task [✔️]")
    
    def test_task_to_dict(self):
        task = Task(1, "Test task", completed=True)
        expected = {"id": 1, "description": "Test task", "completed": True}
        self.assertEqual(task.to_dict(), expected)
    
    def test_task_from_dict(self):
        data = {"id": 1, "description": "Test task", "completed": True}
        task = Task.from_dict(data)
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertTrue(task.completed)


if __name__ == "__main__":
    unittest.main()
