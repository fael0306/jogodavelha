def xjoga(matriz):
    try:
        l = int(input("Linha da jogada do X (1 a 3): "))
        while(l<1 or l>3):
            l = int(input("Linha da jogada do X (1 a 3, sempre): "))
        c = int(input("Coluna da jogada do X (1 a 3): "))
        while(c<1 or c>3):        
            c = int(input("Posição vertical da jogada do X: (1 a 3, sempre): "))
        if(matriz[l-1][c-1]!="_"):
            print("Essa posição já está preenchida. Tente novamente.")
            xjoga(matriz)
        else:
            matriz[l-1][c-1] = "X"
    except:
        print("Você digitou algo errado. Tente novamente.")
        xjoga(matriz)
        
def ojoga(matriz):
    try:
        l = int(input("Linha da jogada do O (1 a 3): "))
        while(l<1 or l>3):
            l = int(input("Linha da jogada do O (1 a 3, sempre): "))
        c = int(input("Coluna da jogada do O (1 a 3): "))
        while(c<1 or c>3):        
            c = int(input("Coluna da jogada do O: (1 a 3, sempre): "))
        if(matriz[l-1][c-1]!="_"):
            print("Essa posição já está preenchida. Tente novamente.")
            ojoga(matriz)
        else:
            matriz[l-1][c-1] = "O"
    except:
        print("Você digitou algo errado. Tente novamente.")
        xjoga(matriz)

def digitanome():
    j1 = input("Digite o nome do jogador 1: ")
    j2 = input("\nDigite o nome do jogador 2: ")
    print("")
    return j1,j2

def joganovamente():
    jn = int(input("\n\nDeseja jogar novamente (1 - Sim ou 2 - Não): "))
    print("")
    while(jn!=1 and jn!=2):
        jn = input("Deseja jogar novamente (1 - Sim ou 2 - Não) digite uma opção válida: ")
    return jn
