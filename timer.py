
import pygame.time

class Timer:

	def __init__(self):
		'''Initialize this timer'''
		self.last = pygame.time.get_ticks()

	def reset(self):
		'''Reset the timer'''
		self.last = pygame.time.get_ticks()

	def elapsed(self):
		'''Get the number of ticks that have passed since the last call to elapsed or reset'''
		current = pygame.time.get_ticks()
		diff = current - self.last
		self.last = current

		return diff
