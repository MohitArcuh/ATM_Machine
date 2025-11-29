# Flask API
from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
    return """
    <h1> "I am Home Page" </h1>
    <h2> "I am running in Flask" </h2>
    """
@app.route("/about")
def about():
    return """ 
    <h1> "Introduction" </h1>
    <h2> "I am a student of VGU" </h2>
    """
if __name__ == "__main__":
    app.run(debug=True)