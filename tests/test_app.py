import app as myapp


def test_home():
    c = myapp.app.test_client()
    r = c.get("/")
    assert r.status_code == 200
    assert b"Hello, World!" in r.data


def test_about():
    c = myapp.app.test_client()
    r = c.get("/about")
    assert r.status_code == 200
    assert b"About page" in r.data
