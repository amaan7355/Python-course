class student():
    def __init__(self,name,roll_num):
        self.name=name
        self.roll_num=roll_num
    def result(self,marks,grade):
        self.marks=marks
        self.grade=grade
        print(f"Marks obtained are {self.marks} and Grade obtained is {self.grade}")
    def hostel(self,facility):
        self.facility=facility
        print(f"The Name of the Student is {self.name} and Roll Number of the student is {self.roll_num}. {self.facility}! hostel facility taken.")
fac=input("Enter yes or no whether hostel facility required or not?: ")
amaan=student("Amaan Alam",16)
amaan.result("700/750","A")
amaan.hostel(fac)