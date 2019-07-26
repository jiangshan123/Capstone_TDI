from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This is a user-friendly k-means machine learning website"

@app.route("/test")
def test():
    return "This is a test page"

if __name__ == "__main__":
    app.run()