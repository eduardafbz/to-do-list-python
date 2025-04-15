from model import Task

class TaskRepository:

    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def add(self, task):
        task.id = self.current_id
        self.current_id += 1
        self.tasks.append(task)
        return task
    
    def get_all(self):
        return self.tasks
    
    def get_by_id(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    def update(self, task: Task):
        for position, existing_task in enumerate(self.tasks):
            if existing_task.id == task.id:
                self.tasks[position] = task
                return task
        return None
    
    def delete_all(self):
        return self.tasks.clear()
    
    def delete_by_id(self, task_id: int):
        for position, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[position]
                return task
        return None