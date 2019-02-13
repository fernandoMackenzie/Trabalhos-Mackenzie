v = []
def ler(v):
    for x in range(10):
        num = int(input("Digite um número: "))
        v.append(num)

ler(v)
v.reverse()
print(v)
