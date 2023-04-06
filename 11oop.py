# WAP to store student info using class concept

# student class 
class student:
    # constructor for passing student info
    def __init__(self,name,rollno,adno,marks):
        self.name = name
        self.rollno = rollno
        self.adno = adno
        self.marks = marks

    # method to print details
    def printDetail(self):
        print(f"Name : {self.name}\nRoll no. : {self.rollno}\nAdmission no. : {self.adno}\nMarks : {self.marks}\n")
    
# object creation and method call for print student info
Std1 = student("Suraj",17510,"2117510",(7,8,8,9))
Std1.printDetail()
Std2 = student("Lakshay",17536,"2117536",(8,8,8,9))
Std2.printDetail()
Std3 = student("Priyanshu",17525,"2117525",(8,8,9,9))
Std3.printDetail()