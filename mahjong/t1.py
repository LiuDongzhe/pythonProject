import pygame

pygame.init()
background = pygame.image.load('interface/interface.png')
background = pygame.transform.smoothscale(background, (50, 50))

window = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 100)
list1 = [1, 2, 3, 4, 5]
test1 = str(len(list1))
text = font.render(test1, True, (1, 1, 1))
running = True
while running:
    for event in pygame.event.get():
        window.fill((0, 0, 0))
        window.blit(background, (320, 100))
        window.blit(text, (320, 100))
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    #pygame.quit()