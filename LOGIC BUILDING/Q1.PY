# Q Swap the first and last element of an array
# inp : nums = [4,8,2,6,7]
# out : [7,8,2,6,4]
nums=[4,8,2,6,7]
a=nums.pop(0)
b=nums.pop(-1)
nums.append(a)
nums.reverse()
nums.append(b)
nums.reverse()
print(nums)
