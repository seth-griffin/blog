from flask import render_template
from flask import Blueprint
from app.blueprints.data.models import Post

blog = Blueprint("blog", __name__, template_folder="web/static/templates")


@blog.route("/", methods=["GET"])
@blog.route("/index")
def index():
    return render_template("index.html")


# Ex: programming/functional-programming/lisp/scheme/arc/2025/12/11/introduction-arc-programming-language.html
@blog.route(
    "/post/<path:categories>/<int:year>/<int:month>/<int:day>/<string:title>",
    methods=["GET"],
)
def post(categories, year, month, day, title):
    return render_template("post.html")


@blog.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
