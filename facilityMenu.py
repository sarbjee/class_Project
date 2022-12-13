#created by sarbjeet kaur brar
import classes
def main():
    
    option = numcheck()
    while option!=0:
        print()
        facility_list = []
        
        if option == 1:
            readFacilitiesFile()
            print()
           
            option = numcheck()
        elif option ==2:
            facility=classes.Facility()
            facility.set_FacilityName(input("Enter Facility name:").title())
            facility_list.append(facility)
            addFacilityToList(facility_list)
            option = numcheck()
        else:
            print(" Invalid Option , Enter Number 0 to 2")
            option = numcheck()

# Facility menu
def facilitymenu():
    print()
    option = int(input(
        "Facilities Menu \n0{:>4s}  Return to Main Menu\n1{:>4s}  Display Facilities list\n2{:>4s}  Add Facility\nEnter Option :".format("-", "-", "-")))
    return option


# check for user valid input for option if user enter invalid option prompt to enter valid option give error massage also
def numcheck():
    try:
        option = facilitymenu()
        if type(option) == int:
            return option

    except ValueError:
        print(" Wrong option Please Enter valid Number 0 to 2:")
        option = numcheck()
        return option


# dicplay records
def disFacilitiesList(f_list):
    for facility in f_list:
        print(facility)
# read doct file

#  read facilities.txt file
def readFacilitiesFile():
    f_list=[]
    f_file = open("facilities.txt","r")
    for f_line in f_file:
        f_items = f_line.rstrip()
        facility = classes.Facility(f_items)
        f_list.append(facility)
    disFacilitiesList(f_list)
    f_file.close()
    
    # add facility 
def addFacilityToList(f_list):
    writeFacilitiesListFile(f_list)

# write facility to file

def writeFacilitiesListFile(f_list):
    f_file = open("facilities.txt", "a")
    for f_items in f_list:
        f_file.write(f_items.formatFacilityInfo())
    f_file.close()




if __name__ == "__main__":
    main()
