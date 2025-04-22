import datetime
from model import Task
from repository.TaskRepository import TaskRepository

class TaskService:

    def __init__(self):
        self.repository = TaskRepository()
        
    def add(self, title, description):
        createdAt = updatedAt = datetime.datetime.now() 
        task = self.repository.add(title = title, description = description, createdAt = createdAt, updatedAt = updatedAt, completed = False)
        return task
    
    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)
    
    def update(self, id, title, description, completed):
        updatedAt = datetime.datetime.now()
        return self.repository.update(id, title, description,updatedAt, completed)
    
    def delete_all(self):
        return self.repository.delete_all()
    
    def delete_by_id(self, id):
        return self.repository.get_by_id(id)

