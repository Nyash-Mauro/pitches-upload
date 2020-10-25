from flask import render_template,request,url_for,abort
from  .import main
from .forms import CommentsForms,UpdateProfile,PitchForm
from ..models import Comment,Pitch,User
from flask_login import login_required, current_user
from .. import db,photos

@main.route('/')
def index():
    """ View root page func that returns the index page and its data """
    return render_template('index.html')
