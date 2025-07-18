# class faculty:
  
#   def __init__(self):
#     self.id=int(input("Enter the Faculty id:"))
#     self.name=input("Enter the Faculty Name: ")
#     self.salary=int(input("Enter the Faculty Salary:"))
#   def display(self):
#       print("faculty id",self.id)
#       print("faculty name",self.name)
#       print("faculty salary",self.salary)

# a=faculty()  

# a.display()

# # Exception handling
# a=int(input("Enter the Value A:"))
# b=int(input("Enter the Value B:"))
# try:
#   c=a/b
# except:
#    print("Can't Divisible By 0")
# else:
#    print("Result",c)
# finally:
#    print("Execution Completed")  # 



class School:
    # class var
    school_nam = "The Punjab School"

    # contsructer instance method
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    # class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_nam = new_name  

    @staticmethod
    def add(a, b):
        return a + b


S1 = School('Mohsin', 22)

print(S1.school_nam)  

School.change_school("Govt School")

print(S1.school_nam) 

print(S1.add(2,4))

     

class A:

   num1=int(input("Enter the 1st number:"))
   num2=int(input("Enter the 2nd number:"))
   def Add(self):
       
       print("Addition",self.num1 +self.num2)

        
class B(A):
    def Sub(self):
        print("Addition",self.num1 - self.num2)

A1=B()
A1.Add()   
A1.Sub()     

# Multilevel Inheritance

class Father:
    surname = "Ali"
    
    def __init__(self, age):
        self.age = age

class Son(Father):   
    def __init__(self, age):
        super().__init__(age)  
        print("Son Constructor")

    def Show(self):
        print("Mohsin", self.surname)
        print("Age", self.age)

class GrandSon(Son):
    def __init__(self, age):
        super().__init__(age)
        print("GrandSon Constructo")

    def Displ(self):
        print("Abrar", self.surname)
        print("Age", self.age)

S1 = Son(50)
S1.Show()

S2 = GrandSon(20)
S2.Displ()


    

     
     



