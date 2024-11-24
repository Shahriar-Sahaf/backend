from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class CalculationForm(FlaskForm):
    input1 = FloatField('Input 1', validators=[DataRequired()])
    input2 = FloatField('Input 2', validators=[DataRequired()])
    input3 = FloatField('Input 3', validators=[DataRequired()])
    submit = SubmitField('Calculate')
