def exibeMsg():
    print("Esse programa converte uma faixa de temperatura entre Celsius e Farenheit.\n\nPara converter Celsius - Farenheit digite 'c' \n\nPara converter Farenheit - Celsius digite 'f' ")

def verificaOpcao():
    escolha = input("Escolha sua conversão: ")
    while escolha.upper() != "C" and escolha.upper() != "F":
        escolha = input("Escolha inválida...\n\nEscolha novamente: ")
    return escolha
def exibeFahrenheitTOCelsius(inicio, fim):
    for x in range(inicio,fim+1):
        c = (x-32)/1.8
        print("ºF: ",x," ºC: ",c)

def exibeCelsiusToFahrenheit(inicio, fim):
    for x in range(inicio,fim+1):
        f = x*1.8 +32
        print("ºC: ",x," ºF: ",f)
def main():
    exibeMsg()
    escolha = verificaOpcao()
    if escolha.upper() == "C":
        inicio = int(input("Temperatura de inicio: "))
        fim = int(input("Temperatura final: "))
        exibeCelsiusToFahrenheit(inicio, fim)
    else:
        inicio = int(input("Temperatura de inicio: "))
        fim = int(input("Temperatura final: "))
        exibeFahrenheitTOCelsius(inicio, fim)

main()
        
        
        
