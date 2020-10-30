from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

photos = UploadSet('photos',IMAGES)

mail = Mail()

def create_app(config_name):
    app=Flask(__name__)
    csrf = CSRFProtect(app)

      #Creating the app configurations
    import os
    SECRET_KEY = os.environ.get('SECRET_KEY')
    app.config['SECRET_KEY']=SECRET_KEY
    app.config.from_object(config_options[config_name])

    #Trial debugging CSRF runtime error
    app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

    # Creating the app configurations
    
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)


    # configure UploadSet
    configure_uploads(app,photos)

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
   
    # Will add the views and forms

    return app