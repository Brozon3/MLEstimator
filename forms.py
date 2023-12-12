from decimal import Decimal
from typing import Tuple
import decimal
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class PersonInformationForm(FlaskForm):
    personAge = IntegerField("Age:", default=20, validators=[DataRequired(), NumberRange(min=20, max=100)])
    personBMI = DecimalField("BMI:", default=Decimal(15.0), places=2, rounding=decimal.ROUND_UP,
                             validators=[DataRequired(), NumberRange(min=15, max=70)])
    personGlucose = IntegerField("Glucose:", default=40, validators=[DataRequired(), NumberRange(min=40, max=200)])

    submit = SubmitField("Submit")


class CarInformationForm(FlaskForm):
    carCylinders = IntegerField("Cylinders:", default=3, validators=[DataRequired(), NumberRange(min=3, max=8)])
    carHorsepower = DecimalField("Horsepower:", default=Decimal(40), places=2, rounding=decimal.ROUND_UP,
                                 validators=[DataRequired(), NumberRange(min=40, max=250)])
    carWeight = IntegerField("Weight:", default=1600, validators=[DataRequired(), NumberRange(min=1600, max=5500)])
    carYear = IntegerField("Year:", default=1965, validators=[DataRequired(), NumberRange(min=1965, max=1987)])
    carOrigin = SelectField("Origin:", choices=["USA", "Japan", "Europe"], validators=[DataRequired()])

    submit = SubmitField("Submit")
