from flask_login import UserMixin


from bprintapp.app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text)
    role = db.Column(db.Text)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return f'Person name: {self.username}, role {self.role}, job {self.role}'

    def get_id(self):
        return self.uid