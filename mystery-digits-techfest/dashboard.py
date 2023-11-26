from main import app,session,request,render_template,redirect,url_for
from dbms import users
from image_generator import generator
from packages import name_generator


@app.route("/game",methods=['GET','POST'])
def game():
	if request.method == "POST":

		data = request.form
		val = data.get('val')
		vals=[]
		for i in val:
			vals.append(str(i))
		check = []
		print(vals)
		print(session["digits"])
		for i in session["digits"]:
			if i in vals:
				check.append(1)

		if len(check) == len(session["digits"]):


			session["level"]=int(session["level"])+1

			users.update_user(session["email"],current_level=int(session["level"]))
			session.pop("filepath")
			return "ok",200
		else:
			session["tries"]=int(session["tries"])-1
			users.update_user(session["email"],tries=int(session["tries"]))
			return "false",400

	if "email" in session:
		level=int(session["level"])
		if session["tries"]==0:
			return "tries finished!"
		if "filepath" not in session:
			filename=name_generator.generate_randomest_string(10)+".png"
			session["filepath"]="/static/"+filename
			session["digits"]=generator.generate_and_get_digits(800,600,level,filename)
			print(session["digits"])
		return render_template("dashboard.html",lvl=session["level"],filename=session["filepath"],tries=session["tries"])
	else:
		return redirect("/")


@app.route("/logout")
def logout():
	if "email" in session:
		session.clear()
	return redirect("/")
