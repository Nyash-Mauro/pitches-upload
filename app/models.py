from . import  db
from werkzeug.security import generate_password_hash,check_password_hash
from flash_login import UserMixin

from . import login_manager, User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.interger, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pitch_id= db.Column(db.Interger,db.ForeignKey('piches.id'))
    bio =db.Column(db.String(255))
    profile_pic_path =db.Column(db.String())
    pass_secure=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('Cant read password attribute')
    @password.setter()