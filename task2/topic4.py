
def add(a, b):
    return a + b
result=add(4, 5)

print("Sum:", result)
#open & read
f = open('topic1.py')
content = f.read()
print(content)
f.close()
# write
f=open('topic1.py','w')
f.write("Python is more important")
f.close()

# # with
# with open('topic2.py', 'w') as f:
#     f.write("Python is important")












