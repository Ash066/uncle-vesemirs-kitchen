import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Functions passing the database category documents to site
@app.route("/get_landing")
def get_landing():
    return render_template("index.html")


@app.route("/get_potions")
def get_potions():
    potions = mongo.db.potions.find()
    return render_template("potions.html", potions=potions)


@app.route("/get_bombs")
def get_bombs():
    bombs = mongo.db.bombs.find()
    return render_template("bombs.html", bombs=bombs)


@app.route("/get_blade_oils")
def get_blade_oils():
    blade_oils = mongo.db.blade_oils.find()
    return render_template("blade_oils.html", blade_oils=blade_oils)


@app.route("/get_decoctions")
def get_decoctions():
    decoctions = mongo.db.decoctions.find()
    return render_template("decoctions.html", decoctions=decoctions)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# User registration funtions
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checking if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


# User login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checking if a username already exists in the user database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# User logout function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
