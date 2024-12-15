testCase = int(input("How many test cases you require: "))
arr = []

# adding values to array
while testCase > 0:
    i = int(input("Give values: "))
    arr.append(i)
    testCase -= 1
print(arr)


#removing values from arr
for i in arr:
    if i > 10:
        arr.remove(i)

print(arr)