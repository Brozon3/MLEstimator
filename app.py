from flask import Flask, render_template
from forms import PersonInformationForm, CarInformationForm
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdaqwawd68448awd6a8w4d6a84wd"
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

        return render_template("viewMPGResults.html", car_dict=car_dict)

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

        return render_template("viewDiabeticResults.html", person_dict=person_dict)

    else:
        return render_template("personInfo.html", form=form)


if __name__ == '__main__':
    app.run()
