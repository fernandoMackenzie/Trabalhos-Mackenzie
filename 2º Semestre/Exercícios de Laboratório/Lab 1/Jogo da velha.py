def gerar_mat():
    mat = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(".")
        mat.append(linha)
    return mat

def print_mat(mat):
    for i in range(3):
        for j in range(3):
            print(mat[i][j], end=" ")
        print("\n")

def jogar(mat):
    a = int(input("Digite a linha da sua jogada: "))
    while a<0 or a>3:
        a = int(input("Valor inválido!!\n\nDigite a linha da sua jogada: "))
    b = int(input("Digite a coluna da sua jogada: "))
    while b<0 or b>3:
        b = int(input("Valor inválido!!\n\nDigite a coluna da sua jogada: "))
    if mat[a][b] != ".":
        return False
    else:
        mat[a][b] = "X"
        return True
    
    
def jogar_2(mat):
    a = int(input("Digite a linha da sua jogada: "))
    while a<0 or a>3:
        a = int(input("Valor inválido!!\n\nDigite a linha da sua jogada: "))
    b = int(input("Digite a coluna da sua jogada: "))
    while b<0 or b>3:
        b = int(input("Valor inválido!!\n\nDigite a coluna da sua jogada: "))
    if mat[a][b] != ".":
        return False
    else:
        mat[a][b] = "O"
        return True
    
def verifica(mat):
    for x in range(3):
        if mat[x][0] == mat[x][1] and mat[x][1] == mat[x][2]:
            if mat[x][0] != ".":
                return True
        elif mat[0][x] == mat[1][x] and mat[1][x] == mat[2][x]:
            if mat[0][x] != ".":
                return True 
        else:
            return False
    
    
grid = gerar_mat()
print_mat(grid)
ver = False
while ver == False:
    print("Jogador 1: ")
    a = jogar(grid)
    while a == False:
        print("Jogada inválida, tente novamente.")
        a = jogar(grid)
    print("\n\n")
    print_mat(grid)
    ver = verifica(grid)
    print("Jogador 2: ")
    b = jogar_2(grid)
    while b == False:
        print("Jogada inválida, tente novamente.")
        b = jogar_2(grid)
    print("\n\n")
    print_mat(grid)

print("\n\nFim de jogo")
        
    
