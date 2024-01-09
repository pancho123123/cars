import pygame, random
from random import randint
from pathlib import Path

WIDTH = 800
HEIGHT = 650
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
GREEN2 = (133,21,35)
RED = (255,0,0)
BLUE = (0,0,255)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cars")
clock = pygame.time.Clock()
current_path = Path.cwd()
file_path = current_path / 'highscore.txt'

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_gas_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("img/car1.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 50
		self.rect.centery = HEIGHT // 2
		self.speed_x = 0
		self.shield = 100
		self.gas = 100
		self.score = 0

	def update(self):
		self.shield += 1/24
		self.gas -= 1/20
		if self.gas < 0:
			self.gas = 0
		if self.gas > 100:
			self.gas = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -7
		if keystate[pygame.K_d]:
			self.speed_x = 7
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -7
		if keystate[pygame.K_s]:
			self.speed_y = 7
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 60:
			self.rect.top = 60
		if self.rect.bottom > 570:
			self.rect.bottom = 570
		if self.shield > 100:
			self.shield = 100

class Cars(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = random.choice(cars_images)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3//2 )
		self.nu_list = [80, 210, 340, 470]
		self.rect.y = random.choice(self.nu_list)
		self.speedy = 0
		self.speedx = randint(-8,-3)
		
    
	def update(self):
		
		self.rect.x += self.speedx
		
		if self.rect.left < -self.rect.width:
			self.image = random.choice(cars_images)
			self.image.set_colorkey(WHITE)
			self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3//2 )
			self.rect.y = random.choice(self.nu_list)
			
			self.speedy = randint(-8,-3)

class Gas(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = gas_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3//2 )
		self.ng_list = [120, 250, 380, 510]
		self.rect.y = random.choice(self.ng_list)
		self.speedy = 0
		self.speedx = -5
		
    
	def update(self):
		
		self.rect.x += self.speedx
		
		if self.rect.left < -self.rect.width:
			
			self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3//2 )
			self.rect.y = random.choice(self.ng_list)
			
			self.speedy = -5

class Gold(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = random.choice(gold_images)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3//2 )
		self.ngo_list = [110, 240, 370, 500]
		self.rect.y = random.choice(self.ngo_list)
		self.speedy = 0
		self.speedx = -5
		
    
	def update(self):
		
		self.rect.x += self.speedx
		
		if self.rect.left < -self.rect.width:
			
			self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH * 3//2 )
			self.rect.y = random.choice(self.ngo_list)
			
			self.speedy = -5

class Objects1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(obj_images)
		self.image.set_colorkey(GREEN2)
		self.rect = self.image.get_rect()
		self.rect.x = randint((WIDTH + self.rect.width),(WIDTH *2))
		self.nva_list = [0,1,2,3,4,5]
		self.rect.y = random.choice(self.nva_list)
		
		self.speedy = 0
		self.speedx = -5

	def update(self):
		
		self.rect.x += self.speedx
		if self.rect.left < -self.rect.width:
			self.image = random.choice(obj_images)
			self.image.set_colorkey(GREEN2)
			self.rect.x = randint((WIDTH + self.rect.width),(WIDTH * 2))
			self.rect.y = random.choice(self.nva_list)
			
			self.speedx = -5

class Objects2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(obj_images)
		self.image.set_colorkey(GREEN2)
		self.rect = self.image.get_rect()
		self.rect.x =randint((WIDTH + self.rect.width),(WIDTH * 2))
		self.nvb_list = [585, 586, 587, 588, 589, 590]
		self.rect.y = random.choice(self.nvb_list)
		
		self.speedy = 0
		self.speedx = -5

	def update(self):
		
		self.rect.x += self.speedx
		if self.rect.left < -self.rect.width:
			self.image = random.choice(obj_images)
			self.image.set_colorkey(GREEN2)
			self.rect.x = randint((WIDTH + self.rect.width),(WIDTH * 2))
			self.rect.y = random.choice(self.nvb_list)
			
			self.speedx = -5

class Objects3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(obj_images)
		self.image.set_colorkey(GREEN2)
		self.rect = self.image.get_rect()
		self.rect.x = randint((WIDTH + self.rect.width),(WIDTH * 2))
		self.nva_list = [0,1,2,3,4,5]
		self.rect.y = random.choice(self.nva_list)
		
		self.speedy = 0
		self.speedx = -5

	def update(self):
		
		self.rect.x += self.speedx
		if self.rect.left < -self.rect.width:
			self.image = random.choice(obj_images)
			self.image.set_colorkey(GREEN2)
			self.rect.x = randint((WIDTH + self.rect.width),(WIDTH + 3 * self.rect.width))
			self.rect.y = random.choice(self.nva_list)
			
			self.speedx = -5

class Objects4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(obj_images)
		self.image.set_colorkey(GREEN2)
		self.rect = self.image.get_rect()
		self.rect.x =randint((WIDTH + self.rect.width),(WIDTH * 2))
		self.nvb_list = [585, 586, 587, 588, 589, 590]
		self.rect.y = random.choice(self.nvb_list)
		
		self.speedy = 0
		self.speedx = -5

	def update(self):
		
		self.rect.x += self.speedx
		if self.rect.left < -self.rect.width:
			self.image = random.choice(obj_images)
			self.image.set_colorkey(GREEN2)
			self.rect.x = randint((WIDTH + self.rect.width),(WIDTH * 2))
			self.rect.y = random.choice(self.nvb_list)
			
			self.speedx = -5

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

def show_go_screen():
	
	screen.blit(background, [0,0])
	draw_text1(screen, "Cars", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Esquiva vehiculos, colecta bidones de bencina y oro", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	draw_text1(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def get_high_score():
	with open(file_path,'r') as file:
		return file.read()

def show_game_over_screen():
	screen.blit(background, [0,0])
	if highest_score <= player.score:
		draw_text1(screen, "¡high score!", 60, WIDTH  // 2, HEIGHT * 1/4)
		draw_text1(screen, "score: "+str(player.score), 30, WIDTH // 2, HEIGHT // 2)
		draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 4/5)
	else:
		draw_text1(screen, "score: "+str(player.score), 60, WIDTH // 2, HEIGHT * 1/3)
		draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 2/3)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

####----------------EXPLOSTION IMAGENES --------------
explosion_anim = []
for i in range(9):
	file = "img/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)

cars_images = []
cars_list = ["img/car2.png", "img/car3.png", "img/car4.png", "img/car5.png",
				"img/truck1.png", "img/truck2.png", "img/truck3.png"]

for img in cars_list:
	cars_images.append(pygame.image.load(img).convert())

obj_images = []
obj_list = ["img/tronco1.png", "img/piedra1.png", "img/piedra2.png", "img/piedra3.png",
				"img/agua1.png", "img/arbol1.png", "img/pasto1.png", "img/pasto2.png",
			"img/pasto3.png"]

for img in obj_list:
	obj_images.append(pygame.image.load(img).convert())

gold_images = []
gold_list = ["img/gol.png", "img/gold.png"]

gas_images = []
gas_list = ["img/gas.png"]
for img in gold_list:
	gold_images.append(pygame.image.load(img).convert())

for img in gas_list:
	gas_images.append(pygame.image.load(img).convert())

# Cargar imagen de fondo
fnd_images = []
fnd_list = ["img/fond11.png", "img/fond22.png"]# "img/fond3.png", "img/fond4.png",]

for img in fnd_list:
	fnd_images.append(pygame.image.load(img).convert())
background = random.choice(fnd_images)
#background = pygame.image.load("img/fond1.png").convert()
### high score

try:
	highest_score = int(get_high_score())
except:
	highest_score = 0



game_over = False
running = True
start = True
while running:
	
	screen.blit(background, [0,0])
	if game_over:

		show_game_over_screen()

		game_over = False
		#backgound = random.choice(fnd_images)
		all_sprites = pygame.sprite.Group()
		cars_list = pygame.sprite.Group()
		obj_list = pygame.sprite.Group() 
		gas_list = pygame.sprite.Group()
		gold_list = pygame.sprite.Group()
		player = Player()
		all_sprites.add(player)
		
		for i in range(4):
			car = Cars()
				
			all_sprites.add(car)
			cars_list.add(car)
			
		
		for i in range(randint(8,9)):
			obj1 = Objects1()
			obj2 = Objects2()
			obj3 = Objects3()
			obj4 = Objects4()
		
			all_sprites.add(obj1, obj2, obj3, obj4)
			obj_list.add(obj1, obj2, obj3, obj4) 
		
		for i in range (randint(1,1)):
			gas = Gas()
			all_sprites.add(gas)
			gas_list.add(gas)

		for i in range (randint(1,1)):
			gold = Gold()
			all_sprites.add(gold)
			gold_list.add(gold)
		player.score = 0

	if start:

		show_go_screen()

		start = False
		backgound = random.choice(fnd_images)
		all_sprites = pygame.sprite.Group()
		cars_list = pygame.sprite.Group()
		obj_list = pygame.sprite.Group() 
		gas_list = pygame.sprite.Group()
		gold_list = pygame.sprite.Group()
		player = Player()
		all_sprites.add(player)
		
		for i in range(4):
			car = Cars()
				
			all_sprites.add(car)
			cars_list.add(car)
			
		
		for i in range(randint(8,9)):
			obj1 = Objects1()
			obj2 = Objects2()
			obj3 = Objects3()
			obj4 = Objects4()
		
			all_sprites.add(obj1, obj2, obj3, obj4)
			obj_list.add(obj1, obj2, obj3, obj4) 
		
		for i in range (randint(1,1)):
			gas = Gas()
			all_sprites.add(gas)
			gas_list.add(gas)

		for i in range (randint(1,1)):
			gold = Gold()
			all_sprites.add(gold)
			gold_list.add(gold)
		player.score = 0
		


	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		

	backgound = random.choice(fnd_images)
	all_sprites.update()

	# limite barra gas
	if player.gas < 1/100:
		game_over = True

	# checar si autos pasan el limite izq sumar score
	if car.rect.left < -car.rect.width + 10:
		player.score += 30
	
	# Checar colisiones - jugador - gas
	hits = pygame.sprite.spritecollide(player, gas_list, True)
	for hit in hits:
		
		player.gas += randint(20,40)
		player.score += 50
		gas = Gas()
		all_sprites.add(gas)
		gas_list.add(gas)

	
	# Checar colisiones - jugador - gold
	hits = pygame.sprite.spritecollide(player, gold_list, True)
	for hit in hits:
		
		
		player.score += randint(50,100)
		gold = Gold()
		all_sprites.add(gold)
		gold_list.add(gold)
	
	# Checar colisiones - jugador - cars
	hits = pygame.sprite.spritecollide(player, cars_list, True)
	for hit in hits:
		
		player.shield -= 25
		player.score -= 20
		car = Cars()
		
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)
		all_sprites.add(car)
		cars_list.add(car)
		
		if player.shield <= 0:
			game_over = True

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	
	draw_text1(screen, str(player.score), 25, WIDTH // 2, 10)
	
	# Escudo.
	
	draw_shield_bar(screen, 5, 5, player.shield)
	draw_text2(screen, str(int(player.shield)) + "/100", 10, 55, 6)
	draw_gas_bar(screen, 5, 20, player.gas)
	draw_text1(screen, str(int(player.gas)) + "/100", 10, 55, 21)

	pygame.display.flip()
pygame.quit()	