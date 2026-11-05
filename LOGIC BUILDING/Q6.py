# Today's Ques: Find the most frequent element.
# Inp: [10,7,4,8,9,4,7,7,10,1,7,1]
# Out: 7

# a=[10,7,4,8,9,4,7,7,10,1,7,1]
# max_count=0
# freq_count=0
# for i in a:
#     count=0
#     for j in a:
#         if i ==j:
#             count+=1
#     if count>max_count:
#         max_count=count
#         freq_count=i
# print(freq_count)


a=[10,7,4,8,9,4,7,7,10,1,7,1]
frequent={}
max_count=0
for i in a:
    if i in frequent:
        frequent[i]+=1
    else:
        frequent[i]=1
    if frequent[i]>max_count:
        max_count=frequent[i]
        most_frequent=i
print(most_frequent)
