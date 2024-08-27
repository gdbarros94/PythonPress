from app.models.db import db

class Telemetry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, action, timestamp):
        self.action = action
        self.timestamp = timestamp
