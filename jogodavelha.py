import metcomunicausuario
import metfuncjogo

def jogar_novamente():
    retorno = metcomunicausuario.joganovamente()
    return retorno == 1

def exibir_tabuleiro(jogo):
    for linha in jogo:
        print(" ".join(linha))
    print()

def jogar(jogador, jogo):
    if jogador == "X":
        metcomunicausuario.xjoga(jogo)
    elif jogador == "O":
        metcomunicausuario.ojoga(jogo)

def verificar_vitoria(jogador, jogo):
    return metfuncjogo.testavitoria(jogo, jogador)

def main():
    j1, j2 = metcomunicausuario.digitanome()

    jogo = [["_"] * 3 for _ in range(3)]

    jogadores = [(j1, "X"), (j2, "O")]
    
    exibir_tabuleiro(jogo)
    
    for rodada in range(9):
        jogador, simbolo = jogadores[rodada % 2]
        print(f"\nÉ a vez do {jogador}")
        jogar(simbolo, jogo)
        exibir_tabuleiro(jogo)
        
        if verificar_vitoria(simbolo, jogo):
            print(f"\nParabéns, {jogador}! Você venceu!")
            break
    else:
        print("\nDeu velha!")

    if jogar_novamente():
        main()
    else:
        print("\nPrograma encerrado")

if __name__ == "__main__":
    main()
