import flask

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

#index.html
@app.route("/")
def index():
  ...
  return render_template("index.html")
  
#register tab
  #gforms integration
    #1st stage: details
    #2nd stage: further details (video/essay/etc)
  #speakers list
  #validating whether they've finished all stages or not
  
#tickets tab
  #Display Hash Key/QR Code according to db
