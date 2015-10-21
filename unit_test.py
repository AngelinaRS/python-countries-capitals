#!/usr/bin/env python
# -*- coding: utf-8 -*-

import application
import unittest


class testCountriesAndCapitals(unittest.TestCase):

	def test_is_alpha(self):
		cc = application.CountriesAndCapitals()
		self.assertEqual(cc.is_alpha("Guatemala"), True)
		self.assertEqual(cc.is_alpha("5"), False)

	def test_is_title(self):
		cc = application.CountriesAndCapitals()
		self.assertEqual(cc.is_title("guate"), "Guate")
		self.assertEqual(cc.is_title("españa"), "España")

	def test_minuscule(self):
		cc = application.CountriesAndCapitals()
		self.assertEqual(cc.minuscule("GUATE"), "guate")

if __name__ == '__main__':
	unittest.main()
