def gerar_mat():
    num = 1
    mat = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(num)
            num +=1
        mat.append(linha)
    return mat

def print_mat(mat):
    print("Tabuleiro: \n\n")
    for i in range(3):
        for j in range(3):
            print(mat[i][j], end="  ")
        print("\n")

def jogar(mat):
    a = int(input("Digite a posição da sua jogada: "))
    while a<0 or a>9:
        a = int(input("Valor inválido!!\n\nDigite a posição da sua jogada: "))
    flag = False
    for i in range(3):
        for j in range(3):
            if mat[i][j] == a:
               mat[i][j] = "X"
               flag = True
               return True
    if flag == False:
        return False

def jogar_2(mat):
    a = int(input("Digite a posição da sua jogada: "))
    while a<0 or a>9:
        a = int(input("Valor inválido!!\n\nDigite a posição da sua jogada: "))
    flag = False
    for i in range(3):
        for j in range(3):
            if mat[i][j] == a:
               mat[i][j] = "O"
               flag = True
               return True
    if flag == False:
        return False

def verifica(mat):
    diago = []
    for i in range(3):
        for j in range(3):
            if i == j:
                diago.append(mat[i][j])
    diago2 =[]
    for i in range(3):
        for j in range(3):
            if i+j == 2:
                diago2.append(mat[i][j])
    flag = True
    for x in range(len(diago)-1):
        if diago[x] != diago[x+1]:
            flag = False
    if flag == True:
        return True
    flag = True
    for x in range(len(diago2)-1):
        if diago2[x] != diago2[x+1]:
            flag = False
    if flag == True:
        return True

    for i in range(3):
        flag = True
        for j in range(2):
            if mat[i][j] != mat[i][j+1]:
                flag = False
        if flag == True:
            return True
    
    for j in range(3):
        flag = True
        for i in range(2):
            if mat[i][j] != mat[i+1][j]:
                flag = False
        if flag == True:
            return True
            
    else:
        return False
    
def jogo_da_velha():
    aux = 0
    print("\n\n")
    grid = gerar_mat()
    print_mat(grid)
    ver = False
    while ver == False:
        print("Jogador 1: ")
        a = jogar(grid)
        while a == False:
            print("\n\nEssa posição já foi esolhida, tente novamente.\n\n")
            a = jogar(grid)
        print("\n\n")
        print_mat(grid)
        if verifica(grid):
            break
        aux +=1
        if aux>4:
            break
        print("Jogador 2: ")
        b = jogar_2(grid)
        while b == False:
            print("\n\nEssa posição já foi esolhida, tente novamente.\n\n")
            b = jogar_2(grid)
        print("\n\n")
        print_mat(grid)
        ver = verifica(grid)
    if aux<=4:
        print("\n\nV I T Ó R I A!\n\n")
    else:
        print("\n\nEmpate!\n\n")
    fim = input("Jogar novamente [S/N]: ")
    while fim.upper() != "S" and fim.upper() != "N":
        fim = input("\nEscolha inválida.\nJogar novamente [S/N]: ")
    if fim.upper() == "S":
        jogo_da_velha()


jogo_da_velha()
    
    



