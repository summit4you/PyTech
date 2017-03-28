import pygame, sys


# A sprite should be a class, which have some member,
# image
# rect

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


if __name__ == '__main__':
	pygame.init()
	screen=pygame.display.set_mode([640,480])
	screen.fill([255,255,255])
	b=Block([255,0,0],100,100,[50,100])
	screen.blit(b.image,b.rect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()

