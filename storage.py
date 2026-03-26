import json
import os

class Storage:
    FILE_NAME = "tasks.json"

    @staticmethod
    def load_tasks():
        if not os.path.exists(Storage.FILE_NAME):
            return []
        with open(Storage.FILE_NAME, "r") as f:
            return json.load(f)

    @staticmethod
    def save_tasks(tasks_list):
        with open(Storage.FILE_NAME, "w") as f:
            json.dump(tasks_list, f, indent=4)

    @staticmethod
    def add_single_task(name, priority):
        tasks = Storage.load_tasks()
        new_task = {"name": name, "priority": int(priority), "duration": 0, "completed": False, "exec_order": None}
        tasks.append(new_task)
        Storage.save_tasks(tasks)

    @staticmethod
    def mark_completed(name):
        tasks = Storage.load_tasks()
        # Find how many are already completed to set the exec_order
        exec_count = len([t for t in tasks if t.get('completed')])
        for t in tasks:
            if t['name'] == name:
                t['completed'] = True
                t['exec_order'] = exec_count + 1
        Storage.save_tasks(tasks)

    @staticmethod
    def delete_task(name):
        tasks = Storage.load_tasks()
        # Create a new list excluding the task with the matching name
        filtered_tasks = [t for t in tasks if t['name'] != name]
        Storage.save_tasks(filtered_tasks)