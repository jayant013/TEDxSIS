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
    return render_template("index1.html")

#Newsletter subscription
@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if not email:
        return redirect(url_for("index"))

    #Save email to database or mailing list service
    ...
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




  
#register tab
  #gforms integration
    #1st stage: details
    #2nd stage: further details (video/essay/etc)
  #speakers list
  #validating whether they've finished all stages or not
  
#tickets tab
  #Display Hash Key/QR Code according to db





if __name__ == "__main__":
    app.run(debug=True)
