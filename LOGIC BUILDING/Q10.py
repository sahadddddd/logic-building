# Check if a given list contains only numbers.
# Inp: ["7", "0", "python", "6", "sql"]
# out: False
# Inp: ["7", "5", "2", "8"]
# out: True
a=["7", "0", "python", "6", "sql"]
check=0
for i in a:
    if i.isdigit():
        check=True
    else:
        check=False
        break
print(check)
