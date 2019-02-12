def verifica(n):
    i = 0
    for x in range(1,n):
        div = n%x
        if div == 0:
            i += x
    if i == n:
        return True
    else:
        return False

n = int(input("N = "))
resp = verifica(n)
print(resp)
