import pygame
from sys import exit

pygame.init()

# screen size
screen = pygame.display.set_mode((800, 400))
# Title of main window
pygame.display.set_caption("Fishing4Days")
# Icon of main window
clock = pygame.time.Clock()


background_surf = pygame.image.load('Imgs/Landscape/Background1.png').convert()
foreground_surf = pygame.image.load('Imgs/Landscape/Foreground.png').convert()
cloud_surf = pygame.image.load('Imgs/Landscape/Cloud1.png').convert_alpha()
tree_surf = pygame.image.load('Imgs/Landscape/Tree.png').convert_alpha()

char_surf = pygame.image.load('Imgs/Characters/SChar.png').convert_alpha()
char_rect = char_surf.get_rect(midbottom=(20, 250))


# Main game loop
while True:
    mouse_pos = pygame.mouse.get_pos()
    mouse_btn = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                char_rect.x +=3

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Reeling")

        if event.type == pygame.MOUSEBUTTONUP:
            print('Stopped Reeling')
            # can fish or not
        if mouse_pos[1] >= 315 and mouse_btn[0]:
            print(str(mouse_pos) + "fish")

    screen.blit(background_surf, (0, 0))
    screen.blit(foreground_surf, (0, 200))
    screen.blit(cloud_surf, (400, -50))
    screen.blit(tree_surf, (0, 25))
    screen.blit(char_surf, char_rect)










    pygame.display.update()

    # tick/frame rate
    clock.tick(60)
