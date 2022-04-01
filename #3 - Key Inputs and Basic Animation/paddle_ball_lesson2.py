# Import and initalize pygame
import pygame
import sys
pygame.init()

# Main window
screen = pygame.display.set_mode((500, 400))

# Game data
paddle_x = 200
paddle_y = 200
paddleUp = False
paddleDown = False

ball_x = 100
ball_y = 200
x_dir = 1
y_dir = 1

# Game loop
while True:
    # Clear the screen
    screen.fill((0, 0, 0))

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

    ball_x += 2 * x_dir
    ball_y += 2 * y_dir

    if paddleUp:
        paddle_y -= 0.5

    if paddleDown:
        paddle_y += 0.5

    if ball_x + 10 > 500:
        x_dir *= -1

    if ball_x - 10 < 0:
        x_dir *= -1

    if ball_y - 10 < 0:
        y_dir *= -1

    if ball_y + 10 > 400:
        y_dir *= -1

    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, paddle_y, 25, 100))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)

    # Update main window
    pygame.display.flip()
