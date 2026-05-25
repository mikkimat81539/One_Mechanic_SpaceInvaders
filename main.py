import pygame, asyncio

pygame.init()

async def main():
	# CLOCK
	clock = pygame.time.Clock()

	# SCREEN
	screen = pygame.display.set_mode((500, 300))

	# OBJECT CLASS
	class Objects:
		def __init__(self, x_pos, y_pos, width, height, color):
			self.x_pos = x_pos
			self.y_pos = y_pos
			self.width = width
			self.height = height
			self.color = color

	# PLAYER CLASS
	class Player(Objects):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))
			self.speed = 5

		# DRAW PLAYER
		def drawPlayer(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)

		def movePlayer(self):
			# PLAYER KEY INPUTS
			key = pygame.key.get_pressed()

			if key[pygame.K_RIGHT]:
				self.rect.x += self.speed

			if key[pygame.K_DOWN]:
				self.rect.y += self.speed

			if key[pygame.K_UP]:
				self.rect.y -= self.speed

			if key[pygame.K_LEFT]:
				self.rect.x -= self.speed

			# PLAYER BORDERS
			if self.rect.x > 475:
				self.rect.x -= self.speed
			if self.rect.x < 5:
				self.rect.x += self.speed

			if self.rect.y > 275:
				self.rect.y -= self.speed
			if self.rect.y < 5:
				self.rect.y += self.speed
	
	class Ammo(Objects):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((0, 0), (self.width, self.height))
			self.rect.center = (x_pos, y_pos)
			self.speed = 5

		def drawAmmo(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)
		
		def shootAmmo(self):
			pass

	# PLAYER
	player = Player(10, 10, 20, 20, "black")

	# AMMO

	ammo = Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red")

	# MAIN LOOP
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill("white")

		# Player Movement
		player.movePlayer()

		# DRAW OBJECTS
		player.drawPlayer(screen)

		ammo.drawAmmo(screen)

		pygame.display.update()

		clock.tick(60)

		await asyncio.sleep(0)

asyncio.run(main())
