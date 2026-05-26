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
#			self.moving_left = False
#			self.moving_right = False
#			self.moving_up = False
#			self.moving_down = False

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
			if self.rect.x > 475:
				self.rect.x -= self.speed
			if self.rect.x < 5:
				self.rect.x += self.speed

			if self.rect.y > 275:
				self.rect.y -= self.speed
			if self.rect.y < 5:
				self.rect.y += self.speed
	
	class Ammo(Objects):
		def __init__(self, x_pos, y_pos, width, height, color, dx, dy):
			super().__init__(x_pos, y_pos, width, height, color)
			self.rect = pygame.Rect((0, 0), (self.width, self.height))
			self.rect.center = (self.x_pos, self.y_pos)
			self.speed = 5 
		
			self.dx = dx
			self.dy = dy

		# DRAW AMMO
		def drawAmmo(self, surface):
			pygame.draw.rect(surface, self.color, self.rect)

		def moveAmmo(self):
			self.rect.x += self.dx * self.speed
			self.rect.y += self.dy * self.speed
				
	# PLAYER
	player = Player(10, 10, 20, 20, "black")

	# AMMO

	ammoList = []

	def move(player):
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]: player.dx, player.dy = -1, 0
		elif keys[pygame.K_RIGHT]: player.dx, player.dy = 1, 0
		elif keys[pygame.K_UP]: player.dx, player.dy = 0, -1
		elif keys[pygame.K_DOWN]: player.dx, player.dy = 0, 1

	def shoot(player, ammoList):
		ammo = Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red", player.dx, player.dy)
		ammoList.append(ammo)

#		if player.moving_left:
#			ammo = Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red", -1, 0)
#			ammoList.append(ammo)
#
#		elif player.moving_right:
#			ammo = Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red", 1, 0)
#			ammoList.append(ammo)
#
#		elif player.moving_up:
#			ammo = Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red", 0, -1)
#			ammoList.append(ammo)
#
#		elif player.moving_down:
#			ammo = Ammo(player.rect.centerx, player.rect.centery, 10, 10, "red", 0, 1)
#			ammoList.append(ammo)


	# MAIN LOOP
	running = True

	while running:
		move(player)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					shoot(player, ammoList)

		screen.fill("white")

		# Player Movement
		player.movePlayer()


		# Ammo Movement
		for i in ammoList:
			i.moveAmmo()

		# DRAW OBJECTS
		for i in ammoList:
			i.drawAmmo(screen)

		player.drawPlayer(screen)
		
		pygame.display.update()

		clock.tick(60)

		await asyncio.sleep(0)

asyncio.run(main())
