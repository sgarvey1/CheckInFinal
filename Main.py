import ClassManagerFunctions
import os

while True:
    print("What would you like to do?")
    print("Add Class (AC) | Remove Class (RC) | Add Student to Class (AS) | Delete Student from Class (DS) | Check-in Class (CC) | Display Class (DC)")
    function = input("Type in letters for one of the above functions: ")
    if function == "AC":
        ClassManagerFunctions.createClass()
    elif function == "RC":
        ClassManagerFunctions.removeClass()
    elif function == "AS":
        ClassManagerFunctions.addStudent()
    elif function == "DS":
        ClassManagerFunctions.deleteName(input("Type name of class you wish to delete student from: "))
    elif function == "CC":
        ClassManagerFunctions.classCheckin()
    elif function == "DC":
        print("Would you like to display class attendence(A) or class roster(R)?")
        DisplayFile = input("Type the letter of the option you choose: ")
        if DisplayFile == "A":
            ClassManagerFunctions.DisplayAttendence(input("Type name of class you wish to view: "))
        if DisplayFile == "R":
            ClassManagerFunctions.DisplayRoster(input("Type name of class you wish to view: "))
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
        print("-"*os.get_terminal_size().columns )
        print("\n")