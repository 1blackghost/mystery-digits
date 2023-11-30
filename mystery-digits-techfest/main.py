
#imports
from flask import *

#Creation of flask app
app=Flask(__name__)
app.secret_key="jdhfivgbeifg549305tigjnbmvflkbvm9548g5j"

#Main Entry Point Here.

@app.route("/privacypolicy")
def privacy():
	return render_template("privacy.html")
@app.route("/")
def home():
    if "email" in session:
        return redirect("/game")
    return render_template("index.html")

with app.app_context():
    #importing views from different files
    from login import *
    from dashboard import *
    from admin import *



if __name__=="__main__":
    app.run(debug=True)
