mat =[]
num_linha = int(input("Digite o número de linhas da matriz: "))
num_coluna = int(input("Digite o numero de colunas: "))
for i in range(num_linha):
    linha=[]
    for j in range(num_coluna):
        num = int(input("Digite um número para a matriz: "))
        linha.append(num)
    mat.append(linha)

for x in range(num_linha):
    for y in range(num_coluna):
        print(mat[x][y], end =" ")
    print("\n")
    
