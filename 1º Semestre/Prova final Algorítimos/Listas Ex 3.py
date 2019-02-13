v = []
def valida():
    nota = int(input("Digite a nota: "))
    while nota<0 or nota>10:
        nota = int(input("Nota inválida...\n\nDigite a nota: "))
    return nota
def ler(v):
    for x in range(4):
        nota = valida()
        v.append(nota)

def media(v):
    s = 0
    for x in range(4):
        s += v[x]
    media = s/4
    return media

ler(v)
media = media(v)
print("Media = ",media)
