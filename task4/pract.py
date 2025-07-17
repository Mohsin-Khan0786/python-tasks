
# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b
# list comprension

numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]

print(squares)  


# dict comprension

squares_dict = {x: x*x for x in numbers}

print(squares_dict)

# set comprehensions
nums = [1, 2, 2, 3, 4, 4, 5]

unique_squares = {x*x for x in nums}

print(unique_squares)