
def print_student_totals(students):
    for student in students:
        marks = student["marks"]
        total = marks["Math"] + marks["English"] + marks["Science"]
        print(f"{student['name']} - Total: {total}")

# Student data
students_data = [
    {
        'name': 'John Doe',
        'marks': {
            'Math': 85,
            'English': 90,
            'Science': 78
        }
    },
    {
        'name': 'Jane Smith',
        'marks': {
            'Math': 75,
            'English': 82,
            'Science': 89
        }
    },
    {
        'name': 'Emily Davis',
        'marks': {
            'Math': 93,
            'English': 87,
            'Science': 85
        }
    },
    {
        'name': 'Michael Brown',
        'marks': {
            'Math': 65,
            'English': 70,
            'Science': 60
        }
    },
    {
        'name': 'Chris Johnson',
        'marks': {
            'Math': 88,
            'English': 85,
            'Science': 90
        }
    }
]

# Call the function with the student data
print_student_totals(students_data)




























