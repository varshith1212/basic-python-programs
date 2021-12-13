str1 = input("Enter date of birth:")

sp = str1.split(".")

bday='/'.join(sp)

d1={"birthday":bday}

print(d1)
