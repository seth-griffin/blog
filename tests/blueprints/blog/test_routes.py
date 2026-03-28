import app.blueprints.blog.routes
from app.blueprints.blog.util import post_url_to_criteria, post_is_url
from xml.etree import ElementTree
import pytest


def test_blog_route_get_index_home(client):
    print("test_blog_route_get_index_home")
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


def test_blog_route_test_rss_output_structure(client):
    response = client.get("/feed.xml")
    assert response.status_code == 200
    assert "application/xml" in response.headers["Content-Type"]

    namespaces = {"atom": "http://www.w3.org/2005/Atom"}
    root = ElementTree.fromstring(response.data)

    entry_nodes = root.findall("atom:entry", namespaces)

    """ 
        TODO: How do we validate this against the data set in a practical way? 
        Fixtures? Injected dataset for in memory db? 
        Rn it seems to magically use mysql dataset which is not what we want 
    """

    for entry_node in entry_nodes:
        assert (
            entry_node.find("atom:title", namespaces).text
            == "Introduction to the Arc Programming Language"
        )

        assert (
            entry_node.find("atom:link", namespaces).get("href")
            == "/programming/functional-programming/lisp/scheme/arc/12/11/2025/introduction-to-the-arc-programming-language.html"
        )
        assert entry_node.find("atom:link", namespaces).get("rel") == "alternate"
        assert entry_node.find("atom:link", namespaces).get("type") == "text/html"
        assert (
            entry_node.find("atom:link", namespaces).get("title")
            == "Introduction to the Arc Programming Language"
        )

        assert (
            entry_node.find("atom:published", namespaces).text
            == "20251211T000000.000000Z"
        )

        assert (
            entry_node.find("atom:updated", namespaces).text
            == "20251211T000000.000000Z"
        )

        assert (
            entry_node.find("atom:id", namespaces).text.strip()
            == "/programming/functional-programming/lisp/scheme/arc/12/11/2025/introduction-to-the-arc-programming-language"
        )

        assert entry_node.find("atom:content", namespaces).get("type") == "html"

        xmlns = "{http://www.w3.org/XML/1998/namespace}"
        assert (
            entry_node.find("atom:content", namespaces).get(f"{xmlns}base")
            == "/programming/functional-programming/lisp/scheme/arc/12/11/2025/introduction-to-the-arc-programming-language.html"
        )
        assert entry_node.find("atom:content", namespaces).text is not None

        category_nodes = entry_node.findall("atom:category", namespaces)

        for category_node in category_nodes:
            assert category_node.get("term") == "programming"
            break
            # TODO: Validate full data set once fixtures for in memory db are figured out

        break
        # TODO: Validate full data set once fixtures for in memory db are figured out


def test_post_url_to_critera():
    test_post_url_good_1 = "programming/functional-programming/lisp/scheme/arc/2025/12/11/introduction-to-the-arc-programming-language.html"
    test_post_url_good_2 = "general/update/2023/02/10/welcome-to-my-github-site.html"

    test_post_url_bad_1 = "general/update/2023-02-10/welcome-to-my-github-site.html"
    test_post_url_bad_2 = "general/update/2023-02-10/welcome-to-my-github-site"

    criteria_expect_good_1 = post_url_to_criteria(test_post_url_good_1)
    assert (
        criteria_expect_good_1["title"]
        == "introduction to the arc programming language"
    )
    assert criteria_expect_good_1["posted_on"] == "2025-12-11"
    assert (
        criteria_expect_good_1["categories"]
        == "programming,functional-programming,lisp,scheme,arc"
    )

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


@pytest.mark.skip("Skipping due to pytest.mark.skip being set")
def test_is_post_url():
    criteria_good_1 = {
        "title": "introduction to the arc programming language",
        "posted_on": "2025-12-11",
        "categories": "programming,functional-programming,lisp,scheme,arc",
    }

    criteria_good_2 = {
        "title": "welcome to my github site",
        "posted_on": "2023-02-10",
        "categories:": "general,update",
    }

    criteria_bad_1 = {
        "title": "welcome to my github site",
        "posted_on": "2023-02-10",
        "categories:": "general,update",
    }

    criteria_bad_2 = {
        "title": "welcome to my github site",
        "posted_on": "2023-02-10",
        "categories:": "general,update",
    }

    test_post_url_good_1_post = is_post_url(criteria_good_1)
    test_post_url_good_2_post = is_post_url(criteria_good_2)

    test_post_url_bad_1_post = is_post_url(criteria_bad_1)
    test_post_url_bad_2_post = is_post_url(criteria_bad_2)

    assert test_post_url_good_1_post is not False
    assert test_post_url_good_2_post is not False
    assert test_post_url_bad_1_post is not False
    assert test_post_url_bad_2_post is not False
