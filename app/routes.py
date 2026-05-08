from flask import Blueprint, render_template, request
from app.weather import get_weather

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])

def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city")

        if city:

            weather = get_weather(city)

            if weather is None:
                error = "City not found"

        else:
            error = "Please enter a city"

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )