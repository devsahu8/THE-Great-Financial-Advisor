from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class IndexForm(FlaskForm):
    amount=IntegerField("Enter the complete amount of money you have.",validators=[DataRequired()])
    submit=SubmitField("Submit")