from app import app
from app.db_controls import add_account, get_db
from flask import render_template, request


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        func = add_account(name=name, password=password)
        return func

    return render_template("login.html")

@app.route("/list")
def list():
    all_users = get_db("info_table")
    return render_template("list.html", all_users=all_users)



