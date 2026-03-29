from xml.etree import ElementTree


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
            assert category_node.get("term") in [
                "programming",
                "functional-programming",
                "lisp",
                "scheme",
                "arc",
            ]

        """ Testing one should be enough since the file is generated in template loop """
        break
