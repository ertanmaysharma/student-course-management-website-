CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code VARCHAR(10) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudent_id INTEGER NOT NULL,
    ecourse_id INTEGER NOT NULL,
    FOREIGN KEY (estudent_id) REFERENCES student(student_id),
    FOREIGN KEY (ecourse_id) REFERENCES course(course_id)
);

INSERT OR IGNORE INTO course (course_id, course_code, course_name, course_description) VALUES
(1, 'CSE01', 'MAD I', 'Modern Application Development - I'),
(2, 'CSE02', 'DBMS', 'Database management Systems'),
(3, 'CSE03', 'PDSA', 'Programming, Data Structures and Algorithms using Python'),
(4, 'BST13', 'BDM', 'Business Data Management');