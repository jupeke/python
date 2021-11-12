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

# Set up the drawing window
scr_width = 800
scr_len = 800
screen = pygame.display.set_mode([scr_wid, scr_len])
w = scr_width/2 # x coordinate
y = scr_width/2 # y coordinate
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Direction?
            if event.key == K_DOWN:
                running = False
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill((100, 255, 100))

    # Draw a solid circle in the center
    pygame.draw.circle(screen, (255, 0, 255), (w, h), 20)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
