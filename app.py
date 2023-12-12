from flask import Flask, render_template
from forms import PersonInformationForm, CarInformationForm
from datetime import datetime
import warnings
from joblib import load
import numpy as np


warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = "as0972140jda0s975093n0as9d"
pathName = "C:/Users/Pat/OneDrive/Documents/Desktop/insuranceEstimator/"


@app.route('/')
def welcome():  # put application's code here
    return render_template("index.html")


@app.route('/carInformation', methods=["POST", "GET"])
def get_car_information():
    form = CarInformationForm()
    if form.validate_on_submit():
        car_cylinders = form.carCylinders.data
        car_hp = form.carHorsepower.data
        car_weight = form.carWeight.data
        car_year = form.carYear.data
        car_origin = form.carOrigin.data

        if car_origin == "USA":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 1}
        elif car_origin == "Japan":
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 1, "origin_usa": 0}
        else:
            car_dict = {"cylinders": car_cylinders, "horsepower": car_hp, "weight": car_weight,
                        "age": datetime.today().year - car_year, "origin_japan": 0, "origin_usa": 0}

        input_array = np.array(list(car_dict.values())).reshape(1, -1)

        mpg_model = load("mpg_model.joblib")
        mpg_estimate = mpg_model.predict(input_array)

        return render_template("viewMPGResults.html", car_dict=car_dict, mpg_estimate=round(mpg_estimate[0], 2))

    else:
        return render_template("carInfo.html", form=form)


@app.route('/personInformation', methods=["POST", "GET"])
def get_person_information():
    form = PersonInformationForm()
    if form.validate_on_submit():

        person_age = form.personAge.data
        person_bmi = form.personBMI.data
        person_glucose = form.personGlucose.data

        person_dict = {"age": person_age, "bmi": person_bmi, "glucose": person_glucose}

        input_array = np.array(list(person_dict.values())).reshape(1, -1)

        diabetes_estimator = load("diabetes_model.joblib")
        diabetes_prediction = diabetes_estimator.predict(input_array)

        return render_template("viewDiabeticResults.html", person_dict=person_dict,
                               diabetes_prediction=diabetes_prediction)

    else:
        return render_template("personInfo.html", form=form)


if __name__ == '__main__':
    app.run()
