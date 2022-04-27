from flask import Flask
from flask_restx import Api
from config import Config
from dao.models.user import User
from setup_db import db
from views.auth import auth_ns
from views.directors_views.derectors import director_ns
from views.genres_views.genres import genre_ns
from views.movies_views.movies import movie_ns
from views.users.users import user_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def create_data():
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")


        with db.session.begin():
            db.session.add_all([u1, u2,])


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    #    create_data()
    app.run()
