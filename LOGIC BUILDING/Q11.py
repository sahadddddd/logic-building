# Today's Question: Find two numbers that have the smallest absolute difference.
# inp: [4,9,6,1]
# out: [4,6]
nums= [4,9,6,1]
min_diff=abs(nums[1]-nums[0])
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        diff=abs(nums[i]-nums[j])
        if diff<min_diff:
            min_diff=diff
            result=[nums[i],nums[j]]
print(result)
