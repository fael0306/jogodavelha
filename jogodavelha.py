#Document properties
#__author__ = "Alicia Neri de Araujo Manteiga"
#__copyright__ = "Copyright_2021"
#__credits__ = __author__
#__license__ = "GPL"
#__version__ = "1.0.0"
#__maintainer__ = "Alicia_Manteiga"

#__email__ = "alicia.sk3@poli.ufrj.br
#__status__ = "Production"

import metcomunicausuario
import metfuncjogo

def main():

        j1,j2 = metcomunicausuario.digitanome()

        jogo = [["_","_","_"],["_","_","_"],["_","_","_"]]

        for i in range(3):
            print(" ".join(jogo[i]))
        print("")

        nj = 0
        print("\nÉ a vez do", j1)
        metcomunicausuario.xjoga(jogo)
        for i in range(3):
            print(" ".join(jogo[i]))
        #if testavitoria(jogo,j1):
        #    print("\nParabéns, "+ j1 +"! Você venceu!")
        while(nj!=4):
            nj=nj+1
            print("\nÉ a vez do", j2)
            metcomunicausuario.ojoga(jogo)
            for i in range(3):
                print(" ".join(jogo[i]))
            if metfuncjogo.testavitoria(jogo,j2):
                print("\nParabéns, "+ j2 +"! Você venceu!")
                break 
            print("\nÉ a vez do", j1)
            metcomunicausuario.xjoga(jogo)
            for i in range(3):
                print(" ".join(jogo[i]))
            if metfuncjogo.testavitoria(jogo,j1):
                print("\nParabéns, "+ j1 +"! Você venceu!")
                break

        if(metfuncjogo.testavitoria(jogo,j2)==False and metfuncjogo.testavitoria(jogo,j1)==False):
            print("\nDeu velha!")

        retorno = metcomunicausuario.joganovamente()
        if retorno == 1:
                main()
        else:
                print("\nPrograma encerrado")

main()
input()
