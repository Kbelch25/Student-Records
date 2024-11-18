import csv

# Function Definitions

def read_csv_file(student_records):
    """Reads and returns data from a CSV file containing student records."""
    student_data = []
    invalid_data = []
    try:
        with open(f"{student_records}.csv", 'r') as file:
            reader = csv.reader(file, delimiter= ',')
            for row in reader:
                if len(row) == 5:
                    student = {
                        'ID': row[0],
                        'FirstName': row[1],
                        'LastName': row[2],
                        'Score': row[3],
                        'Program': row[4]
                    }
                    # Validate score
                    try:
                        score = float(student['Score'])
                        if score < 0 or score > 100:
                            invalid_data.append(row)  # Invalid score
                        else:
                            student_data.append(student)
                    except ValueError:
                        # Invalid score format, add to invalid data
                        invalid_data.append(row)
                    # Validate missing last name
                    if not student['LastName']:
                        invalid_data.append(row)
                else:
                    # Invalid record structure
                    invalid_data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{student_records}' was not found.")
    return student_data, invalid_data

def calculate_average_grade(data):
    """Calculates and displays the average grade for all students."""
    total_score = 0
    count = 0
    for student in data:
        try:
            score = float(student['Score'])
            total_score += score
            count += 1
        except ValueError:
            continue
    if count > 0:
        average_score = total_score / count
        print(f"\nThe average grade for all students is: {average_score:.2f}")
    else:
        print("No valid scores available for calculation.")

def calculate_average_grade_by_program(data, program):
    """Calculates and displays the average grade for a specific program."""
    total_score = 0
    count = 0
    for student in data:
        if student['Program'] == program:
            try:
                score = float(student['Score'])
                total_score += score
                count += 1
            except ValueError:
                continue
    if count > 0:
        average_score = total_score / count
        print(f"\nThe average grade for {program} is: {average_score:.2f}")
    else:
        print(f"No valid scores available for {program}.")

def display_highest_grade_record(data):
    """Displays the record with the highest grade."""
    highest_record = max(data, key=lambda x: float(x['Score']) if x['Score'].replace('.', '', 1).isdigit() else float('-inf'))
    print("\nHighest grade record:")
    print(f"ID: {highest_record['ID']}, Name: {highest_record['FirstName']} {highest_record['LastName']}, Score: {highest_record['Score']}, Program: {highest_record['Program']}")

def display_lowest_grade_record(data):
    """Displays the record with the lowest grade."""
    lowest_record = min(data, key=lambda x: float(x['Score']) if x['Score'].replace('.', '', 1).isdigit() else float('inf'))
    print("\nLowest grade record:")
    print(f"ID: {lowest_record['ID']}, Name: {lowest_record['FirstName']} {lowest_record['LastName']}, Score: {lowest_record['Score']}, Program: {lowest_record['Program']}")

def display_students_in_program(data, program):
    """Displays students in a specific program."""
    print(f"\nStudents in {program}:")
    for student in data:
        if student['Program'] == program:
            print(f"ID: {student['ID']}, Name: {student['FirstName']} {student['LastName']}, Score: {student['Score']}")

def display_sorted_students_by_id(data):
    """Displays all students sorted by student ID."""
    sorted_data = sorted(data, key=lambda x: int(x['ID']))
    print("\nStudents sorted by ID:")
    for student in sorted_data:
        print(f"ID: {student['ID']}, Name: {student['FirstName']} {student['LastName']}, Score: {student['Score']}, Program: {student['Program']}")

def display_invalid_records(invalid_data):
    """Displays invalid records."""
    print("\nInvalid Records:")
    for record in invalid_data:
        print(', '.join(record))

def create_bad_records_file(invalid_data, student_records='BADRECORDS.TXT'):
    """Creates a new file with invalid records."""
    with open(student_records, 'w') as file:
        for record in invalid_data:
            file.write(', '.join(record) + '\n')
    print(f"\n{student_records} has been created.")

# Main Program Loop
def main():
    student_records = 'student_records'
    student_data, invalid_data = read_csv_file(student_records)
    
    if not student_data and not invalid_data:
        return

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Display average grade for all students")
        print("2. Display average grade for each program")
        print("3. Display highest grade record")
        print("4. Display lowest grade record")
        print("5. Display students in MSIT")
        print("6. Display students in MSCM")
        print("7. Display all students in sorted order by student ID")
        print("8. Display invalid records")
        print("9. Create new file with invalid records (BADRECORDS.TXT)")
        print("10. Exit")

        # Get user input
        choice = input("Enter your choice (1-10): ")

        # Handle user input and call respective functions
        if choice == '1':
            calculate_average_grade(student_data)
        elif choice == '2':
            calculate_average_grade_by_program(student_data, 'MSIT')
            calculate_average_grade_by_program(student_data, 'MSCM')
        elif choice == '3':
            display_highest_grade_record(student_data)
        elif choice == '4':
            display_lowest_grade_record(student_data)
        elif choice == '5':
            display_students_in_program(student_data, 'MSIT')
        elif choice == '6':
            display_students_in_program(student_data, 'MSCM')
        elif choice == '7':
            display_sorted_students_by_id(student_data)
        elif choice == '8':
            display_invalid_records(invalid_data)
        elif choice == '9':
            create_bad_records_file(invalid_data)
        elif choice == '10':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

# Run the main function
if __name__ == "__main__":
    main()