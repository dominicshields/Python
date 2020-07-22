def print_triangular_numbers(n):
    a = 0
    x = 1
    while x < n:
        a = a + x
        x += 1
        print(x-1,a)
        
print_triangular_numbers(25)