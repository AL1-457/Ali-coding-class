import pygame

# Initialize required modules 
pygame.init()
white = (255, 255, 255)

# Clock
clock =pygame.time.Clock()

# creating the display surface object of specific dimension..e(X, Y)
display_surface = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption('Image')

# creating asurface object, image is drawn on it.
image = pygame.image.load('L33/turtle.jpeg')

# set the size for the image
DEFAULT_IMAGE_SIZE = (150,150)

# scale the image to your needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

#set a default position
DEFAULT_IMAGE_POSITION = (150,150)

# infinite loop
while True:
    display_surface.fill(white)
    display_surface.blit(image, DEFAULT_IMAGE_POSITION)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # quit the program.
            quit()

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)