# number to find summation of all primes below number
hi = 2000000

# create a set excluding even numbers
numbers = set(xrange(3, hi + 1, 2)) 

for number in xrange(3, int(hi ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    num = number
    while num < hi:
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print (2 + sum(numbers))

"""
sum = 0

def prime(i):
    count = 0
    for j in range(1,i**0.5):
        if i/j == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False
    
for i in range(1,2000000):
    x = prime(i)
    if x == True:
        sum += i
    else:
        break

print "The sum is:" +sum
"""

