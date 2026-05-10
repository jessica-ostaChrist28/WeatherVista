from flask import (
    Blueprint,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.models import db, User

from app.weather import (
    get_weather,
    get_forecast,
    get_weather_by_location
)

main = Blueprint("main", __name__)


# ======================================
# LOGIN
# ======================================

@main.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        return redirect(url_for("main.home"))

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            return redirect(url_for("main.home"))

        flash("Invalid email or password")

    return render_template("login.html")


# ======================================
# SIGNUP
# ======================================

@main.route("/signup", methods=["GET", "POST"])
def signup():

    if current_user.is_authenticated:

        return redirect(url_for("main.home"))

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get("email")

        password = request.form.get("password")

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash("Email already exists")

            return redirect(url_for("main.signup"))

        hashed_password = generate_password_hash(
            password
        )

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        login_user(new_user)

        return redirect(url_for("main.home"))

    return render_template("signup.html")


# ======================================
# LOGOUT
# ======================================

@main.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("main.login"))


# ======================================
# HOME
# ======================================

@main.route("/")
@login_required
def home():

    return render_template(
        "index.html",
        user=current_user
    )


# ======================================
# WEATHER API
# ======================================

@main.route("/api/weather/<city>")
@login_required
def api_weather(city):

    weather = get_weather(city)

    forecast = get_forecast(city)

    if weather is None:

        return jsonify({
            "error": "City not found"
        }), 404

    return jsonify({
        "weather": weather,
        "forecast": forecast or []
    })


# ======================================
# LOCATION WEATHER
# ======================================

@main.route("/api/location/<lat>/<lon>")
@login_required
def location_weather(lat, lon):

    weather = get_weather_by_location(
        lat,
        lon
    )

    if weather is None:

        return jsonify({
            "error": "Location weather unavailable"
        }), 404

    forecast = get_forecast(
        weather["city"]
    )

    return jsonify({
        "weather": weather,
        "forecast": forecast or []
    })