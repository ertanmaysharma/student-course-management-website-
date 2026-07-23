# student-course-management-website-
Student Management System built with Flask and SQLite featuring complete CRUD operations and course enrollment management using SQLAlchemy.

# Student Management System

A simple web application built using **Flask**, **SQLite**, and **SQLAlchemy** to manage student records and course enrollments. The application provides complete CRUD functionality for students while maintaining enrollment information.

## Features

- Add new students
- View student details
- Update student information
- Delete student records
- Enroll students in multiple courses
- Display enrolled courses for each student
- Duplicate roll number validation

## Tech Stack

- Python
- Flask
- SQLite
- Flask-SQLAlchemy
- HTML5
- Jinja2

## Project Structure

```
.
├── app.py
├── database.sqlite3
├── templates
│   ├── index.html
│   ├── create.html
│   ├── update.html
│   ├── student.html
│   └── exists.html
└── static
```

## Database Tables

- Student
- Course
- Enrollments

## Routes

| Route | Description |
|-------|-------------|
| `/` | Display all students |
| `/student/create` | Create a new student |
| `/student/<id>` | View student details |
| `/student/<id>/update` | Update student information |
| `/student/<id>/delete` | Delete a student |

## How to Run

1. Clone the repository.
2. Install dependencies:

```bash
pip install flask flask-sqlalchemy
```

3. Ensure `database.sqlite3` contains the required course records.
4. Start the application:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

## License

This project was developed for academic learning purposes.
