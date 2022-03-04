# Import and initalize pygame
import pygame
import sys
pygame.init()

# Main window
screen = pygame.display.set_mode((520, 520))

# Game loop
while True:
    # Event listner loop
    for event in pygame.event.get():
        # Check if user exits window (clicks 'x' top right)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game code
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 50, 50))

    # Update main window
    pygame.display.flip()
