import os
import uuid

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def about():
    """Teach the Ikigai Concept"""
    return render_template("about.html")


@app.route("/exercise", methods=["GET", "POST"])
@login_required
def exercise():
    """Exercise to fill you ikigai"""
    return render_template("exercise.html")

import uuid

@app.route("/submit_exercise", methods=["POST"])
def submit_exercise():
    # Generate a UUID
    id = str(uuid.uuid4())

    love = request.form.get("love")
    needs = request.form.get("needs")
    paid = request.form.get("paid")
    good = request.form.get("good")
    purpose = request.form.get("purpose")
    passion = request.form.get("passion")
    mission = request.form.get("mission")
    vocation = request.form.get("vocation")
    ikigai = request.form.get("ikigai")

    try:
        db.execute("INSERT INTO ikigai_responses (id, love, needs, paid, good, purpose, passion, mission, vocation, ikigai) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   id, love, needs, paid, good, purpose, passion, mission, vocation, ikigai)
    except Exception as e:
        app.logger.error(f'INSERT INTO ikigai_responses (id, love, needs, paid, good, purpose, passion, mission, vocation, ikigai) VALUES ({id}, {love}, {needs}, {paid}, {good}, {purpose}, {passion}, {mission}, {vocation}, {ikigai})')
        app.logger.error(f'Error while submitting exercise: {e}')
        return apology("An error occurred. Please try again.")

    return redirect("/thanks")




@app.route("/result")
@login_required
def result():
    """Your ikigai result"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/impact", methods=["GET", "POST"])
@login_required
def impact():
    """How to impact more than a million people."""
    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

    if not email or not password or not confirm:
        return apology("No empty Fields")

    if len(password) < 8:
        return apology("Password must be at least 8 characters")

    if password != confirm:
        return apology("Passwords Do Not Match")

    hash = generate_password_hash(password)

    try:
        newUser = db.execute ("INSERT INTO users(username, hash) VALUES (?, ?)", email, hash)
    except:
        return apology("User Already Used")

    session["user_id"] = newUser

    return redirect("/")




@app.route("/share", methods=["GET", "POST"])
@login_required
def share():
    """Share your results"""
    return apology("TODO")
