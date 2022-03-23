def testavitoria(matriz,j):
        if(matriz[0][0]==matriz[0][1]==matriz[0][2] and matriz[0][0]!="_" and matriz[0][1]!="_" and matriz[0][2]!="_" or
                    matriz[0][0]==matriz[1][0]==matriz[2][0] and matriz[0][0]!="_" and matriz[1][0]!="_" and matriz[2][0]!="_" or 
                    matriz[0][0]==matriz[1][1]==matriz[2][2] and matriz[0][0]!="_" and matriz[1][1]!="_" and matriz[2][2]!="_" or 
                    matriz[0][1]==matriz[1][1]==matriz[2][1] and matriz[0][1]!="_" and matriz[1][1]!="_" and matriz[2][1]!="_" or 
                    matriz[0][2]==matriz[1][2]==matriz[2][2] and matriz[0][2]!="_" and matriz[1][2]!="_" and matriz[2][2]!="_" or
                    matriz[0][2]==matriz[1][1]==matriz[2][0] and matriz[0][2]!="_" and matriz[1][1]!="_" and matriz[2][0]!="_" or 
                    matriz[1][0]==matriz[1][1]==matriz[1][2] and matriz[1][0]!="_" and matriz[1][1]!="_" and matriz[1][2]!="_" or
                    matriz[2][0]==matriz[2][1]==matriz[2][2] and matriz[2][0]!="_" and matriz[2][1]!="_" and matriz[2][2]!="_"):
                return True # retorna verdadeiro caso o jogador vença na jogada atual
        else:
                return False # retorna falso caso não haja vitória na rodada
