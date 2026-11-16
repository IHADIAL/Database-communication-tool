import psycopg2 # imports the library that allows comunicaion with the database
conn = psycopg2.connect(host="localhost", database="Assignment 3", user="postgres", password="SQLHadi") 
cur = conn.cursor()
print("Connected to the database successfully!") # establishes a connection to the database and creates a object for executing queries

def getAllStudents(): # exectes a select all query to retrieve all students from the database and prints row by row
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def addStudent(first_name, last_name, email, enrollment_date): # executes a insert query with values provided and checks if the email given is unique
    while True:
        try:
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
            conn.commit()
        except psycopg2.errors.UniqueViolation:
            print("Error: The email address is already in use. Please choose a different email.")
            conn.rollback()
            email = input("Enter a new email address: ")
        else:
            break
    print("Student added successfully!")

def updateStudentEmail(student_id, new_email): # executes a update query to cange the email value of a certain student via id to a new email and checks if the new email is unique
    while True:
        try:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
            conn.commit()
        except psycopg2.errors.UniqueViolation:
            print("Error: The email address is already in use. Please choose a different email.")
            conn.rollback()
            new_email = input("Enter a new email address: ")
        else:
            break
    print("Student email updated successfully!")

def deleteStudent(student_id): # executes a delete query to remove a student via id
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    print("Student deleted successfully!")

def main(): # a simple main menu that shows all commands allows to choose and to exit the program
    while True:
        print("\nStudent Management System")
        print("1. View All Students")
        print("2. Add Student")
        print("3. Update Student Email")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = input("Enter student ID to update email: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            deleteStudent(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    cur.close()
    conn.close()
    print("Database connection closed.")