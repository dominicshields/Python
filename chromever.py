import math

def MsiToChrome(X, Y, Z):
  c = ((X & 0x3f) << 10) + (Y << 2) + (Z >> 14)
  d = (Z & 0x3fff)
  return str(c) + "." + str(d)

A = int(input("Enter first part of the chrome version  "))
B = int(input("Enter second part of the chrome version "))
C = int(input("Enter third part of the chrome version "))

print("Version = ",MsiToChrome(A,B,C))
