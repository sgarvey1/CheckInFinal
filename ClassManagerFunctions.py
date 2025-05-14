import os
import datetime
from getpass import getpass
now = datetime.datetime.now()

def createClass():
    #Creates txt file for class roster
    className = input("Type name of class you wish to create: ")
    file = (className + " Roster.txt")
    if os.path.isfile(file):  #Checks if file exists
        print("Class already exists.")
    else:
        Class = open(className + " Roster.txt", "w")
        Class.close() #Closes the file
    print("-"*os.get_terminal_size().columns )
    print("\n")

def addStudent():
    #Determines class file to access
    Choice = input("Type name of class you wish to add to: ")
    
    file = (Choice + " Roster.txt")
    if os.path.isfile(file):  #Checks if file exists
        Class = open(file, "r+")

        #Writes new student information in file
        name = input("Type Student's Name: ")
        ID = getpass("Scan ID Card")
        Class.writelines([name, ",", ID, ",\n"]) #\n makes program go to next line
        while True:
            repeatFunction = input("Would you like to add another student? [Y/N]\n")
            if repeatFunction == "N":
                break #Exits loop if "N" is given
            elif repeatFunction == "Y":
                name = input("Type Student's Name:")
                ID = getpass("Scan ID Card")
                Class.writelines([name, ",", ID, ";\n"])
            else:
                print("Invalid Input")
        Class.close()
    else:
        print("Invalid Input")
    
    print("-"*os.get_terminal_size().columns )
    print("\n")

def rosterList(className):
    roster = open(className +" Roster.txt", "r") #Opens Class Roster File in reading mode
    lines = roster.readlines()
    Names = []
    for row in lines:
        Names.insert(1, row.rstrip(",1234567890 \n")) #Strips name of ending ID number
    return(Names) #Returns list of names on class roster

def classCheckin():
   #Determines class list which will be searched
    Class = input("Type name of class you wish to take attendence for: ")
    file = (Class + " Roster.txt")
    if os.path.isfile(file):  #Checks if file exists
        CheckIn = open(Class +" Roster.txt", "r+")
        lines = CheckIn.readlines()
        Present = []
        while True:
            ID = getpass("Scan ID Card")
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
    Attendence = open(Class +" Attendence.txt", "w")
    Attendence.write("Present:\n")
    for item in Present:
        Attendence.write(item + "\n")
    Attendence.write("Absent:\n")
    for item in absent:
        Attendence.write(item + "\n")
    
    print("-"*os.get_terminal_size().columns )
    print("\n")


def DisplayAttendence(AttendenceClass):
    file = (AttendenceClass + " Roster.txt")
    if os.path.isfile(file):  #Checks if file exists
        #Prints Attendence File of specified class
        date_string = now.strftime("%m/%d/%Y")
        print("Attendence for: " + AttendenceClass + " Date: " + date_string)
        display = open(AttendenceClass +" Attendence.txt", "r")
        lines = display.readlines()
        for row in lines:
            print(row)
    else:
        print("Attendence file does not exist.")
    
    print("-"*os.get_terminal_size().columns)
    print("\n")

def DisplayRoster(RosterClass):
    file = (RosterClass + " Roster.txt")
    if os.path.isfile(file):  #Checks if file exists
        #Prints Roster File of specified class
        print("Roster for: " + RosterClass)
        display = open(RosterClass +" Roster.txt", "r")
        
        lines = display.readlines()
        Names = []
        for row in lines:
            Names.insert(1, row.rstrip(",1234567890 \n")) #Strips name of ending ID number
        for item in Names:
            print(item + ",")
    else:
        print("Attendence file does not exist.")
    
    print("\n")
    print("-"*os.get_terminal_size().columns )

def deleteName(fileName):
    #Opens file in read mode; Stores data from file into lines
    file = open(fileName + " Roster.txt", "r")
    lines = file.readlines()
    file.close()

    #Opens file in write mode(erases file in the process); Adds back names that need to be keeped
    file = open(fileName + " Roster.txt", "w")
    name = input("Type full name of student you wish to delete: ")
    for line in lines: 
        if 0 == line.find(name): #Looks to see if name given is in line; find(name) give value of 0 if text is found
            print("Name Deleted")
        else:
            file.write(line) #Write stored data back into txt file
    
    print("\n")
    print("-"*os.get_terminal_size().columns )
    
def removeClass():
    #Checks if file exist; then, deletes the file
    file = input("Type class you wish to delete: ")
    if os.path.exists(file + " Roster.txt"):
        os.remove(file + " Roster.txt")
        if os.path.exists(file + " Attendence.txt"):
            os.remove(file + " Attendence.txt")
    else:
        print("The file does not exist.")
    
    print("\n")
    print("-"*os.get_terminal_size().columns )

    