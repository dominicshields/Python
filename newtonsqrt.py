def mySqrt(n):
  oldguess = n/2
  for i in range(30):
        newguess = (1/2) * (oldguess + (n/oldguess))
        if oldguess == newguess:
            break
        oldguess = newguess
        
  return newguess

print(mySqrt(1048576))