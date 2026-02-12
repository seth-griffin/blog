from flask import render_template, Blueprint, make_response
from app.blueprints.data.models import Post
from app.extensions import db
from datetime import date

blog = Blueprint("blog", __name__, template_folder="web/static/templates")

@blog.route("/", methods=["GET"])
@blog.route("/index")
@blog.route("/<path:full_path>")
def index(full_path="/"):
    if full_path == "/" or full_path == "":
        top5_posts = (
            db.session.query(Post).order_by(Post.posted_on.desc()).limit(5).all()
        )
        return render_template("index.html", 
            mimetype="text/html", 
            posts=top5_posts,
            title="Seth Griffin | Home",
            description="Home page"
        )
    else:
        if is_post_url(full_path):
            criteria = post_url_to_criteria(full_path)
            post = post_get(
                criteria["categories"], criteria["posted_on"], criteria["title"]
            )

            posted_on_iso_8601 = post.posted_on.strftime('%Y%m%dT%H%M%S.%fZ')
            posted_on_mm_dd_YYYY = post.posted_on.strftime('%b %d, %Y')

            return render_template("post.html", 
                title=post.title,
                description=post.title,
                post=post, 
                posted_on_iso_8601=posted_on_iso_8601, 
                posted_on_mm_dd_YYYY=posted_on_mm_dd_YYYY
            )


def post_get(categories, posted_on, title):

    return (
        db.session.query(Post)
        # .filter(Post.posted_on == posted_on)
        .filter(Post.categories == categories)
        .filter(Post.title.ilike(title))
        .one()
    )


def post_url_to_criteria(full_path):
    path_segments = full_path.split("/")
    title = path_segments.pop().replace("-", " ").replace(".html", "")
    posted_on = (
        path_segments.pop() + "-" + path_segments.pop() + "-" + path_segments.pop()
    )
    categories = ",".join(path_segments)

    return {"title": title, "posted_on": posted_on, "categories": categories}


def is_post_url(full_path):
    is_post_url = True

    post_criteria = post_url_to_criteria(full_path)

    post = post_get(
        post_criteria["categories"], post_criteria["posted_on"], post_criteria["title"]
    )

    if post is None:
        is_post_url = False

    return is_post_url


@blog.route(
    "/post/<path:categories>/<int:year>/<int:month>/<int:day>/<string:title>",
    methods=["GET"],
)
def post(categories, year, month, day, title):
    return render_template("post.html")


@blog.route("/about", methods=["GET"])
def about():
    return render_template(
        "about.html",
        title="Seth Griffin | About",
        description="Seth Griffin | About"
    )


@blog.route("/feed.xml", methods=["GET"])
def feed():
    top5_posts = db.session.query(Post).order_by(Post.posted_on.desc()).limit(5).all()

    updated = top5_posts[0].posted_on
    posts = top5_posts

    rendered = render_template("rss.xml", updated=updated, posts=posts)
    response = make_response(rendered)
    response.headers["Content-Type"] = "application/xml"
    
    return response
