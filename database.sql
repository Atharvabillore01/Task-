-- Drop existing tables if they exist
DROP TABLE IF EXISTS user_profile;
DROP TABLE IF EXISTS users;

-- Recreate the table with the updated column name
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- Changed column name from password_hash to password
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create user_profile table with foreign key reference to users table
CREATE TABLE user_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
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
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert dummy data into users table
INSERT INTO users (email, password) VALUES
('john.doe@example.com', '1234'),
('jane.smith@example.com', 'hashed_password_2'),
('alice.johnson@example.com', 'hashed_password_3'),
('bob.brown@example.com', 'hashed_password_4'),
('emily.davis@example.com', 'hashed_password_5'),
('michael.wilson@example.com', 'hashed_password_6'),
('laura.martinez@example.com', 'hashed_password_7'),
('david.clark@example.com', 'hashed_password_8'),
('sophia.harris@example.com', 'hashed_password_9'),
('james.lewis@example.com', 'hashed_password_10');

-- Insert dummy data into user_profile table
INSERT INTO user_profile (user_id, name, email, gender, dob, education, salary, location, skills, experience, bio) VALUES
(1, 'John Doe', 'john.doe@example.com', 'Male', '1990-01-01', 'Bachelor of Science', 60000, 'New York', 'Python, SQL, Django', 5, 'A passionate software developer with 5 years of experience.'),
(2, 'Jane Smith', 'jane.smith@example.com', 'Female', '1985-05-15', 'Master of Arts', 70000, 'Los Angeles', 'JavaScript, React, Node.js', 7, 'Creative front-end developer specializing in modern web technologies.'),
(3, 'Alice Johnson', 'alice.johnson@example.com', 'Female', '1992-08-23', 'Bachelor of Engineering', 65000, 'San Francisco', 'Java, Spring, Hibernate', 4, 'Experienced back-end developer with a knack for scalable solutions.'),
(4, 'Bob Brown', 'bob.brown@example.com', 'Male', '1988-11-11', 'Bachelor of Arts', 55000, 'Chicago', 'C++, Embedded Systems', 6, 'Embedded systems engineer with a strong background in C++.'),
(5, 'Emily Davis', 'emily.davis@example.com', 'Female', '1995-02-14', 'Master of Science', 75000, 'Seattle', 'Data Science, Machine Learning, R', 3, 'Data scientist passionate about uncovering insights from data.'),
(6, 'Michael Wilson', 'michael.wilson@example.com', 'Male', '1991-07-30', 'Bachelor of Technology', 68000, 'Austin', 'Cloud Computing, AWS, DevOps', 5, 'Cloud computing expert with experience in AWS and DevOps practices.'),
(7, 'Laura Martinez', 'laura.martinez@example.com', 'Female', '1987-09-09', 'Doctor of Philosophy', 80000, 'Boston', 'Research, Python, Machine Learning', 10, 'Researcher with a PhD in computer science and extensive machine learning expertise.'),
(8, 'David Clark', 'david.clark@example.com', 'Male', '1993-04-18', 'Bachelor of Commerce', 50000, 'Denver', 'SQL, Excel, Financial Analysis', 4, 'Financial analyst with strong skills in SQL and Excel.'),
(9, 'Sophia Harris', 'sophia.harris@example.com', 'Female', '1989-12-25', 'Master of Business Administration', 90000, 'Miami', 'Project Management, Agile, Scrum', 8, 'Experienced project manager with a focus on Agile methodologies.'),
(10, 'James Lewis', 'james.lewis@example.com', 'Male', '1994-03-05', 'Bachelor of Science', 62000, 'Dallas', 'HTML, CSS, JavaScript', 2, 'Junior web developer with a passion for creating beautiful and functional websites.');
