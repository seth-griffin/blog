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
    assert response.status_code = 200

def test_blog_route_get_rss(client):
    response = client.get("/feed.xml")
    assert response.status_code = 200

