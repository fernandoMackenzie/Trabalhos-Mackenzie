mat = []
n = int(input("Digite o número de linhas da matriz: "))
m = int(input("Digite o número de colunas da matriz: "))
maior = -1
for i in range(n):
    linha = []
    for j in range(m):
        num = int(input("Digite um número para a matriz: "))
        if num > maior:
            maior = num
        linha.append(num)
    mat.append(linha)

print("Matriz principal: ")
for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print("\n")

print("Maior número da matriz: ",maior)
