CREATE TABLE IF NOT EXISTS user_profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    bio TEXT
);

INSERT INTO user_profile (username, password, name, email, gender, dob, education, salary, location, skills, experience, bio)
VALUES
('john_doe', 'password123', 'John Doe', 'john.doe@example.com', 'Male', '1990-05-15', 'Bachelor of Science', 60000, 'New York', 'Python, SQL', 5, 'Experienced developer with a focus on web technologies.'),
('jane_smith', 'securepassword', 'Jane Smith', 'jane.smith@example.com', 'Female', '1985-09-28', 'Master of Business Administration', 75000, 'San Francisco', 'Project Management, Leadership', 8, 'Experienced manager with a proven track record in leading teams.'),
('alex_jones', 'password123', 'Alex Jones', 'alex.jones@example.com', 'Male', '1995-03-20', 'Bachelor of Arts', 45000, 'Chicago', 'Graphic Design, Adobe Suite', 3, 'Creative designer specializing in digital and print media.'),
('emily_wilson', 'emily_password', 'Emily Wilson', 'emily.wilson@example.com', 'Female', '1992-11-10', 'Bachelor of Engineering', 70000, 'Los Angeles', 'JavaScript, React, Node.js', 6, 'Full-stack developer passionate about creating responsive web applications.');

DELETE FROM user_profile
WHERE id BETWEEN 5 AND 8;
