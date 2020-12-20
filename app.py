from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add", methods=["POST", "GET"])
def addTodo():
    if request.method == "POST":
        print(request.form["todo"])
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)