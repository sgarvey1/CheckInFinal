import ClassManager
while True:
    print("What would you like to do?")
    print("Add Class (AD) | Remove Class (RC) | Add Student to Class (AS) | Delete Student from Class (DS) | Check-in Class (CC) | Display Class (DC)")
    function = input("Type in letters for one of the above functions:")
    if function == "AD":
        ClassManager.createClass()
    if function == "RC":
        ClassManager.removeClass()
    if function == "AS":
        ClassManager.addStudent()
    if function == "DS":
        ClassManager.deleteName(input("Which class would you like to delete a student from?"))
    if function == "CC":
        ClassManager.classCheckin()
    if function == "DC":
        print("Would you like to display class attendence(A) or class roster(R)?")
        DisplayFile = input("Type the letter of the option you choose:")
        if DisplayFile == "A":
            ClassManager.DisplayAttendence(input("Which class do you want to view?"))
        if DisplayFile == "R":
            ClassManager.DisplayRoster(input("Which class do you want to view?"))
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
        print("-"*os.get_terminal_size().columns )
        print("\n")