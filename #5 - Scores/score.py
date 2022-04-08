# Import and initalize pygame
import pygame
import sys
import random
pygame.init()
pygame.font.init()

# Main window
screen = pygame.display.set_mode((500, 400))

# Create font
pixel_font = pygame.font.Font("#5 - Scores/pixel.ttf", 32)

# Game data
paddleUp = False
paddleDown = False
paddle_x = 20
paddle_y = 200
paddle_rect = pygame.Rect(paddle_x, paddle_y, 25, 100)

ai_x = 455
ai_y = 200
ai_rect = pygame.Rect(ai_x, ai_y, 25, 100)

ball_x = 100
ball_y = 200
x_dir = 1
y_dir = 1

# Score variables
player_score = 0
ai_score = 0
player_score_display = pixel_font.render(str(player_score), True, (255,255,255), None)
ai_score_display = pixel_font.render(str(ai_score), True, (255,255,255), None)

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

    ball_x += 0.1 * x_dir
    ball_y += 0.1 * y_dir

    # Updating user paddle
    if paddleUp:
        paddle_y -= 0.2

    if paddleDown:
        paddle_y += 0.2

    paddle_rect.update(paddle_x, paddle_y, 25, 100)

    # Update ai paddle
    if y_dir < 0 and ai_y > 0: 
        ai_y -= 0.05
    
    if y_dir > 0 and ai_y + 100 < 400:
        ai_y += 0.05
    
    ai_rect.update(ai_x, ai_y, 25, 100)

    # Edge of paddle
    if paddle_rect.collidepoint(ball_x - 10, ball_y) or paddle_rect.collidepoint(ball_x + 10, ball_y):
        x_dir *= -1

    # Edge of paddle
    if ai_rect.collidepoint(ball_x - 10, ball_y) or ai_rect.collidepoint(ball_x + 10, ball_y):
        x_dir *= -1

    # Edges of screen
    if ball_x + 10 > 500:
        x_dir *= -1
        player_score += 1
        player_score_display = pixel_font.render(str(player_score), True, (255,255,255), None)
        ball_x = 250
        ball_y = 200
        x_dir *= random.choice([-1, 1])
        y_dir *= random.choice([-1, 1])

    if ball_x - 10 < 0:
        x_dir *= -1
        ai_score += 1
        ai_score_display = pixel_font.render(str(ai_score), True, (255,255,255), None)
        ball_x = 250
        ball_y = 200
        x_dir *= random.choice([-1, 1])
        y_dir *= random.choice([-1, 1])

    if ball_y - 10 < 0:
        y_dir *= -1

    if ball_y + 10 > 400:
        y_dir *= -1

    # draw paddle and ball to screen
    pygame.draw.rect(screen, (255, 255, 255), paddle_rect)
    pygame.draw.rect(screen, (255, 255, 255), ai_rect)
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)

    # draw score to screen
    screen.blit(player_score_display, (220, 15))
    screen.blit(ai_score_display, (280, 15))

    # Update main window
    pygame.display.flip()
