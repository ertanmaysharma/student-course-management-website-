from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))

class Course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10), unique=True, nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    course_description = db.Column(db.Text)

class Enrollment(db.Model):
    __tablename__ = "enrollments"

    enrollment_id = db.Column(db.Integer, primary_key=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/student/create', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        roll = request.form.get('roll')
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        courses = request.form.getlist('courses')
        
        existing_student = Student.query.filter_by(roll_number=roll).first()
        if existing_student:
            return render_template('exists.html')
        
        new_student = Student(roll_number=roll, first_name=f_name, last_name=l_name)
        db.session.add(new_student)
        db.session.commit()
        
        for course_val in courses:
            course_id = int(course_val.split('_')[1])
            enrollment = Enrollment(estudent_id=new_student.student_id, ecourse_id=course_id)
            db.session.add(enrollment)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/student/<int:student_id>')
def student_details(student_id):
    student = Student.query.get_or_404(student_id)
    enrollments = Enrollment.query.filter_by(estudent_id=student_id).all()
    courses = []
    for enr in enrollments:
        course = Course.query.get(enr.ecourse_id)
        if course:
            courses.append(course)
    return render_template('student.html', student=student, courses=courses)

@app.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        courses = request.form.getlist('courses')
        
        student.first_name = f_name
        student.last_name = l_name
        db.session.commit()
        
        Enrollment.query.filter_by(estudent_id=student_id).delete()
        db.session.commit()
        
        for course_val in courses:
            course_id = int(course_val.split('_')[1])
            enrollment = Enrollment(estudent_id=student_id, ecourse_id=course_id)
            db.session.add(enrollment)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    enrollments = Enrollment.query.filter_by(estudent_id=student_id).all()
    selected_courses = [enr.ecourse_id for enr in enrollments]
    return render_template('update.html', student=student, selected_courses=selected_courses)

@app.route('/student/<int:student_id>/delete', methods=['GET', 'POST'])
def delete_student(student_id):
    Enrollment.query.filter_by(estudent_id=student_id).delete()
    Student.query.filter_by(student_id=student_id).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)