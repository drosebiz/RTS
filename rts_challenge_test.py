"""
Dan Rose
RTS Labs Coding Assignment - Unit Tests
"""

import unittest
from math import pi
from rts_challenge import aboveBelow, stringRotation

class AboveBelowTests(unittest.TestCase):

	# Standard case
	def testA(self):
		int_list = [-1, 0, 1]
		comp_val = 0
		answer = {'above': 1, 'below': 1}
		self.assertEqual(aboveBelow(int_list, comp_val), answer)

	# Another standard case (unsorted)
	def testB(self):
		int_list = [10, 9, 2, 8, 3, 7, 4, 6, 5, 1]
		comp_val = 3
		answer = {'above': 7, 'below': 2}
		self.assertEqual(aboveBelow(int_list, comp_val), answer)
	
	# Empty comparison list
	def testC(self):
		int_list = []
		comp_val = 99
		answer = {'above': 0, 'below': 0}
		self.assertEqual(aboveBelow(int_list, comp_val), answer)

	# Comparison value not an int
	def testD(self):
		int_list = [-1, 0, 1]
		comp_val = pi
		with self.assertRaises(TypeError):
			aboveBelow(int_list, comp_val)

	# No comparison value
	def testE(self):
		int_list = [-1, 0, 1]
		comp_val = None
		with self.assertRaises(TypeError):
			aboveBelow(int_list, comp_val)

	# Floats in comparison list
	def testF(self):
		int_list = [-1.5, 2.18, pi, -9.71223123]
		comp_val = 0
		with self.assertRaises(TypeError):
			aboveBelow(int_list, comp_val)

	# String objects in comparison list
	def testG(self):
		int_list = ['aardvark', 'jalapeno', 'xylophone']
		comp_val = 0
		with self.assertRaises(TypeError):
			aboveBelow(int_list, comp_val)


class StringRotationTests(unittest.TestCase):
	# Standard case
	def testA(self):
		orig = 'Penguin'
		rotations = 3
		answer = 'uinPeng'
		self.assertEqual(stringRotation(orig, rotations), answer)

	# Standard case with wraparound
	def testB(self):
		orig = 'Penguin'
		rotations = 12
		answer = 'nguinPe'
		self.assertEqual(stringRotation(orig, rotations), answer)	
	
	# No rotation
	def testC(self):
		orig = 'Penguin'
		rotations = 0
		with self.assertRaises(ValueError):
			stringRotation(orig, rotations)

	# Empty string
	def testD(self):
		orig = ''
		rotations = 7
		answer = ''
		self.assertEqual(stringRotation(orig, rotations), answer)

	# Non-string original string
	def testE(self):
		orig = 12
		rotations = 3
		with self.assertRaises(TypeError):
			stringRotation(orig, rotations)

	# Negative Rotations
	def testF(self):
		orig = 'Penguin'
		rotations = -5
		with self.assertRaises(ValueError):
			stringRotation(orig, rotations)

	# String with escape characters
	def testG(self):
		orig = "\"vamos\""
		rotations = 1
		answer = "\"\"vamos"
		self.assertEqual(stringRotation(orig, rotations), answer)
	
	# None rotations
	def testH(self):
		orig = 'Penguin'
		rotations = None
		with self.assertRaises(TypeError):
			stringRotation(orig, rotations)

	# None string
	def testI(self):
		orig = None
		rotations = 22
		with self.assertRaises(TypeError):
			stringRotation(orig, rotations)


if __name__ == '__main__':
	unittest.main()