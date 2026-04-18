import pygame
import sys
def fazwin():
    # Inicializar pygame
    pygame.init()
    pygame.mixer.init()

    # Crear ventana en pantalla completa
    wind = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("")

    # Cargar imagen y música
    fazbear_img = pygame.image.load("./assets/img.jpg")
    pygame.mixer.music.load("./assets/aud.mp3")
    pygame.mixer.music.play(-1)

    execute_win = True

    # Loop principal
    while execute_win:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                execute_win = False

        wind.fill((0, 0, 0))
        wind.blit(fazbear_img, (0, 0))
        pygame.display.flip()

    pygame.quit()