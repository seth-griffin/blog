from flask import render_template, Blueprint, request, make_response, current_app as app
from app.extensions import db
from app.blueprints.data.models import Post
from app.blueprints.blog.util import post_url_to_criteria, post_is_url, post_get
import json

blog = Blueprint("blog", __name__, template_folder="web/static/templates")

@blog.route("/", methods=["GET"])
@blog.route("/<path:full_path>")
def index(full_path="/"):
    app.logger.debug("Detecting root or Post path " + full_path)

    
    try:
        app.logger.debug("Checking if full path is / or \"\"")
        if full_path == "/" or full_path == "":
            app.logger.debug(
                "Root path detected, rendering index.html with top 5 posts"
            )

            top5_posts = (
                db.session.query(Post).order_by(Post.posted_on.desc()).limit(5).all()
            )
        
            return render_template(
                "index.html",
                mimetype="text/html",
                posts=top5_posts,
                title="Seth Griffin | Home",
                description="Home page",
            )
        else:
            app.logger.debug(
                "Non-root path detected checking to see if url maps to Post"
            )
            app.logger.debug(full_path)

            criteria = post_url_to_criteria(full_path)
            app.logger.debug(
                "Post url to criteria output: "
                + json.dumps(criteria, default=str, indent=4)
            )

            if post_is_url(criteria):
                app.logger.debug(
                    "Matching post found querying post from database and passing to post.html"
                )

                post = post_get(
                    criteria["categories"], criteria["posted_on"], criteria["title"]
                )
                    
                posted_on_iso_8601 = post.posted_on.strftime("%Y%m%dT%H%M%S.%fZ")
                posted_on_mm_dd_YYYY = post.posted_on.strftime("%b %d, %Y")

                return render_template(
                    "post.html",
                    title=post.title,
                    description=post.title,
                    post=post,
                    posted_on_iso_8601=posted_on_iso_8601,
                    posted_on_mm_dd_YYYY=posted_on_mm_dd_YYYY,
                )
    except Exception:
        app.logger.debug("Exception thrown, rendering 404")
        return render_template('errors/404.html'), 404

@blog.route("/about", methods=["GET"])
def about():
    return render_template(
        "about.html", title="Seth Griffin | About", description="Seth Griffin | About"
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

@blog.errorhandler(404)
def page_not_found(error):
    app.logger.warning(f"404 for path: {request.path} | Referrer: {request.referrer}")
    return render_template('errors/404.html', error=error), 404

@blog.errorhandler(500)
def internal_server_error(error):
    app.logger.warning(f"500 error: {error}\nTraceBack: {traceback.format_exc()}")
    return render_template('errors/500.html', error=error), 500
