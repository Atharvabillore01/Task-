from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import date
#current branch
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key for session management
DATABASE = 'mydb.db'

# Database setup
def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_profile
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL,
                 name TEXT,
                 email TEXT UNIQUE NOT NULL,
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

# Function to fetch current user details from database based on session
def current_user():
    if 'username' in session:
        username = session['username']
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM user_profile WHERE username = ?', (username,))
        user_profile = c.fetchone()
        conn.close()
        return user_profile
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']

        if password != confirm_password:
            flash("Passwords do not match.", 'error')
            return render_template('signup.html')

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        try:
            c.execute('''INSERT INTO user_profile (username, password, email) VALUES (?, ?, ?)''', (username, password, email))
            conn.commit()
            flash("Account created successfully. Please provide additional details.", 'success')
            session['username'] = username
            return redirect(url_for('additional_details'))
        except sqlite3.IntegrityError:
            flash("Username or email already exists. Please choose another.", 'error')
        finally:
            conn.close()
        
    return render_template('signup.html')

@app.route('/additional_details', methods=['GET', 'POST'])
def additional_details():
    if 'username' not in session:
        flash("Please sign up or log in first.", 'error')
        return redirect(url_for('signup'))
    
    max_date = date.today().isoformat()
    if request.method == 'POST':
        username = session['username']
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
        try:
            c.execute('''UPDATE user_profile SET name = ?, email = ?, gender = ?, dob = ?, education = ?, salary = ?, location = ?, skills = ?, experience = ?, bio = ? 
                         WHERE username = ?''', 
                         (name, email, gender, dob, education, salary, location, skills, experience, bio, username))
            conn.commit()
            flash("Profile updated successfully.", 'success')
        except sqlite3.Error as e:
            flash(f"Error updating profile: {e}", 'error')
        finally:
            conn.close()
            
        return redirect(url_for('profile'))
    
    return render_template('additional_details.html', max_date=max_date)

@app.route('/profile')
def profile():
    user_profile = current_user()
    if not user_profile:
        flash("Please sign up or log in first.", 'error')
        return redirect(url_for('signup'))

    return render_template('profiles.html', user_profile=user_profile)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM user_profile WHERE email = ? AND password = ?', (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]  # Set session username to the logged-in user's username
            flash("Login successful.", 'success')
            return redirect(url_for('profile'))
        else:
            flash("Invalid credentials. Please try again.", 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", 'info')
    return redirect(url_for('index'))

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

@app.route('/edit')
def edit_profile():
    return render_template('edit_profile.html')

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
