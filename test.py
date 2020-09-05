#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest
import primo #el nombre de tu archivo de codigo a probar


class Testprueba (unittest.TestCase):

    def test_primo(self):
        self.assertTrue(primo.es_primo(47))
        self.assertTrue(primo.es_primo(97))
        self.assertTrue(primo.es_primo(53))
        self.assertTrue(primo.es_primo(71))
        self.assertFalse(primo.es_primo(25))
        self.assertFalse(primo.es_primo(91))
        self.assertFalse(primo.es_primo(80))
        self.assertFalse(primo.es_primo(6))





if __name__ == '__main__':
    unittest.main()