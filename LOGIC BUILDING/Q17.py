#  Find common elements between three arrays.
first = [8,3,7,1]
second = [9,2,7,8]
third = [9,7,8,2]
# out: [8,7]
temp=[]
for i in first:
    if i in second and i in third:
        temp.append(i)
print(temp)