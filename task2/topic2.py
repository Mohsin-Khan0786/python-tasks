#loops
# For loop
for i in range(5):
    print("For loop value:", i)
#continue
for i in range(5):
    if i == 3:
        continue
    print("For loop value:", i)

# While loop
count = 0
while count < 5:
    if count == 3:
        break
    print("While loop count:", count)
    # count += 1