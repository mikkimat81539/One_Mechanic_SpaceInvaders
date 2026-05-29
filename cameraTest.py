# THIS FILE IS TO LEARN HOW TO IMPLEMENT CAMERA FOR GAMEPLAY
# In most Pygame projects, the screen is not the world itself. It’s more like a window (viewport) into a larger game world.

import pygame

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen_w = 500
screen_h = 300

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Camera Test")

# BACKGROUND IMAGE
img = pygame.image.load("image5.jpg").convert_alpha()


# CAMERA CLASS
class Camera:
	def __init__(self, player):
		pass


# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	screen.blit(img, (0, 0))
	
	pygame.display.update()

pygame.quit()
