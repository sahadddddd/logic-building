# find the last occurance of a charaacter and return its index 
# inp sentence="hello world",k="l"
# out:9
word="hello world"
k="l"
index=0
for i in range(len(word)):
    if word[i]==k:
        index=i
print(index)
        

