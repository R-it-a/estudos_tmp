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


def t(number_1, number_2):
    for i in range(number_2 + 1):
        count = number_1 * i
        print(f"{number_1} x {i} = {count}")

t(9, 11)
