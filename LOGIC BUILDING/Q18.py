# Question: Calculate the prefix sum of an array.
# inp: [8, 20, 12, 40]
# out: [8, 28, 40, 80]
a=[8,20,12,40]
out=[]
count=0
for i in a:
    count+=i
    out.append(count)
print(out)