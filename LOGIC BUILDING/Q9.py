# Today's Question: Remove elements smaller than a given value.
# inp: lis=[5,8,3,2,9,7] val=4
# out: [5,8,9,7]
a=[5,8,3,2,9,7]
val=4
result=[]
for i in a:
    if i > val:
        result.append(i)
print(result)
