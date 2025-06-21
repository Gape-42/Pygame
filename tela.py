import pygame
import time

# Representação do tabuleiro.
# 0 = vazio
# 1 = X
# 2 = O
matriz_jogo = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

pygame.init()
clock = pygame.time.Clock()
running = True

# Resolução da tela
info_tela = pygame.display.Info()
resolucao_x = info_tela.current_w
resolucao_y = info_tela.current_h
tela = pygame.display.set_mode((resolucao_x, resolucao_y), pygame.RESIZABLE)

# Tabuleiro
altura_tabuleiro = 600
largura_tabuleiro = 600
topo_tabuleiro = (resolucao_y - altura_tabuleiro) / 2
esquerda_tabuleiro = (resolucao_x - largura_tabuleiro) / 2
base_tabuleiro = pygame.Rect(esquerda_tabuleiro, topo_tabuleiro, largura_tabuleiro, altura_tabuleiro)
TAMANHO_CELULA = largura_tabuleiro / 3


# Função paara desenhar o tabuleiro
def desenhar_tabuleiro():
    # Cor do fundo
    tela.fill("aquamarine4")
    
    # Desenhando o tabuleiro
    pygame.draw.rect(tela, "white", base_tabuleiro)

    # Desenhando as linhas
    for i in range (0,4):
        x_pos = base_tabuleiro.left + i * TAMANHO_CELULA
        y_pos = base_tabuleiro.top + i * TAMANHO_CELULA
        pygame.draw.line(tela, "black", (x_pos, base_tabuleiro.top), (x_pos, base_tabuleiro.bottom), 5)
        pygame.draw.line(tela, "black", (base_tabuleiro.left, y_pos), (base_tabuleiro.right, y_pos), 5)


# Função para desenhar a jogada
def desenhar_jogada():
    # Desenhando Xis e bolinha no tabuleiro
    for linha in range(3):
        for coluna in range(3):
            centro_x = base_tabuleiro.left + coluna * TAMANHO_CELULA + TAMANHO_CELULA / 2
            centro_y = base_tabuleiro.top + linha * TAMANHO_CELULA + TAMANHO_CELULA / 2
            
            if matriz_jogo[linha][coluna] == 2:
                pygame.draw.circle(tela, "midnightblue", (centro_x, centro_y), 60, 10)    
            elif matriz_jogo[linha][coluna] == 1:
                meia_largura_xis = 50
                pygame.draw.line(tela, "forestgreen", (centro_x - meia_largura_xis, centro_y - meia_largura_xis),
                                                (centro_x + meia_largura_xis, centro_y + meia_largura_xis), 15)
                pygame.draw.line(tela, "forestgreen", (centro_x + meia_largura_xis, centro_y - meia_largura_xis),
                                                (centro_x -  meia_largura_xis, centro_y + meia_largura_xis), 5)


# Função para a verificação de vitória
def verificar_vencedor(jogador):
    sequencia_linha = 0
    # Percorre verificando a linha
    for i in range(3):
        sequencia_linha = 0
        for j in range(3):
            if matriz_jogo[i][j] == jogador:
                sequencia_linha += 1

            if sequencia_linha == 3:
                return jogador

    sequencia_coluna = 0
    # Percorre verificando a coluna
    for i in range(3):
        sequencia_coluna = 0
        for j in range(3):
            if matriz_jogo[j][i] == jogador:
                sequencia_coluna += 1
            
            if sequencia_coluna == 3:
                return jogador
    
    # Verifica a principal
    if matriz_jogo[0][0] == jogador and matriz_jogo[1][1] == jogador and matriz_jogo[2][2] == jogador:
        return jogador
    
    # Verifica a diagonal secundária
    if matriz_jogo[0][2] == jogador and matriz_jogo[1][1] == jogador and matriz_jogo[2][0] == jogador:
        return jogador


#apenas para testeAdd commentMore actions
contador = 0

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Chamada da função para desenhar o tabuleiro
        desenhar_tabuleiro()
        
        # Chamada da função para desenhar as jogadas
        desenhar_jogada()
                    
        # Apenas para testar a atualização da matriz
        matriz_jogo = [[0, 0, 2],
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

        # Verifica quem ganhou
        if verificar_vencedor(1) == 1:   # X ganhou
            # Sugestão: Implementar algo aqui para exibir quem venceu
            continue
        elif verificar_vencedor(2) == 2: # O ganhou
            # Sugestão: Implementar algo aqui para exibir quem venceu
            continue
        
    pygame.quit()
