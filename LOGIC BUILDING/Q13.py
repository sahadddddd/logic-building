# Today's Question: Sort an array without using built-in function.
# inp: [4,9,6,1,2,0,1,4,5,3]
# out: [0,1,1,2,3,4,4,5,6,9]
a=[4,9,6,1,2,0,1,4,5,3]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
            
print(a)
            