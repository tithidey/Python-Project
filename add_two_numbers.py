l1 = [2,4,3]
l1.reverse()

new_l1 = int(''.join(map(str, l1)))

l2 = [5,6,4]
l2.reverse()

new_l2 = int(''.join(map(str, l2)))


sum = new_l1 + new_l2

final_list = [int(digit) for digit in str(sum)]

final_list.reverse()
print(final_list)



