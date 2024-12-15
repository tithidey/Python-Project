nums = []

# declaring number of array and taking input
n = int(input("How many items you want in the list: "))

# taking input
for i in range(0,n):
    i = int(input())
    nums.append(i)

# declaring target value
target = int(input('Enter the target value: '))

# checking the condition
for i in range(0,len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
            print(f"[{i},{j}]")
        