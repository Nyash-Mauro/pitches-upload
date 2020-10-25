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

    @password.setter
    def password(self,password):
        self.pass_secure= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}'

class Pitch(db.Model):
    '''
    Pitch class to define Pitch Objects
    '''
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
        

    def save_pitch(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Pitch.query.all()
