#this is a real world model based on a school enviroment showing varios oop aspects
#such as inheritance,constructors,usage of self,encapsulation and polymorphism
class Student_Sheet(object):
    def fee_balance(self,balance):
        pass
    def marks(self,pass_marks):
        pass
class Student(Student_Sheet): #this showcases inheritance because this class is build upon the parent class Student_Sheet
    def __init__(self):#constructor
        self.pass_marks=250 # public encapsulation here is because this minimum marks /
                                #cannot be set from outside except with special methods
    def marks(self,pass_marks):
        if self.marks >pass_marks:
            print("Student has passed exam")
        elif self.marks<pass_marks:
            print ("Student has failed to reach pass mark mark")
class Fees(Student_Sheet): #multiple inheritance
    def __init__(self):
        self.balance=0   #polymorphism where we declare the variable dont need to continously declare but cn just refer to it
                        #example balance=0 is represented by self.balance
    def fee_statement(self,balance):
        if self.balance>self.balance:
            print ("Fees not fully paid")
        elif self.balance<self.balance:
            print ("fees in advance")
        else:
            print ("fees fully paid")
