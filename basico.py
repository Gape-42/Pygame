import pygame

pygame.init()
tela = pygame.display.set_mode((1366, 768))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    tela.fill("white")

    pygame.display.flip()
    
pygame.quit()