import unittest
import asyncio

from Matrix import *

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

class TestGetMatrix(unittest.TestCase):	
	def test_get_matrix(self):
		self.assertEqual(TRAVERSAL, asyncio.run(get_matrix(SOURCE_URL)))


unittest.main()