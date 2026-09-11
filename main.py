import pygame

# Initialize pygame module
pygame.init()

# Set up game window
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Cats and Hogs")

# Set up game loop
clock = pygame.time.Clock()
dt = 0
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lightblue4")
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()