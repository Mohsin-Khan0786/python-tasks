nums=[2,3,4,5,6,7,8,9,15,14]
my_num=list(filter(lambda x:x%2==0,nums))
print("These are Even numbs:",my_num)




# decoraters
def log_deco(fun):

    def wrapper():

        print("Before Function calling")
        fun()  

        print("After Function Execition") 

@log_deco
def hello():
    print("Execution completed")

hello()    


