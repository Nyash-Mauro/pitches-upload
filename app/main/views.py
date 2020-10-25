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

@main.route('/all_pitches')
def all_pitches():
    general = Pitch.query.all()
    return render_template('all pitches.html',general=general)

@main.route('/interview')
def interview():
    comment =Comment.query.all()
    interview = Pitch.query.filter_by(category ='Interview Pitch').all()
    return render_template('interview.html',interview=interview,comment=comment)

@main.route('/promotion')
def promotion():
    
