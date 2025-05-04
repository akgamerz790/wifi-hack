from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Define the absolute path to the login-portal folder (where login.html is)
login_folder = os.path.join(os.path.dirname(__file__), '../login-portal')

@app.route("/")
def home():
    # Serve the redirect page from templates
    return render_template("login.html")

@app.route("/login-portal/login.html")
def serve_login():
    # Serve the login.html file from the login-portal directory
    return send_from_directory(login_folder, 'login.html')

if __name__ == "__main__":
    app.run(debug=True)
