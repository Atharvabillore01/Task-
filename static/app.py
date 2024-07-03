from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'students.db'

def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 gender TEXT NOT NULL,
                 location TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    location = request.form['location']
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO students (name, age, gender, location) VALUES (?, ?, ?, ?)', (name, age, gender, location))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        conn.close()
    
    return redirect(url_for('show_students'))

@app.route('/students')
def show_students():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    
    return render_template('students.html', students=students)

@app.route('/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute('DELETE FROM students WHERE id = ?', (student_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")
    finally:
        conn.close()
    
    return '', 204  # No content response for successful deletion

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
