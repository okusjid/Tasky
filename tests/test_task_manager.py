import unittest
from Src.task_manager import TaskManager
from Src.task import Task


class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = TaskManager()
    
    def test_add_task(self):
        task = self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.task_id, 1)
    
    def test_delete_task(self):
        self.manager.add_task("Test task")
        self.assertTrue(self.manager.delete_task(1))
        self.assertEqual(len(self.manager.tasks), 0)
        self.assertFalse(self.manager.delete_task(1))  # Task not found
    
    def test_mark_task_as_completed(self):
        self.manager.add_task("Test task")
        self.assertTrue(self.manager.mark_task_as_completed(1))
        self.assertTrue(self.manager.tasks[0].completed)
        self.assertFalse(self.manager.mark_task_as_completed(2))  # Task not found
    
    def test_list_tasks(self):
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0], task1)
        self.assertEqual(tasks[1], task2)
    
    def test_to_dict_list(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        expected = [
            {"id": 1, "description": "Task 1", "completed": False},
            {"id": 2, "description": "Task 2", "completed": False},
        ]
        self.assertEqual(self.manager.to_dict_list(), expected)
    
    def test_load_from_dict_list(self):
        data = [
            {"id": 1, "description": "Task 1", "completed": False},
            {"id": 2, "description": "Task 2", "completed": True},
        ]
        self.manager.load_from_dict_list(data)
        self.assertEqual(len(self.manager.tasks), 2)
        self.assertEqual(self.manager.tasks[0].description, "Task 1")
        self.assertTrue(self.manager.tasks[1].completed)


if __name__ == "__main__":
    unittest.main()
