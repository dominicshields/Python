def seq3np1(n):
    if n > 0:
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:        # n is even
                n = n // 2
            else:                 # n is odd
                n = n * 3 + 1
        return count

highscore = 0    
for inputnum in range(10000):
    steps = seq3np1(inputnum)
    if steps > highscore:
        highscore = steps
        highnum = inputnum
    
print("Number",highnum,"took",highscore,"steps to get to 1")