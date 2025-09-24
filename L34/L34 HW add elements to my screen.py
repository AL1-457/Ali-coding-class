import pygame

pygame.init()
# Create the display surface object of specific dimension.
screen = pygame.display.set_mode((400, 400))

# Fill the screen with white color
screen.fill((255, 255, 255))

# Define colors
BLUE = (255, 175, 100)

# Draw solid circle
pygame.draw.circle(screen, BLUE, (300, 300), 50)

# Draw outlined circle
pygame.draw.circle(screen, BLUE, (100,100), 50, 3)

#draw rectangle
pygame.draw.rect(screen,(0,255,255), pygame.Rect(190,70,100,60))

pygame.display.flip() 

# Draws the surface object to the screen.
pygame.display.update()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()