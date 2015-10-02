import application
import unittest


class testCountriesAndCapitals(unittest.TestCase):

	def test_is_alpha(self):
		self.assertEqual(application.is_alpha("Guatemala"), True)
		self.assertEqual(application.is_alpha("5"), False)

	def test_is_title(self):
		self.assertEqual(application.is_title("guate"), "Guate")

	def test_minuscule(self):
		self.assertEqual(application.minuscule("GUATE"), "guate")

if __name__ == '__main__':
	unittest.main()
