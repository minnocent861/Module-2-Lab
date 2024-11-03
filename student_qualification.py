"""
Author: Maika Innocent
Date: 11/02/2024
This app accepts student first names and last names  and GPAs, then tests if they qualify for the Dean's List or the Honor Roll. 
The program will stop processing if 'ZZZ' is entered as the last name.

"""
while True:
    # Input student's last name
    student_last_name = input("Please enter the student's last name (enter 'ZZZ' to quit): ")

    # Quit if the last name entered is 'ZZZ'
    if student_last_name.upper() == 'ZZZ':
        print("Enter a valid last name")
        break

    # Input student's first name
    student_first_name = input("Please enter the student's first name: ")

    # Ask for and accept the student's GPA as a float
    try:
        gpa = float(input("please enter student's GPA: "))
    except ValueError:
        print("Error. Enter a valid GPA ")
        continue

    #Check for Dean's list or Honor Roll qualification
    if gpa >= 3.5:
        print("student :" , student_first_name , student_last_name, "has made the Dean's list")  
    elif gpa >= 3.25:
        print("student :" , student_first_name , student_last_name, "has made the Honor Roll")  
    else:
        print("student :" , student_first_name , student_last_name, "Student did not qualify for Dean's list/ Honor Roll ")  



