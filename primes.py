import datetime
import time
start_time = time.time()
print ("Starts ",datetime.datetime.now().time())
f = open('primes.txt', 'w')
count = 0
def IsPrime(TestPrime):
    if (TestPrime == 2) or (TestPrime == 3) or (TestPrime == 5):
        return TestPrime
    elif (TestPrime % 2) == 0 or (TestPrime % 5) == 0 or (TestPrime == 1):
        return "No"
    else:
        TestNum = 3
        TestLimit = TestPrime
        while TestLimit > TestNum:
            if TestPrime % TestNum == 0:
#               f.write(str(TestPrime))
#               f.write(" divisible by ")
#               f.write(str(TestNum))
#               f.write('\n')
               return "No"
            else:
#                f.write("Testnum = ")
#                f.write(str(TestNum))
#                f.write('\n')
                TestLimit = TestPrime / TestNum
                TestNum = TestNum + 2
    return TestPrime
for x in range (1,99999):
    ans = str(IsPrime(x))
    if ans != 'No':
        f.write(ans)
        f.write('\n')
        count = count + 1
f.close()
print("Ends   ",datetime.datetime.now().time())
print("Wrote  ",count)
print("Took    %s seconds" % (time.time() - start_time))
