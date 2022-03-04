# Import and initalize pygame
import pygame
import sys
pygame.init()

# Main window
screen = pygame.display.set_mode()

# Game loop
while True:
    # Event listner loop
    for event in pygame.event.get():
        # Check if user exits window (clicks 'x' top right)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update main window
    pygame.display.flip()
