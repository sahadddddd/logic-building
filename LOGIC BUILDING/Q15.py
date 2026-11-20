# Remove elements that appear an odd number of times
a = list(map(int, input("Enter numbers separated by spaces: ").split()))
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
for i in count:
    if count[i]%2!=0:
        # a=[x for x in a if x!=i]  
        while i in a:
             a.remove(i)
print(a)      



