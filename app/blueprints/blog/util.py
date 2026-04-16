from app.blueprints.data.models import Post
from app.extensions import db


def post_get(categories, posted_on, title):
    try:
        return (db.session.query(Post)
        # .filter(Post.posted_on == posted_on)
        .filter(Post.categories == categories)
        .filter(Post.title.ilike(title))
        .one())
    except:
        raise Exception("404") 

def post_url_to_criteria(full_path):
    path_segments = full_path.split("/")
    title = path_segments.pop().replace("-", " ").replace(".html", "")
    posted_on_1 = path_segments.pop()
    posted_on_2 = path_segments.pop()
    posted_on_3 = path_segments.pop()
    posted_on = posted_on_3 + "-" + posted_on_2 + "-" + posted_on_1

    categories = ",".join(path_segments)

    return {"title": title, "posted_on": posted_on, "categories": categories}


def post_is_url(post_criteria):
    post_is_url = True

    post = post_get(
        post_criteria["categories"], post_criteria["posted_on"], post_criteria["title"]
    )

    if post is None:
        post_is_url = False

    return post_is_url
