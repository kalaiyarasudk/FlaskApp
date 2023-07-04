from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class Register_form(FlaskForm):
    def validate_user_name(self, field):
        user = User.query.filter_by(user_name=field.data).first()
        if user:
            raise ValidationError('Username already exists. Please enter a new username.')

    def validate_mail_id(self, field):
        user = User.query.filter_by(mail_id=field.data).first()
        if user:
            raise ValidationError('Email address already exists. Please enter a new email address.')

    

    user_name = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    mail_id = StringField(label='Mail ID', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class login_form(FlaskForm):
    user_name = StringField(label='username',validators=[DataRequired()])
    password = StringField(label='password',validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    
class purchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")
    