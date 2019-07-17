from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.length(min=4, max=20)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])
    email = StringField('Email Address', [validators.length(min=5, max=30)])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [validators.length(min=4, max=20)])
    password = PasswordField('Password', [validators.DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')



