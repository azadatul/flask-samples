from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length


class AdminLoginForm(FlaskForm):
    # admin id - Textbox
    admin_id = EmailField('Admin Id', id='adminidbox',
                          validators=[DataRequired(), Email(),
                                      Length(min=6, max=50)],
                          render_kw={'class': 'form-control', 'placeholder': 'Enter admin Email Id'})

    # Admin Password - Textbox
    admin_password = PasswordField('Password', id='adminpasswordbox',
                                   validators=[
                                       DataRequired(), Length(min=4, max=25)],
                                   render_kw={'class': 'form-control', 'placeholder': 'Enter Password'})

    # Submit - Button
    submit = SubmitField('Login', id='loginbtn', render_kw={
                         'class': 'btn btn-primary btn-block'})
