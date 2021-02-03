import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
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


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
