from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class todos(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    todo = db.Column(db.String(100))

    def __init__(self, todo):
        self.todo = todo


@app.route("/")
def home():
    # GET TODO FROM DB
    todoFromDB = db.session.query(todos).all()
    todosList = []
    for todo in todoFromDB:
        todosList.append(todo.todo)
    return render_template("home.html", todos=todosList)


@app.route("/add", methods=["POST"])
def addTodo():
    todo = request.form["todo"]
    print(f"------------------------\n{todo}\n------------")
    if len(todo) > 3:
        todoOB = todos(todo)
        db.session.add(todoOB)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)