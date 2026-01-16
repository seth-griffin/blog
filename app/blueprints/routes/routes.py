from flask import render_template
from flask import Blueprint
from app.blueprints.db.models import Post

blog = Blueprint('blog', __name__, template_folder='web/static/templates')

@blog.route("/")
@blog.route("/index")
def index():
    return render_template("index.html")
