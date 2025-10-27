# Student Performance Dashboard

A Flask-based web application that allows students to enter their academic details and view their performance summary with calculated grades.

## Features

- **Student Information Form**: Collects student details including name, roll number, department, semester, and marks in 3 subjects
- **Performance Calculation**: Automatically calculates total marks, percentage, and grade (A, B, C, or Fail)
- **Clean UI**: Simple, clean dashboard with basic styling
- **Grade System**: 
  - Grade A: 80% and above
  - Grade B: 70% - 79%
  - Grade C: 60% - 69%
  - Fail: Below 60%

## Installation and Setup

1. **Install Python** (if not already installed)
2. **Install Flask**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`

## Usage

1. **Fill the Form**: Enter student details and marks for 3 subjects (out of 100 each)
2. **Submit**: Click "Calculate Performance" to process the data
3. **View Results**: See the performance dashboard with calculated metrics
4. **Add Another**: Use "Add Another Student" to enter more data

## Example Output

| Field | Example Value |
|-------|---------------|
| Name | xyz |
| Roll No | 23CS101 |
| Department | Computer Science |
| Semester | 5 |
| Marks | 80, 76, 88 |
| Total Marks | 244 |
| Percentage | 81.33% |
| Grade | A |

## File Structure

```
dpc lab 6/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Student form page
│   └── dashboard.html    # Performance dashboard
└── README.md             # This file
```

## Technical Details

- **Framework**: Flask 2.3.3
- **Frontend**: Basic HTML/CSS with simple styling
- **Styling**: Clean, minimal design suitable for academic assignments
- **Validation**: Client-side and server-side form validation
- **Responsive**: Basic responsive design

## Grade Calculation Logic

```python
def calculate_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'Fail'
```

## Error Handling

- Form validation for required fields
- Marks validation (0-100 range)
- Flash messages for user feedback
- Graceful error handling

## Future Enhancements

- Database integration for data persistence
- Student login system
- Historical performance tracking
- Export functionality (PDF, Excel)
- Admin panel for managing students
