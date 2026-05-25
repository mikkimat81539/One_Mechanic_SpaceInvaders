import pygame, asyncio

pygame.init()

async def main():
	# CLOCK
	clock = pygame.time.Clock()

	# SCREEN
	screen_w = 800
	screen_h = 600

	screen = pygame.display.set_mode((screen_w, screen_h))
	pygame.display.set_caption("Chase and Shoot")


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
			if self.rect.x > screen_w - 25:
				self.rect.x -= self.speed
			if self.rect.x < 5:
				self.rect.x += self.speed

			if self.rect.y > screen_h - 25:
				self.rect.y -= self.speed
			if self.rect.y < 5:
				self.rect.y += self.speed
	# AMMO CLASS
	class Ammo(Objects):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((0, 0), (self.width, self.height))
			self.rect.center = (self.x_pos, self.y_pos)
			self.speed = 3

		# DRAW AMMO
		def drawAmmo(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)

	# ENEMY CLASS
	class Enemy(Objects):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))
			self.speed = 3


		def drawEnemy(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)


		def moveEnemy(self, player):
			playerVector = pygame.math.Vector2(player.rect.x, player.rect.y)
			enemyVector = pygame.math.Vector2(self.rect.x, self.rect.y)

			# direction from enemy to player
			direction = playerVector - enemyVector			

			# prevent division by zero 
			if direction.length() != 0:
				direction = direction.normalize()

			self.rect.x += direction.x * self.speed
			self.rect.y += direction.y * self.speed


	
	# PLAYER
	player = Player(150, 10, 20, 20, "black")

	# AMMO
	ammoList = []

	# ENEMY
	enemy = Enemy(5, 100, 50, 50, "green")

	# MAIN LOOP
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					ammoList.append(Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red"))

		screen.fill("white")

		# Player Movement
		player.movePlayer()

		# Ammo Movement
		for i in ammoList:
			i.rect.x += i.speed

		# Enemy Movement
		enemy.moveEnemy(player)

		# DRAW OBJECTS
		player.drawPlayer(screen)

		enemy.drawEnemy(screen)

		for i in ammoList:
			i.drawAmmo(screen)

		pygame.display.update()

		clock.tick(60)

		await asyncio.sleep(0)

asyncio.run(main())
