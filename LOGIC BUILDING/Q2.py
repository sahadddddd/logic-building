# Find the difference between the largest and smallest elements.
# inp : [5,8,3,9,2,10]
# out : 8
# a = list(map(int, input("Enter numbers separated by spaces: ").split()))
a=[5,8,3,9,2,10]
maximum=0
for i in a:
    if i >maximum:
        maximum=i
print(maximum)
minimum=maximum
for i in a:
    if i <minimum:
        minimum=i
print(minimum)
print("The difference:",maximum-minimum)