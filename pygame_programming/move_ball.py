# Install pygame (at school 2023): py -m pip install pygame
# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

# Set up variables and the drawing window
base_speed = 2
speed_x = 2
speed_y = 2
scr_width = 800
scr_len = 800
screen = pygame.display.set_mode([scr_width, scr_len])
w = scr_width/2 # x coordinate
h = scr_width/2 # y coordinate
x = w
y = h
# Run until the user asks to quit
running = True
while running:
    pygame.time.delay(50)
    x += speed_x
    y += speed_y
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Direction?
            if event.key == K_DOWN:
                speed_y = base_speed
                speed_x = 0
            elif event.key == K_UP:
                speed_y = -base_speed
                speed_x = 0
            elif event.key == K_LEFT:
                speed_y = 0
                speed_x = -base_speed
            elif event.key == K_RIGHT:
                speed_y = 0
                speed_x = base_speed
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill((100, 255, 100))

    # Draw a solid circle in the center
    pygame.draw.circle(screen, (255, 0, 255), (x, y), 20)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
