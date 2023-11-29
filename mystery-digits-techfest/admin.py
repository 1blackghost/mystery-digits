from main import app, session, request, render_template, jsonify
from dbms import users

# Hardcoded admin credentials (for demonstration purposes)
admin_username = "admin"
admin_password = "admin123"

# Variable to store the submitted email
submitted_email = None

@app.route('/adminPanel', methods=['GET', 'POST'])
def admin_panel():
    global submitted_email

    if request.method == 'POST':
        # Handle the POST request from /adminPanel
        submitted_email = request.form.get('email')
        users.insert_user(email=submitted_email)
        return jsonify({'message': 'Email submitted successfully'}), 200

    if session.get('admin'):
        return render_template('adminpanel.html')
    else:
        return jsonify({'error': 'Unauthorized access'}), 401

@app.route('/adminLogin', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        data = request.json

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Invalid credentials'}), 400

        if username == admin_username and password == admin_password:
            session['admin'] = True
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 400
    else:
        return render_template('adminlogin.html')

