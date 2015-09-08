#Guided introduction to pygame with Greymerk on YouTube
#Introduction to classes and pygame with ellipses 
#flowing throughout the screen
import pygame
from pygame.locals import *
pygame.init()

class Main(object):
	def __init__(self):
		screenSize = (640, 480)
		surface = pygame.display.set_mode(screenSize)
		lime = (0, 255, 0)
		myBox = Box()
		
		myOtherBox = Box()
		myOtherBox.color = (255, 0, 0) #red
		myOtherBox.x = 300
		myOtherBox.y = 100
		
		yetAnotherBox = Box()
		yetAnotherBox.color = (255, 0, 255) #magenta
		yetAnotherBox.x = 500
		yetAnotherBox.y = 200
		
		done = False
		
		while not done: 
			surface.fill(lime) #RGB color of lime green
			myBox.update()
			myOtherBox.update()
			yetAnotherBox.update()
			
			myBox.draw(surface)
			myOtherBox.draw(surface)
			yetAnotherBox.draw(surface)
			
			pygame.display.flip() #draw surface on screen
			
			events = pygame.event.get() #function gets all recent input events
			
			for e in events:
				if e.type is QUIT: #triggered by hitting x 
					done = True
				elif e.type is KEYDOWN: #if it is letter "q" set done to true
					if e.key == K_q:
						done = True
						
class Box(object): #can reuse this idea of box
	def __init__(self):
		self.x = 0
		self.y = 0
		self.vx = 1
		self.vy = 1
		self.size = (50, 50)
		self.color = (0, 0, 255)
		
	def update(self):
		self.x += self.vx
		self.y += self.vy #with x and y it will move diagonally
	
		if self.x > 640 - 50:
			self.vx = -1
		
		if self.x < 0:
			self.vx = 1
		
		if self.y > 480 - 50:
			self.vy = -1
		
		if self.y < 0:
			self.vy = 1
		
	def draw(self, surface):
		rect = pygame.Rect((self.x, self.y), self.size) #square at a position 
		pygame.draw.ellipse(surface, self.color, rect) #could also use rect for a square
		
Main()	