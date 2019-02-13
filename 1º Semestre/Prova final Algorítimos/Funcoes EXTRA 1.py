def ePrimo():
    n = int(input("Digite um número: "))
    div = 0
    for x in range(n,0,-1):
        teste = n%x
        if teste == 0:
            div +=1
    if div > 2:
        return False
    else:
        return True

def main():
    num = ePrimo()
    if num == True:
        print("Número primo!")
    else:
        print("Número não é primo!")

main()
