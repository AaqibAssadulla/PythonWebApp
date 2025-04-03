from flask import Blueprint, render_template

web_blueprint = Blueprint("web", __name__)

# Home Page
@web_blueprint.route("/")
def homepage():
    return render_template("index.html")

# Tools
@web_blueprint.route("/kpdcl-bill-reader")
def kpdcl_bill_reader():
    return render_template("sample-page.html")
    #return render_template("kpdcl-bill-reader.html")

@web_blueprint.route("/hsd-statement-generator")
def hsd_statement_generator():
    return render_template("sample-page.html")
    #return render_template("hsd-statement-generator.html")

@web_blueprint.route("/oorja-docket-closer")
def oorja_docket_closer():
    return render_template("sample-page.html")
    #return render_template("oorja-docket-closer.html")

@web_blueprint.route("/oorja-bill-filler")
def oorja_bill_filler():
    return render_template("sample-page.html")
    #return render_template("oorja-bill-filler.html")

# Education
@web_blueprint.route("/jto-training")
def jto_training():
    return render_template("sample-page.html")
    #return render_template("jto-training.html")

# Islamic
@web_blueprint.route("/quran")
def quran_page():
    return render_template("sample-page.html")
    #return render_template("quran.html")

@web_blueprint.route("/hadith")
def hadith_page():
    return render_template("sample-page.html")
    #return render_template("hadith.html")

@web_blueprint.route("/fiqh")
def fiqh_page():
    return render_template("sample-page.html")
    #return render_template("fiqh.html")

@web_blueprint.route("/arabic")
def arabic_page():
    return render_template("sample-page.html")
    #return render_template("arabic.html")

# Authentication
@web_blueprint.route("/authentication-login")
def login_page():
    return render_template("sample-page.html")
    #return render_template("authentication-login.html")

@web_blueprint.route("/authentication-register")
def register_page():
    return render_template("sample-page.html")
    #return render_template("authentication-register.html")

# Extras
@web_blueprint.route("/icon-tabler")
def icons_page():
    return render_template("sample-page.html")
    #return render_template("icon-tabler.html")

@web_blueprint.route("/sample-page")
def sample_page():
    return render_template("sample-page.html")
    #return render_template("sample-page.html")
