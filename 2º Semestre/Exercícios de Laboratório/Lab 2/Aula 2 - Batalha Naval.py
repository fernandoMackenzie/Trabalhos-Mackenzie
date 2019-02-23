import random
def inicializarGrid():
    grid = []
    for i in range(11):
        linha = []
        for j in range(11):
            linha.append(".")
        grid.append(linha)
    for i in range(11):
        grid[i][0] = i
    for j in range(11):
        grid[0][j]= j
    return grid

def print_matriz(mat):
    for i in range(11):
        for j in range(11):
            print(mat[i][j], end=" ")
        print("\n")


def porta_avioes(grid,linha,coluna,vertical):
    if vertical == True and linha>6:
         return False
    elif vertical == False and coluna>6:
        return False
    else:
        if vertical == True:
            for x in range(linha,linha+5):
                if grid[x][coluna] != ".":
                    return False
            for x in range(linha,linha+5):
                grid[x][coluna] = "P"
            return True
        else:
            for x in range(coluna,coluna+5):
                if grid[linha][x] != ".":
                    return False
            for x in range(coluna,coluna+5):
                grid[linha][x] = "P"
            return True

def encouracado(grid,linha,coluna,vertical):
    if vertical == True and linha>7:
         return False
    elif vertical == False and coluna>7:
        return False
    else:
        if vertical == True:
            for x in range(linha,linha+4):
                if grid[x][coluna] != ".":
                    return False
            for x in range(linha,linha+4):
                grid[x][coluna] = "E"
            return True
        else:
            for x in range(coluna,coluna+4):
                if grid[linha][x] != ".":
                    return False
            for x in range(coluna,coluna+4):
                grid[linha][x] = "E"
            return True

def cruzador(grid,linha,coluna,vertical):
    if vertical == True and linha>8:
         return False
    elif vertical == False and coluna>8:
        return False
    else:
        if vertical == True:
            for x in range(linha,linha+3):
                if grid[x][coluna] != ".":
                    return False
            for x in range(linha,linha+3):
                grid[x][coluna] = "C"
            return True
        else:
            for x in range(coluna,coluna+3):
                if grid[linha][x] != ".":
                    return False
            for x in range(coluna,coluna+3):
                grid[linha][x] = "C"
            return True

def submarino(grid,linha,coluna,vertical):
    if vertical == True and linha>9:
         return False
    elif vertical == False and coluna>9:
        return False
    else:
        if vertical == True:
            for x in range(linha,linha+2):
                if grid[x][coluna] != ".":
                    return False
            for x in range(linha,linha+2):
                grid[x][coluna] = "S"
            return True
        else:
            for x in range(coluna,coluna+2):
                if grid[linha][x] != ".":
                    return False
            for x in range(coluna,coluna+2):
                grid[linha][x] = "S"
            return True

def atirar(grid,linha,coluna,grid2):
    if grid[linha][coluna] == ".":
        grid[linha][coluna] = "x"
        grid2[linha][coluna] = "x"
        print("\n\nMARINHEIRO: ÁÁÁGUA!!\n\n")
        print("CAMPO DE BATALHA: ")
        print_matriz(grid2)
        return True,False
    elif grid[linha][coluna] == "x" or grid[linha][coluna] == "X":
        print("\n\nMARINHEIRO: Desculpe Capitão, mas já verificamos essas coordenadas!\n\n")
        return False,True
    else:
        grid[linha][coluna] = "X"
        grid2[linha][coluna] = "X"
        print("\n\nMARINHEIRO: Bem na mosca Capitão!\n\n")
        print("CAMPO DE BATALHA: ")
        print_matriz(grid2)
        return True,True
    
        
def jogar():
    pts = 0
    chances = 30
    grid = inicializarGrid()
    grid2 = inicializarGrid()
    print("CAMPO DE BATALHA: \n\n")
    print_matriz(grid2)
    #Posicionamento das embarcações
    flag = porta_avioes(grid,random.randint(1,10),random.randint(1,10),False)
    while flag == False:
        flag = porta_avioes(grid,random.randint(1,10),random.randint(1,10),False)

    flag = encouracado(grid,random.randint(1,10),random.randint(1,10),True)
    while flag == False:
        flag = encouracado(grid,random.randint(1,10),random.randint(1,10),True)

    flag = cruzador(grid,random.randint(1,10),random.randint(1,10),False)
    while flag == False:
        flag = cruzador(grid,random.randint(1,10),random.randint(1,10),False)

    flag = submarino(grid,random.randint(1,10),random.randint(1,10),True)
    
    while flag == False:
        flag = submarino(grid,random.randint(1,10),random.randint(1,10),True)
    #Fim do posicionamento
    
    while pts<14 and chances>0:
        print("Sua munição: ",chances)
        linha = int(input("Digite a linha da sua jogada: "))
        while linha < 1 or linha > 10:
            linha = int(input("\nMARINHEIRO: Ops! Só vale no mar Capitão \n\nDigite a linha da sua jogada: "))
        coluna = int(input("Digite a coluna da sua jogada: "))
        while coluna <1 or coluna> 10:
            coluna = int(input("\nMARINHEIRO: Não encontramos essas coordenadas Senhor, vamos tentar de novo!\n\nDigite a coluna da sua jogada: "))
        tiro,flag = atirar(grid,linha,coluna,grid2)
        if tiro == True and flag == True:
            pts +=1
            chances -= 1
        elif tiro == True and flag == False:
            chances -= 1
    if pts == 14:
        print("\n\nVocê venceu !")
    else:
        print("\n\nMARINHEIRO: Acabou a munição Capitão, hora de bater em retirada... \nnvocê perdeu!\nVeja o campo de batalha: \n")
        print_matriz(grid)
    fim = input("Jogar novamente [S/N]: ")
    while fim.upper() != "S" and fim.upper() != "N":
        fim = input("\nEscolha inválida.\nJogar novamente [S/N]: ")
    if fim.upper() == "S":
        jogar()
    
    
print('''

                                  BEM VINDO À BATALHA NAVAL

                                  
	Frota inimiga:
	
	1 - Porta-aviões (5 espaços)
	1 - Encouraçado  (4 espaços)
	1 - Cruzador     (3 espaços)
	1 - Submarino    (2 espaços)
	
	Determine as coordenadas do seu ataque através dos números no tabuleiro.
	**Você tem apenas 30 chances para detonar a marinha inimiga!

	**Sempre que você acertar um ataque em uma embarcação aparecerá um "X" na posição do ataque.
	Se você errar, aparecerá um "x"(minúsculo).

	**Se você tentar atirar 2 vezes no mesmo local, receberá uma mensagem de aviso e suas chances não serão
	deduzidas.


	''')
jogar()


