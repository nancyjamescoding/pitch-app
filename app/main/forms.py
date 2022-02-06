from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import Required
from wtforms import TextAreaField, SelectField, SubmitField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Describe Yourself.',
                        validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Technology', 'Technology'), (
        'Promotion', 'Promotion'), ('Advertisement', 'Advertisement')], validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Submit')
