from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def button():
    return render_template("front_end.html", ButtonPressed = "hi")