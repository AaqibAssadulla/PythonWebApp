from flask import Blueprint, render_template

web_blueprint = Blueprint("web", __name__)

# Home Page
@web_blueprint.route("/")
def homepage():
    predefined_tool_list = [
        {"name": "KPDCL Bill Reader", "slug": "kpdcl-bill-reader"},
        {"name": "HSD Statement Generator", "slug": "hsd-statement-generator"},
        {"name": "Oorja Docket Closer", "slug": "oorja-docket-closer"},
        {"name": "Oorja Bill Filler", "slug": "oorja-bill-filler"}
    ]
    
    return render_template("index.html",predefined_tool_list=predefined_tool_list)

# Tools
@web_blueprint.route("/tools/<tool_slug>")
def render_tool_details(tool_slug):
    predefined_tool_list = [
        {"name": "KPDCL Bill Reader", "slug": "kpdcl-bill-reader"},
        {"name": "HSD Statement Generator", "slug": "hsd-statement-generator"},
        {"name": "Oorja Docket Closer", "slug": "oorja-docket-closer"},
        {"name": "Oorja Bill Filler", "slug": "oorja-bill-filler"}
    ]

    selected_tool = next((item for item in predefined_tool_list if item["slug"] == tool_slug), None)

    if not selected_tool:
        abort(404)

    return render_template("tool_detail.html", predefined_tool_list=predefined_tool_list,selected_tool=selected_tool)

# Islamic
@web_blueprint.route("/islamic/<category_slug>")
def render_islamic_category_page(category_slug):
    predefined_islamic_categories = [
        {"title": "Quran", "slug": "quran"},
        {"title": "Hadith", "slug": "hadith"},
        {"title": "Fiqh", "slug": "fiqh"},
        {"title": "Arabic", "slug": "arabic"}
    ]

    selected_category = next(
        (category for category in predefined_islamic_categories if category["slug"] == category_slug),
        None
    )

    if not selected_category:
        abort(404)

    return render_template("islamic_category.html", selected_category=selected_category)
# Education
@web_blueprint.route("/jto-training")
def jto_training():
    return render_template("sample-page.html")
    #return render_template("jto-training.html")


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
