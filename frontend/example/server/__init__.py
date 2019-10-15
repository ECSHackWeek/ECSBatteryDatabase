from flask import Flask, render_template

application = Flask(__name__,
                    static_folder="../static/dist",
                    template_folder="../static")


@application.route("/")
def index():
    return render_template("index.html")
