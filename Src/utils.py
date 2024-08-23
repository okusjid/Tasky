import json
from typing import List, Dict
import os


class Utils:
    @staticmethod
    def save_tasks_to_file(file_path: str, data: List[Dict]) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    
    @staticmethod
    def load_tasks_from_file(file_path: str) -> List[Dict]:
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r') as file:
            return json.load(file)
