from . import  db
from werkzeug.security import generate_password_hash,check_password_hash
from flash_login import UserMixin

from . import login_manager, User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))