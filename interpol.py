
import math
import pygame
import timer

class Interpolator:

	def __init__(self, start, end, repeat, ticks):
		self.start = start
		self.end = end
		self.repeat = repeat
		self.ticks = ticks

		self.progress = 0
		self.done = False

		self.timer = timer.Timer()

	def reset(self):
		self.progress = 0
		self.timer.reset()
		self.done = False

	def length(self):
		return self.end - self.start

	def __iter__(self):
		return self

	def next(self):
		# a finished interpolator is always at the end
		if self.done:
			return self.end

		# accumulate the number of ticks passed
		self.progress += self.timer.elapsed()

		# handle termination boundaries
		if self.repeat:
			if self.progress > self.ticks:
				self.progress %= self.ticks
		else:
			if self.progress > self.ticks:
				self.done = True

		v = self.next_internal(float(self.progress) / float(self.ticks))

		return max(min(v, self.end), self.start)

	def next_internal(self, prog):
		return prog

class Linear(Interpolator):
	'''Performs interpolation linearly'''

	def next_internal(self, prog):
		return self.start + (self.length() * prog)

class Trigonometric(Interpolator):
	'''Performs interpolation along a trignometric wave'''

	def next_internal(self, prog):
		return self.start + (math.sin(prog * (math.pi / 2)) * self.length())

class Logarithmic(Interpolator):
	'''Performs interpolation along a logarithmic curve'''

	def next_internal(self, prog):
		return self.start + (math.log10(1.0 + (prog * 9.0)) * self.length())

