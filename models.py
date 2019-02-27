from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    deadline = db.Column(db.DateTime)
    
    def __init__(self,title,deadline):
        self.title = title
        self.deadline = deadline