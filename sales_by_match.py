def matching_items(n, arr):
    #declaring empty list 
    new_arr = list()
    #declaring match value
    match = 0
    
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
        else:
            match += 1
            new_arr.remove(i)
    return match



n = int(input("How many cases? "))
arr = list(map(int, input("items in the arr").split()))[:n]

result = matching_items(n, arr)
print(result)