# Merge two arrays into a single sorted array
a=[3,4,1,5,2]
b=[8,6,9,7,10]
merge=a+b
for i in range (len(merge)):
    for j in range (i+1,len(merge)):
        if merge[i]>merge[j]:
            temp=merge[j]        
            merge[j]=merge[i]
            merge[i]=temp                 
print(merge)