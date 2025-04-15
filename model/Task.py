class Task:

    def __init__(self, id, title, description, createdAt, updatedAt, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __str__(self):
        return f"Task(id={self.id}, title={self.title}, description={self.description}, completed={self.completed}, created at={self.createdAt}, updated at={self.updatedAt})"
    
    def mark_completed(self):
        self.completed = True

    def mark_uncompleted(self):
        self.completed = False