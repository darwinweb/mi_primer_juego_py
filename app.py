import pygame
import sys
import random

pygame.init()

#Dimensiones de la pantalla y colores

ancho = 800
alto = 600
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)

#player

player_size = 60
player_pos = [ancho/2, alto - player_size * 2]

#Enemigo
enemigo_size = 60
enemigo_pos = [random.randint(0, ancho - enemigo_size),0]

# ventana y titulo del juego
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Invacion Espacial")

game_over = False
clock = pygame.time.Clock()

def detectar_colision(player_pos, enemigo_pos):
    px = player_pos[0]
    py = player_pos[1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]

    if (ex >= px and ex <(px + player_size)) or (px >= ex and px <(ex + enemigo_size)):
        if (ey >= py and ey <(py + player_size)) or (py >= ey and py <(ey + enemigo_size)):
            return True
        return False 
      
def pantalla_game_over():
    font = pygame.font.SysFont(None, 75)
    texto = font.render("Game Over", True, color_rojo)
    ventana.blit(texto, (ancho/2 - texto.get_width()/2, alto/2 - texto.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

#Eventos
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size
            
            player_pos[0] = x

    ventana.fill(color_negro)

    if enemigo_pos[1] >= 0 and enemigo_pos[1] < alto:
        enemigo_pos[1] += 20
    else:
        enemigo_pos[0] = random.randint(0, ancho - enemigo_size)
        enemigo_pos[1] = 0

    if detectar_colision(player_pos,enemigo_pos):
        game_over = True
        pantalla_game_over()

    #dibujo del jugador y enemigo

    pygame.draw.rect(ventana, color_azul,
                     (enemigo_pos[0], enemigo_pos[1],
                     enemigo_size, enemigo_size))

    pygame.draw.rect(ventana, color_rojo,
                     (player_pos[0], player_pos[1], 
                      player_size, player_size))
    
    clock.tick(40)
    pygame.display.update()
    

