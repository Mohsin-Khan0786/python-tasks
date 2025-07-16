x = 10  # Global variable

def show():
    x = 5  # Local variable
    print("Inside function x:", x)

show()
print("Outside function x:", x)
#local varriable
def outer():
    x = 10

    def inner():
        nonlocal x   
        x = 20
        print("Inner function:", x)

    inner()
    print("Outer function:", x)

outer()