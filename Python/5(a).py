a = input("Enter string:")

count = 0
r = {}

for i in a:
    if i in r:
        r[i] +=1
    else:
        r[i] = 1

print(r)
        
