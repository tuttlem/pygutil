
import pygame
from pygame.locals import *

class Spritemap:

	def __init__(self, filename, colourkey=None):
		self.load_map(filename, colourkey)

	def load_map(self, filename, colourkey):
		'''Initializes this map to a file'''
		self.defs = {}

		try:
			self.map = pygame.image.load(filename)
		except pygame.error, message:
			print 'Cannot load image: ', name
			raise SystemExit, message

		self.map = self.map.convert()

		if colourkey is not None:
			if colourkey is -1:
				colourkey = self.map.get_at((0, 0))

			self.map.set_colorkey(colourkey, RLEACCEL)

	def def_sprite(self, key, rect):
		'''Defines a single sprite within the map'''
		self.defs[key] = rect

	def def_set(self, key, rects):
		'''Defines an arbitrary set of sprites within the map'''
		self.defs[key] = rects

	def def_line(self, key, rect, n):
		'''Defines an array of rects within the map occuring in repitition on the x-axis'''
		rects = [pygame.Rect(rect.x + (i * rect.width), rect.y, rect.w, rect.h) for i in range(n)]
		self.def_set(key, rects)

	def blit(self, screen, x, y, key, index=0):
		'''Draws the sprite referred to by key'''
		entry = self.defs[key]

		# we can't do anything if we don't find an entry
		if entry is None:
			return

		r = None

		# if we pulled out an array, it's a set - use the index parameter
		if isinstance(entry, list):
			r = entry[index]
		else:
			r = entry

		# draw the image to screen
		dest = pygame.Rect(x, y, r.width, r.height)
		screen.blit(self.map, dest, r)
