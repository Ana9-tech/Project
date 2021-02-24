from project import db,login_manager,app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):

    __tablename__ = " Users"

    id = db.Column(db.Integer, primary_key = True)
    names = db.Column(db.String(50), nullable= False)
    email = db.Column(db.String(20), nullable = False)
    password_hash = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)