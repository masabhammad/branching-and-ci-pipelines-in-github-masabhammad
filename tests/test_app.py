import app as myapp

def test_home():
    client = myapp.app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hello, World!" in r.data

def test_about():
    client = myapp.app.test_client()
    r = client.get("/about")
    assert r.status_code == 200
    assert b"About page" in r.data
