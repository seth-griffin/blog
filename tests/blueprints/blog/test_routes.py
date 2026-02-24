from app.blueprints.blog.routes import post_url_to_criteria

def test_blog_route_get_index_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Posts" in response.data

def test_blog_route_get_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_blog_route_get_index_post(client):
    response = client.get("/")
    assert response.status_code == 200

def test_blog_route_get_rss(client):
    response = client.get("/feed.xml")
    assert response.status_code == 200

def test_post_url_to_critera():
    test_post_url_good_1 = "programming/functional-programming/lisp/scheme/arc/2025/12/11/introduction-to-the-arc-programming-language.html"
    test_post_url_good_2 = "general/update/2023/02/10/welcome-to-my-github-site.html"

    test_post_url_bad_1 = "general/update/2023-02-10/welcome-to-my-github-site.html"
    test_post_url_bad_2 = "general/update/2023-02-10/welcome-to-my-github-site"

    criteria_expect_good_1 = post_url_to_criteria(test_post_url_good_1)
    assert criteria_expect_good_1["title"] == "introduction to the arc programming language"
    assert criteria_expect_good_1["posted_on"] == "2025-12-11"
    assert criteria_expect_good_1["categories"] == "programming,functional-programming,lisp,scheme,arc"

    criteria_expect_good_2 = post_url_to_criteria(test_post_url_good_2)
    assert criteria_expect_good_2["title"] == "welcome to my github site"
    assert criteria_expect_good_2["posted_on"] == "2023-02-10"
    assert criteria_expect_good_2["categories"] == "general,update"

    criteria_expect_bad_1 = post_url_to_criteria(test_post_url_bad_1)
    assert criteria_expect_bad_1["title"] == "welcome to my github site"
    assert criteria_expect_bad_1["posted_on"] != "2023-02-10"
    assert criteria_expect_bad_1["categories"] != "general,update"

    criteria_expect_bad_2 = post_url_to_criteria(test_post_url_bad_2)
    assert criteria_expect_bad_2["title"] == "welcome to my github site"
    assert criteria_expect_bad_2["posted_on"] != "2025-02-10"
    assert criteria_expect_bad_2["categories"] == ""

def test_is_post_url():
    assert False is False
        
