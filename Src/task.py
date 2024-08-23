# **`src/task.py`:**
from typing import Dict


class Task:
    def __init__(self, task_id: int, description: str, completed: bool = False) -> None:
        self.task_id = task_id
        self.description = description
        self.completed = completed
    
    def __repr__(self) -> str:
        status = "✔️" if self.completed else "❌"
        return f"{self.task_id}. {self.description} [{status}]"
    
    def to_dict(self) -> Dict:
        return {
            "id": self.task_id,
            "description": self.description,
            "completed": self.completed
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Task':
        return Task(data['id'], data['description'], data['completed'])
