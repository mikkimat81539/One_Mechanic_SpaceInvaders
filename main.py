import pygame, asyncio

pygame.init()

async def main():
	# CLOCK
	clock = pygame.time.Clock()

	# SCREEN
	screen_w = 800
	screen_h = 600

	screen = pygame.display.set_mode((screen_w, screen_h))


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
			self.speed = 10
			self.dx, self.dy = 1, 0
		

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
			if self.rect.x > 785:
				self.rect.x -= self.speed
			if self.rect.x < 5:
				self.rect.x += self.speed

			if self.rect.y > 585:
				self.rect.y -= self.speed
			if self.rect.y < 5:
				self.rect.y += self.speed

	# AMMO CLASS	
	class Ammo(Objects):
		def __init__(self, x_pos, y_pos, width, height, color, dx, dy):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((0, 0), (self.width, self.height))
			self.rect.center = (self.x_pos, self.y_pos)
			self.speed = 15 
		
			self.dx = dx
			self.dy = dy

		# DRAW AMMO
		def drawAmmo(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)

		def moveAmmo(self):
			self.rect.x += self.dx * self.speed
			self.rect.y += self.dy * self.speed



	# ENEMY CLASS
	class Enemy(Objects):
		def __init__(self, x_pos, y_pos, width, height, color):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))
			self.speed = 0


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
	player = Player(10, 10, 10, 10, "black")

	# AMMO
	ammoList = []

	def move(player):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]:
			player.dx, player.dy = -1, 0

		elif keys[pygame.K_RIGHT]:
			player.dx, player.dy = 1, 0

		elif keys[pygame.K_UP]:
			player.dx, player.dy = 0, -1

		elif keys[pygame.K_DOWN]:
			player.dx, player.dy = 0, 1

	def shoot(player, ammoList):
		ammo = Ammo(player.rect.centerx, player.rect.centery, 5, 5, "red", player.dx, player.dy)
		ammoList.append(ammo)

	# ENEMY
	enemy = Enemy(5, 100, 30, 30, "green")


	# COLLISION
	def collisions(player, enemy):
		collide = enemy.rect.colliderect(player.rect) # Player colliding with enemy

		if collide:
			enemy.color = "orange"
		else:
			enemy.color = "green"

	# MAIN LOOP
	running = True

	while running:
		move(player)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

#			if event.type == pygame.KEYDOWN:
#				if event.key == pygame.K_SPACE:
#					shoot(player, ammoList)

		screen.fill("white")

		# Player Movement
		player.movePlayer()


		# AMMO SHOT
		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE]:
			shoot(player, ammoList)

		# Ammo Movement
		for i in ammoList:
			i.moveAmmo()
			i.drawAmmo(screen)

			if i.rect.colliderect(enemy.rect): # ammo hitting enemy
				enemy.color = "brown"

		# Enemy Movement
		enemy.moveEnemy(player)

		# Collision call for player
		collisions(player, enemy)

		# DRAW OBJECTS
		player.drawPlayer(screen)
		
		enemy.drawEnemy(screen)

		pygame.display.update()

		clock.tick(60)

		await asyncio.sleep(0)

asyncio.run(main())
