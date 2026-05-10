from flask import Flask
from flask_login import LoginManager
from app.models import db, User

login_manager = LoginManager()

login_manager.login_view = "main.login"


def create_app():

    app = Flask(__name__)

    import os

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "sqlite:///weathervista.db"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager.init_app(app)

    from app.routes import main

    app.register_blueprint(main)

    with app.app_context():

        db.create_all()

    return app


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))