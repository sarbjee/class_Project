#created by Sarbjeet kaur Brar 

#  class for patients
class Patient:

    def __init__(self, ID=0, Name="", Diagnosis="", Gender="", Age=0):
        self.__ID = ID
        self.__Name = Name
        self.__Diagnosis = Diagnosis
        self.__Gender = Gender
        self.__Age = Age

    def set_ID(self, ID):
        self.__ID = ID

    def set_Name(self, Name):
        self.__Name = Name

    def set_Diagnosis(self, Diagnosis):
        self.__Diagnosis = Diagnosis

    def set_Gender(self, Gender):
        self.__Gender = Gender

    def set_Age(self, Age):
        self.__Age = Age

    def get_ID(self):
        return self.__ID

    def get_Name(self):
        return self.__Name

    def get_Diagnosis(self):
        return self.__Diagnosis

    def get_Gender(self):
        return self.__Gender

    def get_Age(self):
        return self.__Age

    def __str__(self):
        result = f"{self.__ID:<8s}{self.__Name:<20s}{self.__Diagnosis:<20s}{self.__Gender:<20s}{self.__Age:<20s}"
        return result

    def formatPatientInfo(self):
        formatted = f'{self.__ID}_{self.__Name}_{self.__Diagnosis}_{self.__Gender}_{self.__Age}\n'
        return formatted

# class for doctors
class Doctor:
    def __init__(self, ID=0, Name="", Specialty="", Schedule="", Qualifications="", Roomnumber=""):
        self.__ID=ID 
        self.__Name=Name 
        self.__Specialty = Specialty
        self.__Schedule = Schedule 
        self.__Qualifications = Qualifications
        self.__Roomnumber = Roomnumber
      
    def set_ID(self, ID):
            self.__ID = ID

    def get_ID(self):
        return self.__ID

    def get_Name(self):
        return self.__Name

    def set_Name(self, Name):
        self.__Name = Name

    def set_Specialty(self, Specialty):
        self.__Specialty = Specialty

    def get_Specialty(self):
        return self.__Specialty

    def set_Schedule(self, Schedule):
        self.__Schedule = Schedule

    def get_Schedule(self):
        return self.__Schedule

    def set_Qualifications(self, Qualifications):
        self.__Qualifications = Qualifications

    def get_Qualifications(self):
        return self.__Qualifications

    def set_Roomnumber(self, Roomnumber):
        self.__Roomnumber = Roomnumber

    def get_Roomnumber(self):
        return self.__Roomnumber

    def __str__(self):
        return f'{self.__ID :<10s}{self.__Name : <20s}{self.__Specialty : <20s}{self.__Schedule : <20s}{self.__Qualifications: <20s}{self.__Roomnumber:<20s}'

    def formatDoctorInfo(self):
        formatted = f'{self.__ID}_{self.__Name}_{self.__Specialty}_{self.__Schedule}_{self.__Qualifications}_{self.__Roomnumber}\n'
        return formatted

# class for facility
class Facility:
    def __init__(self,FacilityName=""):
        self.__FacilityName = FacilityName

    def set_FacilityName(self, FacilityName):
        self.__FacilityName = FacilityName

    def get_FacilityName(self):
        return self.__FacilityName
    def __str__(self):
        return f'{self.__FacilityName}'

    def formatFacilityInfo(self):
        formatted = f'{self.__FacilityName}\n'
        return formatted

#  class for Laboratory
class Laboratory:
    def __init__(self,LabName="", Cost=0):
        self.__LabName = LabName
        self.__Cost = Cost

    def set_LabName(self,LabName):
        self.__LabName =LabName

    def get_LabName(self):
        return self.__LabName
    def set_Cost(self,Cost):
        self.__Cost=Cost
    def get_Cost(self):
        return self.__Cost


    def __str__(self):
        return f'{self.__LabName : <20s}{self.__Cost: >20s}'

    def formatLaboratoryInfo(self):
        formatted = f'{self.__LabName}_{self.__Cost}\n'
        return formatted
