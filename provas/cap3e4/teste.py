def facto(n):
    if n == 0:
        return 1
    else:
        fatorial = facto(n-1)
    return n * fatorial
