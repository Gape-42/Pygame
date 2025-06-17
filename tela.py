import pygame
import time

pygame.init()
clock = pygame.time.Clock()
running = True

#resolução da tela
info_tela = pygame.display.Info()
resolucao_x = info_tela.current_w
resolucao_y = info_tela.current_h
tela = pygame.display.set_mode((resolucao_x, resolucao_y))

#Tabuleiro
altura_tabuleiro = 600
largura_tabuleiro = 600
topo_tabuleiro = (resolucao_y - altura_tabuleiro)/2
esquerda_tabuleiro = (resolucao_x - largura_tabuleiro)/2
base_tabuleiro = pygame.Rect(esquerda_tabuleiro, topo_tabuleiro, largura_tabuleiro, altura_tabuleiro)
TAMANHO_CELULA = largura_tabuleiro/3

#Representação do tabuleiro. 0 = vazio, 1 = X, 2 = O
matriz_jogo = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

#apenas para teste
contador = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Cor do fundo
    tela.fill("aquamarine4")

    #Desenhando o tabuleiro
    pygame.draw.rect(tela, "white", base_tabuleiro)

    #Desenhando as linhas
    for i in range (0,4):
        x_pos = base_tabuleiro.left + i * TAMANHO_CELULA
        y_pos = base_tabuleiro.top + i * TAMANHO_CELULA
        pygame.draw.line(tela, "black", (x_pos, base_tabuleiro.top), (x_pos, base_tabuleiro.bottom), 5)
        pygame.draw.line(tela, "black", (base_tabuleiro.left, y_pos), (base_tabuleiro.right, y_pos), 5)
        
    #Desenhando Xis e bolinha no tabuleiro
    for linha in range(3):
        for coluna in range(3):
            centro_x = base_tabuleiro.left + coluna * TAMANHO_CELULA + TAMANHO_CELULA/2
            centro_y = base_tabuleiro.top + linha * TAMANHO_CELULA + TAMANHO_CELULA/2
            
            if matriz_jogo[linha][coluna] == 2:
                pygame.draw.circle(tela, "midnightblue", (centro_x, centro_y), 60, 10)    
            elif matriz_jogo[linha][coluna] == 1:
                meia_largura_xis = 50
                pygame.draw.line(tela, "forestgreen", (centro_x - meia_largura_xis, centro_y - meia_largura_xis),
                                                (centro_x + meia_largura_xis, centro_y + meia_largura_xis), 15)
                pygame.draw.line(tela, "forestgreen", (centro_x + meia_largura_xis, centro_y - meia_largura_xis),
                                                (centro_x -  meia_largura_xis, centro_y + meia_largura_xis), 5)
                
    #apenas para testar a atualização da matriz
    matriz_jogo = [[2, 0, 2],
                    [2, 1, 2],
                    [2, 0, 1]]
    if(contador%2==0):
        matriz_jogo[0][0] = 1
    else:
        matriz_jogo[0][0] = 2
    contador += 1
    time.sleep(1)


    pygame.display.flip()    
    clock.tick(60)
    
pygame.quit()