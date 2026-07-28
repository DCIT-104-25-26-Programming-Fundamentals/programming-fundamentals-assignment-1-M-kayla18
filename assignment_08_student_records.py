# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student(students):
    student = {
        "name": "Mickella Kud",
        "id": "BE22459896",
        "scores": [78, 88, 96]
    }

    students.append(student)
    print('Student "Mickella Kud" added successfully.')


def display_students(students):
    if len(students) == 0:
        print("No student records found.")
        return

    print("------------------------------------------------------------")
    print("Name\t\tID\t\tScores\t\tAverage")
    print("------------------------------------------------------------")

    for student in students:
        total = 0

        for score in student["scores"]:
            total += score

        if len(student["scores"]) > 0:
            average = round(total / len(student["scores"]), 2)
        else:
            average = 0

        scores = ""
        for i in range(len(student["scores"])):
            scores += str(student["scores"][i])
            if i != len(student["scores"]) - 1:
                scores += ", "

        print(student["name"], "\t", student["id"], "\t", scores, "\t", average)

    print("------------------------------------------------------------")


def calculate_average(students):
    if len(students) == 0:
        print("No student records found.")
        return

    student_id = input("Enter student ID: BE22459896")

    found = False

    for student in students:
        if student["id"] == student_id:
            total = 0

            for score in student["scores"]:
                total += score

            average = round(total / len(student["scores"]), 2)

            print(student["name"] + "'s average score:87.33", average)
            found = True
            break

    


def menu():
    print("\n================================")
    print(" STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        menu()

        choice = input("Enter your choice (1-4):2 ")

        


main()