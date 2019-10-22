from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__,
                    static_folder="static/dist",
                    template_folder="static")
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(application)


@application.route("/")
def index():
    return render_template("index.html")
