#created by Sarbjeet kaur brar
import classes
import os


def main():
    print()
    option = numcheck()

    while option != 0:
        print()
        patient_list = []
        # Display patient 
        if option == 1:
            readPatientFile(patient_list)
          
            print()
            option = numcheck()
        # search for patient with 
        elif option == 2:
            ID = int(input("Enter the Patient ID:"))
            searchPatientById(ID)
            print()
            option = numcheck()
        #  add patient
        elif option == 3:
            enterPatientInfo()
            print()
            option = numcheck()
        # edit patient info
        elif option == 4:
            id=editPatientList()
            enterNewPatientInfo(id)
            readPatientFile(patient_list)
            print()
            
            option=numcheck()
        else:
            print(" Invalid Option , Enter Number 0 to 4")
            option = numcheck()
           


# display a list or records
def displayPatientList(p_list):
    for patient in p_list:
        print(patient)


# add patient to patient list

def enterPatientInfo():
    p_list=[]
    patient = classes.Patient()
    patient.set_ID(input("Enter Patient ID :"))
    patient.set_Name(input("Enter  Patient name: ").title())
    patient.set_Diagnosis(input("Enter Patient Diagnosos: ").title())
    patient.set_Gender(input("Enter Patient gender: ").title())
    patient.set_Age(input("Enter Patient age: "))
    p_list.append(patient)
    addPatientToList(p_list)
    return (p_list)

# add patient 
def addPatientToList(p_list):
    writePatientListtoFile(p_list)

#read file
def readPatientFile(p_list):
    p_file = open("patients.txt", "r")
    for p_line in p_file:
        p_items = p_line.rstrip().split("_")
        patient = classes.Patient(
            p_items[0], p_items[1], p_items[2], p_items[3], p_items[4])
        p_list.append(patient)
    displayPatientList(p_list)

    p_file.close()


# Patient Menu
def patientmenu():
    option = int(input("Patient Menu\n0{:>4s}  Return to Main Menu\n1{:>4s}  Display patient list\n2{:>4s}  Search for Patient by ID\n3{:>4s}  Add Patient\n4{:>4s}  Edit Patient info\nEnter option :".format(
        "-", "-", "-", "-", "-")))
    return option

# check for user valid input for option if user enter invalid option prompt to enter valid option give error massage also
def numcheck():
    try:
        option = patientmenu()
        if type(option) == int:
            return option

    except ValueError:
        print(" Wrong option Please Enter valid Number 0 to 4:")
        option = numcheck()
        return option


# search List of the Patient objects for the specific Id


def searchPatientById(ID):
    p_list=[]
    p_file = open("patients.txt", "r")
    for p_line in p_file:
        p_items = p_line.rstrip().split("_")
        if str(ID) in p_items[0]:
            patient = classes.Patient(
                p_items[0], p_items[1], p_items[2], p_items[3], p_items[4])
            p_list.append(patient)
            displayPatientList(p_list)
            return (p_list)


    p_file.close()
    if p_list == []:
        print("Patient with ID {} not in patient file".format(ID))
        return p_list


# write patient record to patient.txt file
def writePatientListtoFile(p_list):
    p_file = open("patients.txt", "a")
    for p_items in p_list:

        p_file.write(p_items.formatPatientInfo())
      
    p_file.close()

#  ask user to enter new info of patient to edit in file 
def enterNewPatientInfo(ID):
    new_list = []
    patient = classes.Patient()
    patient.set_ID(ID)

    patient.set_Name(input("Enter new Patient name:").title())
    patient.set_Diagnosis(input("Enter new Patient Diagnosos:").title())
    patient.set_Gender(input("Enter new  gender:").title())
    patient.set_Age(input("Enter  new age:"))
    new_list.append(patient)
    temp_file = open("temppatients.txt", "a")
    for p_items in new_list:
        temp_file.write(p_items.formatPatientInfo())

    temp_file.close()

    os.remove("patients.txt")
    os.rename("temppatients.txt", "patients.txt")


# for editing logic
def editPatientList():
    p_list=[]
    while p_list ==[]:
        ID = int(input("Enter the Patient ID: "))
        p_list=searchPatientById(ID)
    else:
        p_file = open("patients.txt", "r")
        temp_file = open("temppatients.txt", "w")
        for p_line in p_file:
            p_items = p_line.rstrip().split("_")
            patient = classes.Patient(p_items[0],p_items[1],p_items[2],p_items[3],p_items[4])
            if (patient.get_ID() ==str(ID)):
                pass
            
            else:
                temp_file.write(patient.formatPatientInfo())
        p_file.close()
        temp_file.close()
        return(ID)
    


if __name__ == '__main__':
    main()
