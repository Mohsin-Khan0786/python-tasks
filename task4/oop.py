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

    # contsructer instance nethod
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

     

