from main import app, session, request, render_template, redirect, url_for, jsonify
from dbms import users, leader
from image_generator import generator
from packages import name_generator

@app.route("/getL", methods=["GET"])
def get_leaderboard():
    data = leader.read_leaderboard()
    return jsonify(data)

@app.route("/ended")
def end():
    return render_template("end.html")

@app.route("/game", methods=['GET', 'POST'])
def game():
    if "email" not in session:
        return redirect("/")

    if request.method == "POST":
        if "end" in session:
            return jsonify({"error": "error"}), 400

        if "email" not in session:

            return jsonify({"error": "error"}), 400

        data = request.form
        val = data.getlist('val')  # Use getlist to get multiple values
        vals = [str(i) for i in val]
        check = []

        for i in session["digits"]:
            if i in vals:
                check.append(1)

        if len(check) == len(session["digits"]):
            session["level"] = int(session["level"]) + 1
            users.update_user(session["email"], current_level=int(session["level"]))

            # Update leaderboard only when the user successfully completes a level
            leader.sortLb([session["name"], session["level"], 0, session["pic"]])

            session.pop("filepath")
            level = session["level"]
            filename = name_generator.generate_randomest_string(10) + ".png"
            session["filepath"] = "/static/" + filename
            session["digits"] = generator.generate_and_get_digits(800, 600, level, filename)
            session_data = {"level": level, "tries": session["tries"], "filepath": session["filepath"]}
            return jsonify(session_data), 200
        else:
            session["tries"] = int(session["tries"]) - 1
            users.update_user(session["email"], tries=int(session["tries"]))

            level = session["level"]
            tries = session["tries"]
            filepath = session["filepath"]

            if int(session["tries"]) <= 0:
                session_data = {"continue": "false", "level": level, "tries": tries, "filepath": filepath}
            else:
                session_data = {"continue": "true", "level": level, "tries": tries, "filepath": filepath}

            return jsonify(session_data), 400

    if "email" in session:
        level = int(session["level"])
        if session["tries"] <= 0:
            session["end"] = True
            return redirect("/ended")
        if "filepath" not in session:
            filename = name_generator.generate_randomest_string(10) + ".png"
            session["filepath"] = "/static/" + filename
            session["digits"] = generator.generate_and_get_digits(800, 600, level, filename)

        return render_template("dashboard.html", lvl=session["level"], filename=session["filepath"],
                               tries=session["tries"])
    else:
        return redirect("/")


@app.route("/logout")
def logout():
    if "email" in session:
        session.clear()

    return redirect("/")
