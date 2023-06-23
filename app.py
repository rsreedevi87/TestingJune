from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_flask():
    return 'This is my first flask prog'

@app.route("/flask_2")
def second():
    return "Python is fun"

app.run(debug=True)
