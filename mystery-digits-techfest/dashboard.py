from main import app,session,request,render_template,redirect,url_for
from dbms import users
from image_generator import generator


@app.route("/game")
def game():
	if "email" in session:
		level=int(session["level"])
		generator.generate_and_get_digits(800,600,1,"/static/save.png")

		return render_template("dashboard.html",lvl=session["level"])
	else:
		return redirect("/")


@app.route("/logout")
def logout():
	if "email" in session:
		session.clear()
	return redirect("/")