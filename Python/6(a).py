t1 = ["name","clg","age"]
t2 = [34,"abc","mrec"]

res = {}

for key in t1:
    for value in t2:
        res[key] = value
        t2.remove(value)
        break
    
print(res) 
