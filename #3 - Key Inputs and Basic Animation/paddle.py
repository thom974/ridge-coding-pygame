# Import and initalize pygame
from operator import truediv
import pygame
import sys
pygame.init()

# Main window
screen = pygame.display.set_mode((500,400))

# Game data 
paddle_x = 20
paddle_y = 20
paddleUp = False
paddleDown = False

ball_x = 250
ball_y = 200

# Game loop
while True:
    # Event listner loop
    for event in pygame.event.get():
        # Check if user exits window (clicks 'x' top right)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddleUp = True
            if event.key == pygame.K_DOWN:
                paddleDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddleUp = False
            if event.key == pygame.K_DOWN:
                paddleDown = False

    # Clear the screen
    screen.fill((0,0,0))

    # Game code
    if paddleUp:
        paddle_y -= 0.1
    
    if paddleDown: 
        paddle_y += 0.1

    # Draw paddle
    pygame.draw.rect(screen, (255,0,0), (paddle_x, paddle_y, 25, 100))

    # Draw ball
    pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), 10)

    # Update main window
    pygame.display.flip()
