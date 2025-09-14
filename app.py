from flask import Flask, redirect, render_template, request, flash, url_for
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "supersecret"

Session(app)

#Homepage
@app.route("/")
def index():
    ...
    return render_template("index.html")

#Newsletter subscription
@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if not email:
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("index"))

    #Save email to database or mailing list service
    ...
    flash(f"Thanks for subscribing, {email}!", "success")
    return redirect(url_for("index"))

#About page
@app.route("/about")
def about():
    ...
    return render_template("about.html")

#Events page
@app.route("/events")
def events():
    ...
    return render_template("events.html")

#Speakers page + speakers registration
@app.route("/speakers")
def speakers():
    ...
    return render_template("speakers.html")
