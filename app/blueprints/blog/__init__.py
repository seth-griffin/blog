from flask import Flask
from ..data.models import Post

app = Flask(__name__)


@app.template_global("article_link")
def article_link(post: Post):
    return "#"
