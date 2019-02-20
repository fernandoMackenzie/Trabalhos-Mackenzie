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

def atirar(grid,linha,coluna):
    if grid[linha][coluna] == ".":
        grid[linha][coluna] = "x"
        print("\n\n")
        print_matriz(grid)
        return True
    elif grid[linha][coluna] == "x" or grid[linha][coluna] == "X":
        print("\n\n")
        print_matriz(grid)
        return False
    else:
        grid[linha][coluna] = "X"
        print("\n\n")
        print_matriz(grid)
        return True
    
        
def jogar():
    grid = inicializarGrid()
    print("Tabuleiro: \n\n")
    print_matriz(grid)
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
    atirar(grid,3,3)
    

jogar()


