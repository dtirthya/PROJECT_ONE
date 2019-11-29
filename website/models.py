from datetime import datetime
from website import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=True, nullable=False)
    middle_name = db.Column(db.String, unique=True, nullable=True)
    last_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    image_folder = db.Column(db.String, unique=True, nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time_details = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    u_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    is_present = db.Column(db.Boolean, default=False, nullable=False)