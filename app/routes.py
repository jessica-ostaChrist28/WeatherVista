from flask import Blueprint, render_template, request
from app.weather import get_weather
from app.weather import get_weather, get_forecast
from flask import jsonify
main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])

def home():

    weather = None
    error = None
    forecast = None
    if request.method == "POST":

        city = request.form.get("city")

        if city:

            weather = get_weather(city)
            forecast = get_forecast(city)

            if weather is None:
                error = "City not found"

        else:
            error = "Please enter a city"

    return render_template(
        "index.html",
        weather=weather,
        error=error,
        forecast=forecast
    )

@main.route("/api/weather/<city>")

def api_weather(city):

    weather = get_weather(city)

    forecast = get_forecast(city)

    if weather is None:

        return jsonify({
            "error": "City not found"
        }), 404

    return jsonify({
        "weather": weather,
        "forecast": forecast
    })