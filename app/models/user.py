from app.models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'editor', etc.

    def __init__(self, username, password, role='editor'):
        self.username = username
        self.password = password
        self.role = role
