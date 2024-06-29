-- create_table.sql

-- Drop table if it exists
DROP TABLE IF EXISTS user_profile;

-- Create new table
CREATE TABLE user_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    gender TEXT NOT NULL,
    dob TEXT NOT NULL,
    education TEXT NOT NULL,
    salary INTEGER,
    location TEXT,
    skills TEXT,
    experience INTEGER,
    bio TEXT
);

INSERT INTO user_profile (name, email, gender, dob, education, salary, location, skills, experience, bio)
VALUES 
    ('John Doe', 'john.doe@example.com', 'Male', '1990-05-15', 'Bachelor\'s Degree', 70000, 'New York', 'Python, SQL, JavaScript', 5, 'Experienced software engineer with a focus on web development.'),
    ('Jane Smith', 'jane.smith@example.com', 'Female', '1988-09-21', 'Master\'s Degree', 85000, 'San Francisco', 'Java, C++, Agile', 7, 'Senior software developer with over 10 years of experience.'),
    ('Mike Johnson', 'mike.johnson@example.com', 'Male', '1995-03-10', 'Bachelor\'s Degree', 60000, 'Chicago', 'React, Node.js, MongoDB', 3, 'Front-end developer passionate about creating user-friendly interfaces.');
