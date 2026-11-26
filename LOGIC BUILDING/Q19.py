# Second Question: Reverse the last k elements of an array
# inp: lis = [1, 2, 3, 4, 5, 6], k = 3
# out: [1, 2, 3, 6, 5, 4]
lis=list(map(int,input("enter the number with spaces:").split()))
k=int(input("Enter the k:"))
lis[k:]=lis[k:][::-1]
print(lis)