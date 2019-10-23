from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__,
                    static_folder="../static/dist",
                    template_folder="../static/")
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(application)
migrate = Migrate(application, db)

import server.orm  # noqa E402
from server.api import api  # noqa E402
application.register_blueprint(api)


@application.route("/")
def index():
    return render_template("index.html")
