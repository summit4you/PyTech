import pygame, sys


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height, initial_position):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.topleft = initial_position


# A sprite should be a class, which have some member,
# image
# rect

class Cat(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
	def __init__(self, target):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.target=target
		self.image = None
		self.master_image = None
		self.sub_rect = None
		self.master_rect = None
		self.rect = None
		self.topleft = 0,0
		self.frame = 0
		self.old_frame = -1
		self.frame_width = 1
		self.frame_height = 1
		self.first_frame = 0
		self.last_frame = 0
		self.columns = 1
		self.last_time = 0
		self.speed = 10



	def load(self, filename, width, height, columns):
		self.master_image = pygame.image.load(filename).convert_alpha()
		self.frame_width = width
		self.frame_height = height
		self.sub_rect = 0,0,width,height
		self.columns = columns  # how much columns in image
		self.master_rect = self.master_image.get_rect()
		self.last_frame = (self.master_rect.width // width) * (self.master_rect.height // height) - 1 # how much frame in image
		# set first image
		self.frame = 0
		self.old_frame = -1
		frame_x = (self.frame % self.columns) * self.frame_width
		frame_y = (self.frame // self.columns) * self.frame_height
		cliprect = ( frame_x, frame_y, self.frame_width, self.frame_height )
		self.image = self.master_image.subsurface(cliprect) # get the sub-image
		self.old_frame = self.frame
		self.rect = self.image.get_rect()

	def move_right(self):
		self.rect.right=self.rect.right+10
		if self.rect.right>self.target.get_width():
			self.rect.right=self.target.get_width()


	
	def update(self, current_time, rate=60):
		if current_time > self.last_time + rate:
			self.frame += 1
			if self.frame > self.last_frame: # reach last frame?
				self.frame = self.first_frame # return to beginning
			self.last_time = current_time

		if self.frame != self.old_frame:
			frame_x = (self.frame % self.columns) * self.frame_width
			frame_y = (self.frame // self.columns) * self.frame_height
			rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
			self.image = self.master_image.subsurface(rect) # get the sub-image
			self.old_frame = self.frame




if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((800,600),0,32)
	pygame.display.set_caption("Test")
	font = pygame.font.Font(None, 18)
	framerate = pygame.time.Clock()
	cat = Cat(screen)
	cat.load("sprite.png", 100, 100, 4)
	group = pygame.sprite.Group()
	group.add(cat)
	b=Block([255,0,0],100,100,[600,0])
	group.add(b)
	while True:
		framerate.tick(30)
		ticks = pygame.time.get_ticks()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					cat.move_right()

		if pygame.sprite.collide_circle(cat, b):
			pygame.display.set_caption("touch")

		key = pygame.key.get_pressed()
		if key[pygame.K_ESCAPE]:
			exit()

		screen.fill((0,0,100))

		group.update(ticks)
		group.draw(screen)
		pygame.display.update()





