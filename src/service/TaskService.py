import datetime
from model import Task
from repository.TaskRepository import TaskRepository

class TaskService:

    def __init__(self):
        self.repository = TaskRepository()
        
    def add(self, title, description):
        task = self.repository.add(title, description)
        return task
    
    def findAll(self):
        return self.repository.findAll()
    
    def findById(self, id):
        return self.repository.findById(id)
    
    def update(self, id, title, description, completed):
        updatedAt = datetime.datetime.now()
        return self.repository.update(id, title, description,updatedAt, completed)
    
    def deletAll(self):
        return self.repository.delete_all()
    
    def deleteById(self, id):
        return self.repository.deleteById(id)

