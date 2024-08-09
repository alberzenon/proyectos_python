import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Tamaño de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

# Tamaño de los bloques
TAMANO_BLOQUE = 20

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Inicializar fuente
fuente = pygame.font.SysFont(None, 55)

# Cargar sonidos
comer_sonido = pygame.mixer.Sound("comer.wav")
game_over_sonido = pygame.mixer.Sound("game_over.wav")

# Función para mostrar la pantalla de inicio
def mostrar_pantalla_inicio():
    ventana.fill(NEGRO)
    texto_inicio = fuente.render("Presiona Enter para jugar", True, BLANCO)
    ventana.blit(texto_inicio, (ANCHO // 2 - texto_inicio.get_width() // 2, ALTO // 2 - texto_inicio.get_height() // 2))
    pygame.display.flip()

    # Esperar a que el jugador presione Enter
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Enter
                    esperando = False

# Función para mostrar la pantalla de Game Over
def mostrar_game_over(puntuacion):
    ventana.fill(NEGRO)
    texto_game_over = fuente.render("Game Over", True, ROJO)
    ventana.blit(texto_game_over, (ANCHO // 2 - texto_game_over.get_width() // 2, ALTO // 2 - 100))
    
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    ventana.blit(texto_puntuacion, (ANCHO // 2 - texto_puntuacion.get_width() // 2, ALTO // 2))
    
    texto_reiniciar = fuente.render("Presiona Enter para reiniciar", True, BLANCO)
    ventana.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 50))
    
    pygame.display.flip()

    # Esperar a que el jugador presione Enter
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Enter
                    esperando = False

# Función para verificar colisiones
def colision_con_cuerpo(cabeza, segmentos):
    return cabeza in segmentos[:-1]  # No verificar la colisión con la cabeza

# Función principal del juego
def juego():
    # Velocidad inicial
    velocidad_x = TAMANO_BLOQUE
    velocidad_y = 0
    velocidad_juego = 15

    # Posición inicial de la serpiente
    posicion_serpiente_x = ANCHO // 2
    posicion_serpiente_y = ALTO // 2

    # Lista para almacenar los segmentos de la serpiente
    segmentos_serpiente = []
    longitud_serpiente = 1

    # Posición inicial de la comida
    posicion_comida_x = random.randrange(0, ANCHO - TAMANO_BLOQUE, TAMANO_BLOQUE)
    posicion_comida_y = random.randrange(0, ALTO - TAMANO_BLOQUE, TAMANO_BLOQUE)

    # Inicializar puntuación
    puntuacion = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidad_x == 0:
                    velocidad_x = -TAMANO_BLOQUE
                    velocidad_y = 0
                elif evento.key == pygame.K_RIGHT and velocidad_x == 0:
                    velocidad_x = TAMANO_BLOQUE
                    velocidad_y = 0
                elif evento.key == pygame.K_UP and velocidad_y == 0:
                    velocidad_x = 0
                    velocidad_y = -TAMANO_BLOQUE
                elif evento.key == pygame.K_DOWN and velocidad_y == 0:
                    velocidad_x = 0
                    velocidad_y = TAMANO_BLOQUE

        # Mover la serpiente
        posicion_serpiente_x += velocidad_x
        posicion_serpiente_y += velocidad_y

        # Agregar la cabeza de la serpiente a la lista de segmentos
        cabeza_serpiente = [posicion_serpiente_x, posicion_serpiente_y]
        segmentos_serpiente.append(cabeza_serpiente)

        # Eliminar el segmento más antiguo si la longitud de la serpiente excede el límite
        if len(segmentos_serpiente) > longitud_serpiente:
            del segmentos_serpiente[0]

        # Limpiar la ventana
        ventana.fill(NEGRO)

        # Dibujar la serpiente con color aleatorio
        color_serpiente = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for segmento in segmentos_serpiente:
            pygame.draw.rect(ventana, color_serpiente, (segmento[0], segmento[1], TAMANO_BLOQUE, TAMANO_BLOQUE))

        # Dibujar la comida
        pygame.draw.rect(ventana, ROJO, (posicion_comida_x, posicion_comida_y, TAMANO_BLOQUE, TAMANO_BLOQUE))

        # Verificar si la serpiente ha comido la comida
        if posicion_serpiente_x == posicion_comida_x and posicion_serpiente_y == posicion_comida_y:
            posicion_comida_x = random.randrange(0, ANCHO - TAMANO_BLOQUE, TAMANO_BLOQUE)
            posicion_comida_y = random.randrange(0, ALTO - TAMANO_BLOQUE, TAMANO_BLOQUE)
            longitud_serpiente += 1
            puntuacion += 1  # Incrementar la puntuación
            comer_sonido.play()  # Reproducir sonido al comer

            # Aumentar la velocidad del juego
            velocidad_juego += 1

        # Verificar si la serpiente se ha chocado con los bordes o con su cuerpo
        if (posicion_serpiente_x < 0 or posicion_serpiente_x >= ANCHO or 
            posicion_serpiente_y < 0 or posicion_serpiente_y >= ALTO or 
            colision_con_cuerpo(cabeza_serpiente, segmentos_serpiente)):
            game_over_sonido.play()  # Reproducir sonido de Game Over
            mostrar_game_over(puntuacion)
            break

        # Mostrar la puntuación
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
        ventana.blit(texto_puntuacion, (10, 10))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        reloj.tick(velocidad_juego)  # Aumentar la velocidad según la puntuación

# Función principal
def main():
    while True:
        mostrar_pantalla_inicio()
        juego()

# Ejecutar el juego
main()
pygame.quit()
