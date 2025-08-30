import bugintroduced as bi
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, World!"

@app.get("/about")
def about():
    return "About page"

if __name__ == "__main__":
    app.run(debug=True)
