import pygame

pygame.init()
SCREEN_WITDH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WITDH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image...')

backgroundimage = pygame.transform.scale(pygame.image.load('background.png').convert(), (SCREEN_WITDH, SCREEN_HEIGHT))
penguinimage = pygame.transform.scale(pygame.image.load('penguin.png').convert_alpha(), (200, 200))

penguin_rect = penguinimage.get_rect(center = (SCREEN_WITDH // 2 , SCREEN_HEIGHT // 2 - 30))

font = pygame.font.Font(None, 38)
text = font.render('Hello Penguin!', True, pygame.Color('black'))

def game_loop():

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(backgroundimage, (0, 0))
        display_surface.blit(penguinimage, penguin_rect)
        display_surface.blit(text, (100, 100))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    game_loop()