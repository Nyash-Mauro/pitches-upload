from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import DataRequired

class CommentsForms(FlaskForm):
    comment= TextAreaField('Comment',validators=DataRequired())
    vote=RadioField('default arguments',choices=[('1','UpVote'),('1''DownVote')])
    submit=SubmitField('Submit')