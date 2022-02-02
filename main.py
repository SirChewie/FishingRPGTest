import random
import pygame
from sys import exit

pygame.init()

# screen size
screen = pygame.display.set_mode((800, 400))
# Title of main window
pygame.display.set_caption("Fishing4Days")
# Icon of main window
pygame.display.set_icon(pygame.image.load('Imgs/Fish/GreenFins_YellowBelly.png').convert_alpha())
clock = pygame.time.Clock()

# Landscape
background_surf = pygame.image.load('Imgs/Landscape/Background1.png').convert()
foreground_surf = pygame.image.load('Imgs/Landscape/Foreground.png').convert()
cloud_surf = pygame.image.load('Imgs/Landscape/Cloud1.png').convert_alpha()
tree_surf = pygame.image.load('Imgs/Landscape/Tree.png').convert_alpha()


class Ui:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.sx = sx
        self.y = y
        self.sy = sy
        self.surf_skin = pygame.image.load('Imgs/UI/StressBarSkin.png').convert_alpha()
        self.rect_skin = self.surf_skin.get_rect(midbottom=(sx, sy))
        self.stress_bar_R = pygame.image.load('Imgs/UI/StressBarColorR.png')
        self.stress_bar_R_rect = self.stress_bar_R.get_rect(midbottom=(sx, sy))
        self.surf = pygame.image.load('Imgs/UI/StressBarLine.png').convert()
        self.rect = self.surf.get_rect(midbottom=(x, y))
        self.color = (120, 241, 56)
        self.velX = 0
        self.velY = 0
        self.speed = 3
        self.x = True

    def draw(self, screen):
        if player.is_fishing:
            screen.blit(self.stress_bar_R, self.stress_bar_R_rect)
            screen.blit(self.surf_skin, self.rect_skin)
            screen.blit(self.surf, self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0

        # can fish or not
        if not player.is_fishing:
            if player.space_pressed and player.mouse_pos[1] >= 315:
                player.fishing_pos = (player.mouse_pos[0], player.mouse_pos[1])
                player.is_fishing = True

        if player.is_fishing:
            player.mobile = False
            if (fish.x, fish.y) == (player.fishing_pos[0], player.fishing_pos[1]):
                player.hooked = True

            if player.mouseL_pressed and not player.mouseM_pressed and not player.mouseR_pressed:
                print("Reeling" + str(player.line_str))
                if ui.x >= 490:
                    if player.line_str <= 0:
                        print('Line broke')
                        ui.x = 369
                        player.hooked = False
                        player.is_fishing = False
                        player.mobile = True
                        player.line_str = 300
                        return
                    player.line_str -= 10
                    return
                player.line_str -= 1
                self.velX += self.speed

            elif player.line_str <= 0:
                print('Line broke')
                ui.x = 369
                player.hooked = False
                player.is_fishing = False
                player.mobile = True
                player.line_str = 300
                return
            else:
                if ui.x <= 250:
                    print('Fish got off')
                    ui.x = 369
                    player.hooked = False
                    player.is_fishing = False
                    player.mobile = True
                    player.line_str = 300
                    return
                player.line_str += .5
                self.velX -= self.speed / 2
            self.x += self.velX
            self.y += self.velY
            self.stress_bar_R_rect = pygame.Rect(self.sx, self.sy, 210, 25)
            self.rect = pygame.Rect(self.x, self.y, 7, 17)
            self.rect_skin = pygame.Rect(self.sx, self.sy, 210, 25)


class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surf = pygame.image.load('Imgs/Fish/GreenFins_YellowBelly.png')
        self.rect = self.surf.get_rect(midbottom=(x, y))
        self.velX = 0
        self.velY = 0
        self.is_hooked = False

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0

        self.x += self.velX
        self.y += self.velY
        self.rect = pygame.Rect(self.x, self.y, 25, 11)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surf = pygame.image.load('Imgs/Characters/SChar.png').convert_alpha()
        self.rect = self.surf.get_rect(midbottom=(x, y))
        self.velX=0
        self.velY=0
        self.color = (120, 241, 56)
        self.mobile = True
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouseL_pressed = False
        self.mouseM_pressed = False
        self.mouseR_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False
        self.speed = 1
        self.is_fishing = False
        self.line_str = 300
        self.hooked = False
        self.fishing_pos = (0, 0)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.velX=0
        self.velY=0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        if self.space_pressed:
            self.is_fishing = True

        self.x += self.velX
        self.y += self.velY
        self.rect = pygame.Rect(self.x, self.y, 32, 64)


player = Player(50, 100)
ui = Ui(253, 369, 250, 365)
fish = Fish(random.randint(0, 800), random.randint(315, 400))
# Main game loop
while True:

    # event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Movement
        if event.type == pygame.KEYDOWN and player.mobile:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.down_pressed = True
            if event.key == pygame.K_SPACE:
                player.space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False
            if event.key == pygame.K_SPACE:
                player.space_pressed = False

        # Mouse Controls
        player.mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.mouseL_pressed = True
            if event.button == 2:
                player.mouseM_pressed = True
            if event.button == 3:
                player.mouseR_pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                player.mouseL_pressed = False
            if event.button == 2:
                player.mouseM_pressed = False
            if event.button == 3:
                player.mouseR_pressed = False

    # draw
    screen.blit(background_surf, (0, 0))
    screen.blit(foreground_surf, (0, 200))
    screen.blit(cloud_surf, (400, -50))
    screen.blit(tree_surf, (0, 25))
    player.draw(screen)
    ui.draw(screen)
    fish.draw(screen)
    # update
    player.update()
    ui.update()
    fish.update()
    pygame.display.flip()

    # tick/frame rate
    clock.tick(120)


