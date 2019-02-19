def criar_mat(n):
    mat = []
    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input("Digite um número para a matriz: "))
            linha.append(valor)
        mat.append(linha)
    return mat

def traco_mat(mat,n):
    soma = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                soma += mat[i][j]
    return soma
            
            
n = int(input("Digite o número de linhas e colunas da matriz quadrada: "))
mat = criar_mat(n)
result = traco_mat(mat,n)
print("Matriz: ")
for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print("\n")
        
print("\nTraço da matriz = ",result)
