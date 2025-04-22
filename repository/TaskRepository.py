from model import Task

class TaskRepository:

    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def add(self, title, description, createdAt, updatedAt, completed=False):
        task = Task(self.current_id, title, description, createdAt, updatedAt, completed)
        self.tasks.append(task)
        self.current_id += 1
        return task
    
    def get_all(self):
        return self.tasks
    
    def get_by_id(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    def update(self, id, title, description, updatedAt, completed):
        task = self.get_by_id(id)
        if task:
            task.title = title
            task.description = description
            task.updatedAt = updatedAt
            task.completed = completed
            return task
        return None
    
    def delete_all(self):
        return self.tasks.clear()
    
    def delete_by_id(self, task_id: int):
        for position, task in enumerate(self.tasks):
            if task.id == task_id:
                return self.tasks.pop(position)
        return None