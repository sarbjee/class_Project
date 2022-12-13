# created by sarbjeet kaur brar
import classes
def main():
    option = numcheck()
    Laboratory_list=[]
    while option !=0:
        print()
        # display lab list
        if option == 1:
            readLaboratoryiesFile()
            # displayLabList(Laboratory_list)
            option = numcheck()
        # add lab 
        elif option == 2:
            enterLaboratoryInfo(Laboratory_list)
            option = numcheck()
        else:
            print(" Invalid Option , Enter Number 0 to 2")
            option=numcheck()
        

#  display list 
def displayLabList(l_list):
    for lab in l_list:
        print(lab)


# read records from laboratories file
def readLaboratoryiesFile():
    l_list=[]
    l_file = open("laboratories.txt", "r")
    for l_line in l_file:
        l_items = l_line.rstrip().split("_")
        laboratry = classes.Laboratory(
            l_items[0], l_items[1])
        l_list.append(laboratry)
    displayLabList(l_list)
    l_file.close()

#  write entered list to laboratories.txt file
def writeLabsListToFile(l_list):
    l_file = open("laboratories.txt", "a")
    for l_items in l_list:
        l_file.write(l_items.formatLaboratoryInfo())
    l_file.close()

#  enter Lab information to add in list
def enterLaboratoryInfo(l_list):
    laboratory=classes.Laboratory()
    laboratory.set_LabName(input("Enter Lab Name: "))
    laboratory.set_Cost(input("Enter Lab Cost:"))
    l_list.append(laboratory)
    writeLabsListToFile(l_list)
    
    
#  Laboratory menu

def laboratorymenu():
    print()
    option = int(input(
        "Laboratory Menu \n0{:>4s}  Return to Main Menu\n1{:>4s}  Display Laboratory list\n2{:>4s}  Add Laboratory \nEnter Option :".format("-", "-", "-")))
    return option

# check for user valid input for option if user enter invalid option prompt to enter valid option give error massage also

def numcheck():
    try:
        option = laboratorymenu()
        if type(option) == int:
            return option

    except ValueError:
        print(" Wrong option Please Enter valid Number 0 to 2:")
        option = numcheck()
        return option


if __name__ == "__main__":
   
    main()
