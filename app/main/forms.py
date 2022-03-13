from flask_wtf import FlaskForm
from wtforms import  StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, DataRequired, Length


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Blog')
    
    
# class BlogForm(FlaskForm):
#     title = StringField('Title', validators=[Required()])
#     category = SelectField('Category', choices=[('Choise_1','Choise_1'),('Choise_2','Choise_2'),('Choise_3','Choise_3'),('Choise_4','Choise_4')],validators=[Required()])
#     post = TextAreaField('Your Pitch', validators=[Required()])
#     submit = SubmitField('Pitch')


class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
