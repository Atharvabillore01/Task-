from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import date

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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        step = int(request.form.get('step', 1))

        if step == 1:
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            if password != confirm_password:
                flash("Passwords do not match.", 'error')
                return render_template('signup.html', step=1)

            session['signup_data'] = {
                'email': email,
                'password': password
            }
            return render_template('signup.html', step=2)

        elif step == 2:
            signup_data = session.get('signup_data', {})
            username = request.form['username']
            name = request.form['name']

            signup_data.update({
                'username': username,
                'name': name
            })

            session['signup_data'] = signup_data
            return render_template('signup.html', step=3)

        elif step == 3:
            signup_data = session.get('signup_data', {})
            gender = request.form['gender']

            signup_data.update({
                'gender': gender
            })

            session['signup_data'] = signup_data
            return render_template('signup.html', step=4)

        elif step == 4:
            signup_data = session.get('signup_data', {})
            dob = request.form['dob']

            signup_data.update({
                'dob': dob
            })

            session['signup_data'] = signup_data
            return render_template('signup.html', step=5)

        elif step == 5:
            signup_data = session.get('signup_data', {})
            education = request.form['education']
            salary = request.form['salary']

            signup_data.update({
                'education': education,
                'salary': salary
            })

            session['signup_data'] = signup_data
            return render_template('signup.html', step=6)

        elif step == 6:
            signup_data = session.get('signup_data', {})
            location = request.form['location']
            skills = request.form['skills']
            experience = request.form['experience']
            bio = request.form['bio']

            signup_data.update({
                'location': location,
                'skills': skills,
                'experience': experience,
                'bio': bio
            })

            # Save data to the database
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            try:
                c.execute('''INSERT INTO user_profile (username, password, email, name, gender, dob, education, salary, location, skills, experience, bio)
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                          (signup_data['username'], signup_data['password'], signup_data['email'], signup_data['name'], 
                           signup_data['gender'], signup_data['dob'], signup_data['education'], signup_data['salary'], 
                           signup_data['location'], signup_data['skills'], signup_data['experience'], signup_data['bio']))
                conn.commit()
                flash("Account created successfully.", 'success')
                session.pop('signup_data', None)
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash("Username already exists. Please choose another username.", 'error')
            finally:
                conn.close()

    return render_template('signup.html', step=1)

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
            session['email'] = email
            flash("Login successful.", 'success')
            return redirect(url_for('profile'))
        else:
            flash("Invalid credentials. Please try again.", 'error')

    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'email' not in session:
        flash("Please log in first.", 'error')
        return redirect(url_for('login'))

    email = session['email']
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM user_profile WHERE email = ?', (email,))
    user_profile = c.fetchone()
    conn.close()

    return render_template('profiles.html', user_profile=user_profile)

@app.route('/logout')
def logout():
    session.pop('email', None)
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

def current_user():
    if 'email' in session:
        email = session['email']
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT * FROM user_profile WHERE email = ?', (email,))
        user_profile = c.fetchone()
        conn.close()
        return user_profile
    return None

@app.route('/edit', methods=['GET', 'POST'])
def edit_profile():
    """
    This route handles editing user profiles.
    """
    if 'email' not in session:
        flash("Please sign up or log in first.", 'error')
        return redirect(url_for('signup'))

    user_profile = current_user()

    if request.method == 'POST':
        username = request.form['username']
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

        # Update database with prepared statement to prevent SQL injection
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        try:
            c.execute('''UPDATE user_profile SET username = ?, name = ?, email = ?, gender = ?, dob = ?, education = ?, salary = ?, location = ?, skills = ?, experience = ?, bio = ? 
                         WHERE email = ?''', (username, name, email, gender, dob, education, salary, location, skills, experience, bio, user_profile[4]))
            conn.commit()
            flash("Profile updated successfully.", 'success')
        except sqlite3.Error as e:
            flash(f"Error updating profile: {e}", 'error')
        finally:
            conn.close()
        return redirect(url_for('profile'))

    return render_template('edit_profile.html', user_profile=user_profile)

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
