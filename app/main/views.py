from flask import render_template,request,url_for,abort
from  .import main
from .forms import CommentsForms,UpdateProfile,PitchForm
from ..models import Comment,Pitch,User
from flask_login import login_required, current_user
from .. import db,photos

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Pitch Deck'
    
    return render_template('index.html', title = title)

@main.route('/loggedin')
def loggedin():

    title='Pitch Deck'

    return render_template('login.html',title=title)