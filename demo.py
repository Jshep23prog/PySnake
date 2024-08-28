import pygame

#init pygame instance
pygame.init()

#setting up the game window

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

green = (0, 128, 0)
game_over = False


#game loop logic
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #write logic outside of the for loop
    pygame.draw.rect(window, green, [400, 300, 10, 10]) #400 and 300 are where the snake begins in centerpoint. 10, 10 is the size of pixel
    #need to call update for snake to show on window
    pygame.display.update()