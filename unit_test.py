import application
import unittest


class testCountriesAndCapitals(unittest.TestCase):

	def test_is_alpha(self):
		self.assertEqual(application.is_alpha("Guatemala"), True)
		self.assertEqual(application.is_alpha("5"), False)

if __name__ == '__main__':
	unittest.main()
