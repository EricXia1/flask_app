from flask import Flask, request, render_template
app = Flask(__name__)

ButtonPressed = 0
@app.route('/', methods=["GET", "POST"])
def button():
    global ButtonPressed
    if request.method == "POST":
        ButtonPressed += 1
        return render_template("front_end.html", ButtonPressed = ButtonPressed)
    return render_template("front_end.html", ButtonPressed = ButtonPressed)