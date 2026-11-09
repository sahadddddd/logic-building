# Check if all elements are unique.

# inp: [4,6,2,8,9]
# out: True

# inp: [9,4,3,3,7,7]
# out: False
a=list(map(int,input("enter number seperated with spaces:").split()))
count={}
for i in a:
    if i in count:
        count[i]+=1
        print("false")
        break
    else:
        count[i]=1
else:
    print("True")


