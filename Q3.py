# find the second largest in a list
a=[5,8,3,9,2,10]
maximum=0
secon=0
for i in a:
    if i>maximum:
        maximum=i
for i in a:
    if i<maximum and i>secon:
     secon=i
print("second largest:",secon)