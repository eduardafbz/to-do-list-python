import datetime
from model.Task import Task

class TaskRepository:

    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def add(self, title, description):
        createdAt = updatedAt = datetime.datetime.now()
        completed = False
        task = Task(self.current_id, title, description, createdAt, updatedAt, completed)
        self.tasks.append(task)
        self.current_id += 1
        return task
    
    def findAll(self):
        return self.tasks
    
    def findById(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    def update(self, id, title, description, updatedAt, completed):
        task = self.get_by_id(id)
        if task is None:
            return None
        task.title = title
        task.description = description
        task.updatedAt = updatedAt
        task.completed = completed
        return task
    
    def deleteAll(self):
        return self.tasks.clear()
    
    def deleteById(self, task_id: int):
        for position, task in enumerate(self.tasks):
            if task.id == task_id:
                return self.tasks.pop(position)
        return None