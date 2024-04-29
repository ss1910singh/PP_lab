# calculate sum and average of list

list = [1,2,3,4,5]

sum = 0
for i in list:
    sum = sum + i
avg = sum/len(list)
print("Sum: ", sum)
print("Average: ", avg)
