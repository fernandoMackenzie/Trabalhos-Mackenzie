def entrada():
    num = int(input("Digite um número: "))
    return num

def verifica(a):
    if a>0:
        return print("P")
    else:
        return print("N")

def main():
    num = entrada()
    verifica(num)
    

main()
    
