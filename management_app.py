# created by Sarbjeet kaur brar 
import classes
import doctorMenu
import facilityMenu
import laboratoriesMenu
import patientMenu


# Main entry Function


def main():
    option = numcheck()

#  this option prompt to doctor menu and show all options for Doctor
    while option != 0:
        if option == 1:
            doctorMenu.main()
            main()
            break
            
        #    this option prompt to Facility menu and show all options for Facilities
        elif option == 2:
            facilityMenu.main()
            main()
            break
        # this option prompt to Laboratory menu and shows all options for Laboratory 
        elif option == 3:
            laboratoriesMenu.main()
            main()
            break
        # this option prompt to patient menu and shows all options for patient
        elif option == 4:
            patientMenu.main()
            main()
            break
        else:
            print("Invalid Option , Enter Number 0 to 4")
            option=numcheck()
            
# Main Menu for application
def mainMenu():
    print("\nWelcome to the Alberta Rural Patient Care Management System\n")
    print()
    option = int(input(
        "Main Menu \n0{:>4s}  close Application\n1{:>4s}  Doctor\n2{:>4s}  Facilities\n3{:>4s}  Laboratories\n4{:>4s}  Patients\nEnter Option :".format("-", "-", "-", "-", "-")))
    return option

#  check user enter entered valid type of data if used invalid option prompt user to enter right option 
def numcheck():
    try:
        option=mainMenu()
        if type(option)==int:
            return option
         
    except ValueError:
        print(" Wrong option Please Enter valid Number 0 to 4:")
        option=numcheck()
        return option

   
    


if __name__ == "__main__":
   
    main()
