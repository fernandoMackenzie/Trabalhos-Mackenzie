def entrada():
    custo = float(input())
    return custo
def somaImposto(porc,custo):
    corrigido = custo+custo*(porc/100)
    return corrigido

def main():
    print("Digite o custo do produto: ")
    custo = entrada()
    print("Digite o valor do imposto em porcentagem: ")
    porc = entrada()
    novo_custo = somaImposto(porc,custo)
    print("Valor corrigido = ", novo_custo)

main()
