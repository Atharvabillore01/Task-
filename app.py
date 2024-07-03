from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)
DATABASE = 'mydb.db'

# Database setup
def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_profile
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL,
                 name TEXT,
                 email TEXT,
                 gender TEXT,
                 dob TEXT,
                 education TEXT,
                 salary INTEGER,
                 location TEXT,
                 skills TEXT,
                 experience INTEGER,
                 bio TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            error = "Passwords do not match."
            return render_template('signup.html', error=error)
        
        # Save the username and password to the database
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''INSERT INTO user_profile (username, password) VALUES (?, ?)''', (username, password))
        conn.commit()
        conn.close()
        
        return redirect(url_for('additional_details'))
    return render_template('signup.html')

@app.route('/additional_details', methods=['GET', 'POST'])
def additional_details():
    max_date = date.today().isoformat()
    if request.method == 'POST':
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
        
        # Update the latest user profile with additional details
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''UPDATE user_profile SET name = ?, email = ?, gender = ?, dob = ?, education = ?, salary = ?, location = ?, skills = ?, experience = ?, bio = ? 
                     WHERE id = (SELECT MAX(id) FROM user_profile)''', 
                     (name, email, gender, dob, education, salary, location, skills, experience, bio))
        conn.commit()
        conn.close()
        
        return redirect(url_for('show_profiles'))
    return render_template('additional_details.html', max_date=max_date)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM user_profile WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            return redirect(url_for('show_profiles'))
        else:
            error = "Invalid credentials. Please try again."
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/search')
def search_page():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM user_profile')
    profiles = c.fetchall()
    conn.close()
    
    return render_template('search.html', users=profiles)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
