from main import app,session,request,render_template,redirect,url_for
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import os
import pathlib
import requests
from dbms import users

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


GOOGLE_CLIENT_ID = "430968654550-bc43t3q8iadeqtggqrjc4p32sr8m913n.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

def find_dup():
	data=users.read_users()
	for i in data:
		if str(i[3])==str(session["email"]):
			session["level"]=i[5]
			session["tries"]=i[6]
			return True


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  
        else:
            return function()

    return wrapper

@app.route("/login")
def login():
	return render_template("login.html")


@app.route("/getDetails", methods=["POST"])
def getData():
    if request.method == "POST":
        data = request.form
        phone = data.get('phone')
        name = data.get('name')
        
        print("Received Phone:", phone)
        print("Received Name:", name)
        
        session["phone"]=phone
        session["name"]=name
        return "Data received successfully",200 

	
@app.route("/login_google")
def login_google():
	authorization_url, state = flow.authorization_url()
	session["state"] = state

	return redirect(authorization_url)


@app.route("/callback")
def callback():
	flow.fetch_token(authorization_response=request.url)
	if not session["state"] == request.args["state"]:
		abort(500)  
	credentials = flow.credentials
	request_session = requests.session()
	cached_session = cachecontrol.CacheControl(request_session)
	token_request = google.auth.transport.requests.Request(session=cached_session)
	id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
		audience=GOOGLE_CLIENT_ID
	)
	session["google_id"] = id_info.get("sub")
	session["email"] = id_info.get("email")
	session["pic"] = id_info.get("picture")
	val=find_dup()
	if val:
		users.update_user(email=session["email"],username=session['name'],phone=session["phone"],profile_url=session["pic"])
	else:
		session.clear()
		return render_template("index.html",err="you have not registered!")

	return redirect("/game")
