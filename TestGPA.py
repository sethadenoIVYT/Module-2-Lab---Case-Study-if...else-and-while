"""
Name: Seth Deno
File Name: TestGPA.py
Description: The program will accept a students name and GPA and determine
whether the student makes the Dean's List, Honor Roll, or neither.
"""

lastName = ' ' # Intializes last name variable 

# Controls program loop 
while lastName != 'ZZZ':
    
    lastName = input("Please Enter Your Last Name (Enter 'ZZZ' To Exit): ") # Accepts last name input
    
    if lastName != 'ZZZ': # Makes sure the last name is not ZZZ, otherwise program ends
        
        firstName = input("Please Enter Your First Name: ") # Accepts first name input
        studentGPA = float(input("Please Enter Your GPA: ")) # Accepts student GPA as float
        
        # Tests to see if student make Dean's List or Honor Roll and prints result
        if studentGPA >= 3.5:
            print(firstName, lastName, "has made the Dean's List.")
        elif studentGPA >= 3.25:
            print(firstName, lastName, "has made the Honor Roll.")

