from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Grade calculation function
def calculate_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'Fail'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form.get('name')
    roll_no = request.form.get('roll_no')
    department = request.form.get('department')
    semester = request.form.get('semester')
    
    # Get marks for 3 subjects
    subject1_marks = int(request.form.get('subject1_marks', 0))
    subject2_marks = int(request.form.get('subject2_marks', 0))
    subject3_marks = int(request.form.get('subject3_marks', 0))
    
    # Validate marks (assuming max marks per subject is 100)
    if not all(0 <= mark <= 100 for mark in [subject1_marks, subject2_marks, subject3_marks]):
        flash('Marks should be between 0 and 100 for each subject!', 'error')
        return redirect(url_for('index'))
    
    # Calculate performance metrics
    total_marks = subject1_marks + subject2_marks + subject3_marks
    percentage = round((total_marks / 300) * 100, 2)  # Assuming 100 marks per subject
    grade = calculate_grade(percentage)
    
    # Prepare student data
    student_data = {
        'name': name,
        'roll_no': roll_no,
        'department': department,
        'semester': semester,
        'subject1_marks': subject1_marks,
        'subject2_marks': subject2_marks,
        'subject3_marks': subject3_marks,
        'total_marks': total_marks,
        'percentage': percentage,
        'grade': grade
    }
    
    return render_template('dashboard.html', student=student_data)

if __name__ == '__main__':
    app.run(debug=True)
