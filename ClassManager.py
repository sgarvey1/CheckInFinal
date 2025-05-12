import os
import datetime
now = datetime.datetime.now()

def createClass():
    #Creates txt file for class roster
    className = input("Type name of class you wish to create:")
    file = (className + " Roster")
    if os.path.isfile(file):  #Checks if file exists
        print("Class already exists.")
    else:
        Class = open(className + " Roster", "w")
        Class.close() #Closes the file

def addStudent():
    #Determines class file to access
    Choice = input("Which class would you like to add to?")
    
    file = (Choice + " Roster")
    if os.path.isfile(file):  #Checks if file exists
        Class = open(file, "r+")

        #Writes new student information in file
        name = input("Type Student's Name:")
        ID = input("Scan ID Card")
        Class.writelines([name, ",", ID, ",\n"]) #\n makes program go to next line
        while True:
            repeatFunction = input("Would you like to add another student? [Y/N]")
            if repeatFunction == "N":
                break #Exits loop if "N" is given
            elif repeatFunction == "Y":
                name = input("Type Student's Name:")
                ID = input("Scan ID Card")
                Class.writelines([name, ",", ID, ";\n"])
            else:
                print("Invalid Input")
        Class.close()
    else:
        print("Invalid Input")

def rosterList(className):
    roster = open(className +" Roster", "r") #Opens Class Roster File in reading mode
    lines = roster.readlines()
    Names = []
    for row in lines:
        Names.insert(1, row.rstrip(",1234567890 \n")) #Strips name of ending ID number
    return(Names) #Returns list of names on class roster

def classCheckin():
   #Determines class list which will be searched
    Class = input("Which class do you want to take attendence for?")
    file = (Class + " Roster")
    if os.path.isfile(file):  #Checks if file exists
        CheckIn = open(Class +" Roster", "r+")
        lines = CheckIn.readlines()
        Present = []
        while True:
            ID = input("Please Scan ID Card: ")
            if ID == "exit":
                break
            else:
                for row in lines:
                    if row.find(ID) != -1:
                        presentName = row.rstrip(",1234567890 \n") #Strips ending ID off of text
                        Present.insert(1, presentName)
        CheckIn.close

        #Creates list of all absent students
        absent = rosterList(Class) #Creates list of all students
        for item in Present:
            absent.remove(item) #Removes name from absent if on Present
    else:
        print("Class does not exist.")

    #Creates txt file that store attendence information
    Attendence = open(Class +" Attendence", "w")
    Attendence.write("Present:\n")
    for item in Present:
        Attendence.write(item + "\n")
    Attendence.write("Absent:\n")
    for item in absent:
        Attendence.write(item + "\n")


def DisplayAttendence(AttendenceClass):
    file = (AttendenceClass + " Roster")
    if os.path.isfile(file):  #Checks if file exists
        #Prints Attendence File of specified class
        date_string = now.strftime("%m/%d/%Y")
        print("Attendence for: " + AttendenceClass + " Date: " + date_string)
        display = open(AttendenceClass +" Attendence", "r")
        lines = display.readlines()
        for row in lines:
            print(row)
    else:
        print("Attendence file does not exist.")

def DisplayRoster(RosterClass):
    file = (RosterClass + " Roster")
    if os.path.isfile(file):  #Checks if file exists
        #Prints Roster File of specified class
        print("Roster for: " + RosterClass)
        display = open(RosterClass +" Roster", "r")
        
        lines = display.readlines()
        Names = []
        for row in lines:
            Names.insert(1, row.rstrip(",1234567890 \n")) #Strips name of ending ID number
        for item in Names:
            print(item + ",")
    else:
        print("Attendence file does not exist.")

#def deleteName(file):