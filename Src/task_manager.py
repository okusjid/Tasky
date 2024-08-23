from typing import List, Dict
from .task import Task


class TaskManager:
    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, description: str) -> Task:
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def delete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def mark_task_as_completed(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            task.completed = True
            return True
        return False
    
    def list_tasks(self) -> List[Task]:
        return self.tasks
    
    def to_dict_list(self) -> List[Dict]:
        return [task.to_dict() for task in self.tasks]
    
    def load_from_dict_list(self, data: List[Dict]) -> None:
        self.tasks = [Task.from_dict(item) for item in data]
        if self.tasks:
            self.next_id = max(task.task_id for task in self.tasks) + 1
    
    def _find_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
