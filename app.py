from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from datetime import date

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'mydb.db'

# Database setup
def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_profile
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT NOT NULL,
                 gender TEXT NOT NULL,
                 dob TEXT NOT NULL,
                 education TEXT NOT NULL,
                 salary INTEGER,
                 location TEXT,
                 skills TEXT,
                 experience INTEGER,
                 bio TEXT,
                 password TEXT NOT NULL)''')  # Added password field
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin_form():
    max_date = date.today().isoformat()
    return render_template('signin.html', max_date=max_date)

@app.route('/submit', methods=['POST'])
def submit_profile():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    dob = request.form['dob']
    education = request.form['education']
    salary = request.form['salary']
    location = request.form['location']
    skills = request.form['skills']
    experience = request.form['experience']
    bio = request.form['bio']
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''INSERT INTO user_profile (name, email, gender, dob, education, salary, location, skills, experience, bio)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                 (name, email, gender, dob, education, salary, location, skills, experience, bio))
    conn.commit()
    conn.close()
    
    return redirect(url_for('show_profiles'))

@app.route('/profiles')
def show_profiles():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM user_profile')
    profiles = c.fetchall()
    conn.close()
    
    return render_template('show_profiles.html', profiles=profiles)

@app.route('/delete/<int:profile_id>', methods=['POST'])
def delete_profile(profile_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM user_profile WHERE id = ?', (profile_id,))
    conn.commit()
    conn.close()
    
    return '', 204  # No content response for successful deletion

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('username')
    password = data.get('password')
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = c.fetchone()
    conn.close()

    if user:
        session['user_id'] = user[0]  # Assuming user ID is at index 0
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False, 'error': 'Invalid credentials'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]  # Assuming user ID is at index 0
            return redirect(url_for('index'))  # Redirect to home page on successful login
        else:
            error = "Invalid credentials. Please try again."
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/search')
def search_page():
    # Placeholder for search functionality
    return "Search Page"

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
