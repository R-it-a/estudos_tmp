##(n x n-1 x n-2...)
#def fatorial(n):
#    for i in range(n):
#        fat = (n-i)
#        return fat ** n
#
#print(fatorial(23))
def fatorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    print(factorial)
print(fatorial(23))
