import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
ROJO = (255, 0, 0)

# Tamaño de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Tipo Mario Bros")

# Configuración del reloj
reloj = pygame.time.Clock()

# Clase del jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = ALTO - 150
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.saltando = False
        self.vidas = 3

    def update(self):
        # Gravedad
        self.velocidad_y += 1
        if self.velocidad_y > 10:
            self.velocidad_y = 10

        # Movimiento horizontal
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Colisión con el suelo
        if self.rect.y >= ALTO - 50:
            self.rect.y = ALTO - 50
            self.saltando = False
            self.velocidad_y = 0

    def saltar(self):
        if not self.saltando:  # Solo permitir saltar si no está saltando
            self.velocidad_y = -15
            self.saltando = True

# Clase de plataformas
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Clase de objetos coleccionables
class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Clase de enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = random.choice([-3, 3])  # Movimiento aleatorio hacia la izquierda o derecha

    def update(self):
        self.rect.x += self.velocidad_x
        # Cambiar dirección al chocar con los bordes
        if self.rect.x <= 0 or self.rect.x >= ANCHO - self.rect.width:
            self.velocidad_x *= -1

# Crear grupos de sprites
todos_los_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
objetos = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

# Crear el jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Crear plataformas
plataforma1 = Plataforma(0, ALTO - 50, ANCHO, 50)
plataforma2 = Plataforma(300, 400, 200, 20)
plataforma3 = Plataforma(600, 300, 200, 20)
plataforma4 = Plataforma(1000, 350, 200, 20)
plataforma5 = Plataforma(1300, 450, 200, 20)

plataformas.add(plataforma1, plataforma2, plataforma3, plataforma4, plataforma5)
todos_los_sprites.add(plataforma1, plataforma2, plataforma3, plataforma4, plataforma5)

# Crear objetos coleccionables
objeto1 = Objeto(400, 350)
objeto2 = Objeto(800, 250)
objeto3 = Objeto(1200, 400)

objetos.add(objeto1, objeto2, objeto3)
todos_los_sprites.add(objeto1, objeto2, objeto3)

# Crear enemigos
enemigo1 = Enemigo(500, ALTO - 100)
enemigo2 = Enemigo(1000, ALTO - 100)

enemigos.add(enemigo1, enemigo2)
todos_los_sprites.add(enemigo1, enemigo2)

# Inicializar puntuación
puntuacion = 0
fuente = pygame.font.SysFont(None, 36)

# Bucle principal del juego
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.velocidad_x = -5
            if evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 5
            if evento.key == pygame.K_SPACE:
                jugador.saltar()  # Llamar al método de salto

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 0

    # Actualizar sprites
    todos_los_sprites.update()

    # Colisiones con plataformas
    if pygame.sprite.spritecollide(jugador, plataformas, False):
        jugador.rect.y = plataformas.sprites()[0].rect.top - jugador.rect.height
        jugador.velocidad_y = 0
        jugador.saltando = False

    # Colisiones con objetos
    objetos_recogidos = pygame.sprite.spritecollide(jugador, objetos, True)
    puntuacion += len(objetos_recogidos)

    # Colisiones con enemigos
    if pygame.sprite.spritecollide(jugador, enemigos, False):
        jugador.vidas -= 1
        if jugador.vidas <= 0:
            print("Game Over")
            ejecutando = False  # Terminar el juego

    # Limpiar la ventana
    ventana.fill(NEGRO)

    # Dibujar todos los sprites
    todos_los_sprites.draw(ventana)

    # Mostrar la puntuación
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    ventana.blit(texto_puntuacion, (10, 10))

    # Mostrar vidas
    texto_vidas = fuente.render(f"Vidas: {jugador.vidas}", True, BLANCO)
    ventana.blit(texto_vidas, (10, 40))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(60)

# Salir de Pygame
pygame.quit()
