# created by sarbjeet kaur brar
import classes
import os


def main():
    option = numcheck()

   
    while option != 0:
        print()
        Doctor_list = []
        # Read all records FROM doctors.txt file and display them
        if option == 1:
            readDoctorFile(Doctor_list)
            print()
            option = numcheck()
        # search  Doctor with ID if exist in file display else gives a massage Doctor not found

        elif option == 2:
            id = int(input("Enter the doctor ID: "))
            searchDoctorById(id)
            print()
            option = numcheck()
        #search  Doctor with NAME if exist in file display else gives a massage Doctor not found
        
        elif option == 3:
            name = input("Enter the doctor name: ").title()
            searchDoctorByName(name)
            option = doctormenu()
        # ADD doctor in list
        elif option == 4:
            enterDrInfo()
            print()
            option = numcheck()
        # edit doctor info 
        elif option == 5:
            ID= editDoctorInfo()
            enterNewInfoForDr(ID)
            readDoctorFile(Doctor_list)
            print()
            option = numcheck()

        else:
            print(" Invalid Option , Enter Number 0 to 5")
            option = numcheck()


# Displays all the Doctors information
def displayDoctorsList(d_list):
    for doctor in d_list:
        print(doctor)

# read doct file
def readDoctorFile(d_list):
    d_file = open("doctors.txt", "r")
    for d_line in d_file:
        d_items = d_line.rstrip().split("_")
        doctor = classes.Doctor(
            d_items[0], d_items[1], d_items[2], d_items[3], d_items[4], d_items[5])
        d_list.append(doctor)
    displayDoctorsList(d_list)
    d_file.close()

# search for particular doctor with ID from doctors.txt file if doctor found display otherwise give massage 
def searchDoctorById(ID):
    d_list = []
    d_file = open("doctors.txt", "r")
    for d_line in d_file:
        d_items = d_line.rstrip().split("_")
        if str(ID) in d_items[0]:
            doctor = classes.Doctor(
                d_items[0], d_items[1], d_items[2], d_items[3], d_items[4], d_items[5])
            d_list.append(doctor)
            displayDoctorsList(d_list)
            return(d_list)
    d_file.close()
    if d_list == []:
        print("Doctor with ID {} not found in Doctors file".format(ID))
        return d_list

# search for particular doctor with NAME from doctors.txt file if doctor found display otherwise give massage
def searchDoctorByName(name):
    d_list = []
    d_file = open("doctors.txt", "r")
    for d_line in d_file:
        d_items = d_line.rstrip().split("_")
        if name in d_items:
            print(name)
            doctor = classes.Doctor(
                d_items[0], d_items[1], d_items[2], d_items[3], d_items[4], d_items[5])
            d_list.append(doctor)
            displayDoctorsList(d_list)

    d_file.close()
    if d_list == []:
        print("Doctor with ID {} not found in Doctors file".format(name))

# enter doctor info for add 
def enterDrInfo():
    d_list = []
    doctor = classes.Doctor()
    doctor.set_ID(input("Enter Dr. ID: "))
    doctor.set_Name(input("Enter Dr name:").title())
    doctor.set_Specialty(input("Enter Dr specialty: ").title())
    doctor.set_Schedule(input("Enter Dr schedule: "))
    doctor.set_Qualifications(input("Enter Dr qualifications: ").upper())
    doctor.set_Roomnumber(input("Enter Dr room number: "))
    d_list.append(doctor)
    addDrToList(d_list)
    return (d_list)

# add entered doctor 
def addDrToList(d_list):
    writeDoctorListToFile(d_list)

# write doctor list entered to doctors.txt file 
def writeDoctorListToFile(d_list):
    d_file = open("doctors.txt", "a")
    for d_items in d_list:
        d_file.write(d_items.formatDoctorInfo())
    d_file.close()

# enter new info of doctor for editing that is already exist in file
def enterNewInfoForDr(ID):
    new_list = []
    doctor = classes.Doctor()
    doctor.set_ID(ID)

    doctor.set_Name(input("Enter new name:").title())
    doctor.set_Specialty(input("Enter new specialty: ").title())
    doctor.set_Schedule(input("Enter new schedule: "))
    doctor.set_Qualifications(input("Enter new qualifications: ").upper())
    doctor.set_Roomnumber(input("Enter new room number: "))
    new_list.append(doctor)
    temp_file = open("tempdoctors.txt", "a")
    for d_items in new_list:
        temp_file.write(d_items.formatDoctorInfo())

    temp_file.close()

    os.remove("doctors.txt")
    os.rename("tempdoctors.txt", "doctors.txt")

#  works for editing doctor information
def editDoctorInfo():
    d_list=[]
  
    while  d_list == []:
        ID = int(input("Enter the Doctor ID: "))
        d_list = searchDoctorById(ID)
    else:
        d_file = open("doctors.txt", "r")
        temp_file = open("tempdoctors.txt", "w")
        for d_line in d_file:
            d_items = d_line.rstrip().split("_")
            doctor = classes.Doctor(
                d_items[0], d_items[1], d_items[2], d_items[3], d_items[4], d_items[5])
            if (doctor.get_ID() == str(ID)):
                pass

            else:
                temp_file.write(doctor.formatDoctorInfo())
        d_file.close()
        temp_file.close()
        return(ID)

  

    

#  doctor menu 
def doctormenu():
    print()
    option = int(input(
        "Doctor 's Menu \n0{:>4s}  Return to Main Menu\n1{:>4s}  Display Doctor List\n2{:>4s}  Search for Doctor ID\n3{:>4s}  Search for Doctor by name\n4{:>4s}  Add Doctor\n5{:>4s}  Edit doctor info\nEnter Option :".format("-", "-", "-", "-", "-", "_")))
    return option

#  check for user valid input for option if user enter invalid option prompt to enter valid option give error massage also
def numcheck():
    try:
        option = doctormenu()
        if type(option) == int:
            return option

    except ValueError:
        print("Wrong option Please Enter valid Number 0 to 2:")
        option = numcheck()
        return option


if __name__ == "__main__":
    main()
