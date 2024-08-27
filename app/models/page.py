from app.models.db import db

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.slug = title.lower().replace(" ", "-")
