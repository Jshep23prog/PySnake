import pygame

#init pygame instance
pygame.init()

#setting up the game window

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

green = (0, 128, 0)
black = (0, 0, 0)
game_over = False

x1 = window_width / 2
y1 = window_height / 2
x1_change = 0
y1_change = 0

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
    window.fill(black) # to refresh the background
    #write logic outside of the for loop
    pygame.draw.rect(window, green, [x1, y1, 10, 10]) #400 and 300 are where the snake begins in centerpoint. 10, 10 is the size of pixel
    #need to call update for snake to show on window
    pygame.display.update()