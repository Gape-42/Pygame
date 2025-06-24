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
    
    # Verifica a diagonal principal
    if matriz_jogo[0][0] == jogador and matriz_jogo[1][1] == jogador and matriz_jogo[2][2] == jogador:
        return jogador
    
    # Verifica a diagonal secundária
    if matriz_jogo[0][2] == jogador and matriz_jogo[1][1] == jogador and matriz_jogo[2][0] == jogador:
        return jogador


# Função para verificar empate
def verificar_empate():
    for linha in matriz_jogo:
        if 0 in linha:
            return False
    return True


# Exibe tela de quem ganhou ou empate
def exibir_vencedor(vencedor):
    fonte = pygame.font.SysFont(None, 72)
    if vencedor == 0:
        texto_vencedor = fonte.render('Empate!', True, "white")
    else:
        texto_vencedor = fonte.render(f'Jogador {vencedor} venceu!', True, "white")

    # Dimensões da caixa
    largura_modal = 500
    altura_modal = 320
    x_modal = (resolucao_x - largura_modal) // 2
    y_modal = (resolucao_y - altura_modal) // 2
    modal_rect = pygame.Rect(x_modal, y_modal, largura_modal, altura_modal)

    # Botão "Jogar Novamente"
    largura_botao = 250
    altura_botao = 60
    x_botao_jogar_novamente = (resolucao_x - largura_botao) // 2
    y_botao_jogar_novamente = (resolucao_y - altura_botao) // 2
    botao_jogar_novamente = pygame.Rect(x_botao_jogar_novamente, y_botao_jogar_novamente, largura_botao, altura_botao)

    # Botão "Sair"
    x_botao_sair = (resolucao_x - largura_botao) // 2
    y_botao_sair = (resolucao_y - altura_botao + 170) // 2
    botao_sair = pygame.Rect(x_botao_sair, y_botao_sair, largura_botao, altura_botao)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar_novamente.collidepoint(event.pos):
                    return  # Reinicia o jogo
                elif botao_sair.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        # Desenha o tabuleiro por trás
        desenhar_tabuleiro()
        desenhar_jogada()

        # Modal
        pygame.draw.rect(tela, "gray10", modal_rect, border_radius=20)
        pygame.draw.rect(tela, "white", modal_rect, width=5, border_radius=20)

        # Texto do vencedor
        tela.blit(texto_vencedor, (
            x_modal + (largura_modal - texto_vencedor.get_width()) // 2,
            y_modal + 40
        ))

        # Fonte dos botões
        fonte_botao = pygame.font.SysFont(None, 40)

        # Botão "Jogar Novamente"
        pygame.draw.rect(tela, "green", botao_jogar_novamente, border_radius=10)
        texto_jogar = fonte_botao.render("Jogar Novamente", True, "white")
        tela.blit(texto_jogar, (
            botao_jogar_novamente.x + (largura_botao - texto_jogar.get_width()) // 2,
            botao_jogar_novamente.y + (altura_botao - texto_jogar.get_height()) // 2
        ))

        # Botão "Sair"
        pygame.draw.rect(tela, "red", botao_sair, border_radius=10)
        texto_sair = fonte_botao.render("Sair", True, "white")
        tela.blit(texto_sair, (
            botao_sair.x + (largura_botao - texto_sair.get_width()) // 2,
            botao_sair.y + (altura_botao - texto_sair.get_height()) // 2
        ))

        pygame.display.flip()
        clock.tick(60)


# Apenas para teste
contador = 0

# Loop principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Chamada da função para desenhar o tabuleiro
    desenhar_tabuleiro()
    
    # Chamada da função para desenhar as jogadas
    desenhar_jogada()
    pygame.display.flip()
                
    # ------------------- Inicio dos Algoritmos de busca -------------------
    # Apenas para testar a atualização da matriz
    matriz_jogo = [[0, 2, 1],
                   [1, 1, 2],
                   [2, 1, 2]]

    # Chamada da função para desenhar as jogadas
    desenhar_jogada()
    pygame.display.flip()

    if(contador%2==0):
        matriz_jogo[0][0] = 1
    else:
        matriz_jogo[0][0] = 2
    contador += 1
    # -------------------- Fim dos Algoritmos de busca --------------------

    time.sleep(1)
    desenhar_jogada()
    pygame.display.flip()
    clock.tick(60)
    time.sleep(1)

    # Verifica quem ganhou
    if verificar_vencedor(1) == 1:   # X ganhou
        exibir_vencedor(1)
        matriz_jogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        continue

    elif verificar_vencedor(2) == 2: # O ganhou
        exibir_vencedor(2)
        matriz_jogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        continue

    elif verificar_empate():         # Empate
        exibir_vencedor(0)
        matriz_jogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        continue
    
pygame.quit()
