from appoms import db
from datetime import datetime


class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    start_date_time = db.Column(db.DateTime, nullable=True)
    end_date_time = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="appointment")

    def __repr__(self):
        return f"<Appointment {self.service_name} {self.description}\
                {self.start_date_time} {self.end_date_time}>"
