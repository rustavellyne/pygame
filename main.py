import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
main_font = pygame.font.Font('./assets/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('./assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('./assets/graphics/ground.png').convert()
text_surface = main_font.render('My Game', False, 'Green')

snail_surface = pygame.image.load('./assets/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300));
player_surface = pygame.image.load('./assets/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(50,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    if snail_rect.left < -100:
        snail_rect.left = 800
    if player_rect.left > 800:
        player_rect.left = -50
    snail_rect.left -= 1
    player_rect.left += 1
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60) 
