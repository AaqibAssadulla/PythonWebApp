from flask import Blueprint, render_template

web_blueprint = Blueprint("web_blueprint", __name__)

@web_blueprint.route("/")
def homepage():
    return render_template("index.html")

@web_blueprint.route("/ui-buttons")
def ui_buttons_page():
    return render_template("ui-buttons.html") 