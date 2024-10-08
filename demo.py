import pygame
import random

#init pygame instance
pygame.init()

#setting up the game window

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

green = (0, 128, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
game_over = False
score = 0

x1 = window_width / 2
y1 = window_height / 2

x1_change = 0
y1_change = 0

snake_body = []
length_of_snake = 1

foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
foody = round(random.randrange(0, window_height - 10) / 10) * 10.0


clock = pygame.time.Clock() #Object method to set the framerate

#game loop logic
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #check for arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = +10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = +10

    x1 = x1 + x1_change
    y1 = y1 + y1_change
#create game boundaries
    if x1 >= window_width or x1< 0 or y1 >= window_height or y1< 0:
        game_over = True
    window.fill(black) # to refresh the background
    #write logic outside of the for loop
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_body.append(snake_head)

    #logic fto keep from drawing snake body indefinitely
    if len(snake_body) > length_of_snake:
        del snake_body[0]
    #logic for snake hitting itself
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True
    font_style = pygame.font.SysFont(None, 50)
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])
    #EAT FOOD LOGIC check if the snake and food is in the same
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, window_width - 10) / 10) * 10.0
        foody = round(random.randrange(0, window_height - 10) / 10) * 10.0
        length_of_snake += 1
        score += 1
    pygame.draw.rect(window, red, [foodx, foody, 10, 10])
    #loop through list for body logic
    for segment in snake_body:
        pygame.draw.rect(window, green, [segment[0], segment[1], 10, 10])
    # print(snake_body)
    # pygame.draw.rect(window, green, [x1, y1, 10, 10]) #400 and 300 are where the snake begins in centerpoint. 10, 10 is the size of pixel
    #need to call update for snake to show on window
    pygame.display.update()
    clock.tick(24) #set framerate