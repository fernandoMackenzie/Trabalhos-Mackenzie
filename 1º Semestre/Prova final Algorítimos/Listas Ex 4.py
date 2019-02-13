v =[]
medias = []
bons_alunos = 0
def valida():
    nota = int(input("Digite a nota: "))
    while nota<0 or nota> 10:
        nota = int(input("Nota inválida...\n\nDigite a nota: "))
    return nota

def ler(v):
    for x in range(4):
        nota = valida()
        v.append(nota)
        

def media(v,medias):
    s = 0
    for x in range(4):
        s += v[x]
    media = s/4
    medias.append(media)

    
    

for x in range(3):
    print("Digite as notas do aluno ",x+1)
    ler(v)
    media(v,medias)
    v = []
for x in range(len(medias)):
    n = medias[x]
    if n >= 7.5:
        bons_alunos += 1
print("Medias dos alunos", medias,"\n\nAlunos com notas acima de 7.5: ",bons_alunos)

