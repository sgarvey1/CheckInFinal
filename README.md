# CheckInFinal

## Description
This check-in system uses an rfid reader that inputs data like a keyboard. The rfid reader should be set to automaticaly hit enter after typing in data.  Data about attendence and class roster is stored in txt files. 

When students are added, a name and ID vlaue from their access card are inserted into a Roster file. This file is referred back to during check-in. After check-in, an Attendence file is created or updated to include the names of people who are present. When attendence is displayed, these files are compared to determine who is absent and who is present.

When running on a Raspberry Pi, the program must be run with admin priveledges or the program will fail to create and open files. In addition, the Check-In and Add Student function must be run locally through the Pi's terminal. This is because the rfid reader sends data as a keyboard input. The other functions can be used either locally or remotely through ssh.


## Features
- Ability to add and delete classes
- Ability to add and remove students from classes
- Ability to check-in students
- Ability to display class roster and class attendence

## Useful Links
- https://www.geeksforgeeks.org/python-open-function/
- https://docs.python.org/3/library/functions.html#open