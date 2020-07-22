import math
def is_prime(n):
    x = 2
    while x < math.sqrt(n):
        if n % x == 0:
            return False
        x += 1
    return True

testnum = 773
print("Test number",testnum,"test for prime returned",is_prime(testnum))