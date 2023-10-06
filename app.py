from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong, random secret key

# Define a dictionary to store user credentials and UIDs (for demonstration purposes)
user_data = {
    'czabhishek': {
        'password': '82025840',
        'uid': str(random.randint(10000000, 99999999))
    }
}

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/home.html')
def home():
    # Check if the user is logged in by verifying the session
    if 'username' in session:
        username = session['username']
        uid = user_data.get(username, {}).get('uid', 'N/A')
        return f"Welcome, {username}! Your UID is: {uid}"
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # In a real application, you would perform secure authentication
    # Here, we're just checking if the username and password match the stored data
    if username in user_data and user_data[username]['password'] == password:
        session['username'] = username  # Store the username in the session
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the user's session to log them out
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
