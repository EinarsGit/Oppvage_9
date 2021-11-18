# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:47:18 2021

@author: Einar
"""

import unittest
from o10 import QuizTest

class TestSvarsjekk(unittest.TestCase):
    def testsvarsjekk(self):
        Test1 = QuizTest("Sporsmal1",["Svar1","Svar2","Svar3"],1)
        Test2 = QuizTest("Spørsmal2",["Svar1","Svar2","Svar3","Svar4"],3)
        Test3 = QuizTest.svarsjekk(Test1,2) #.Fasit + 1
        Test4 = QuizTest.svarsjekk(Test2,4) #.Fasit + 1
        self.assertEqual(Test1.Sporsmal,"Sporsmal1")
        self.assertEqual(Test2.Sporsmal,"Spørsmal2")
        self.assertEqual(Test1.Svar,["Svar1","Svar2","Svar3"])
        self.assertEqual(Test2.Svar,["Svar1","Svar2","Svar3","Svar4"])
        self.assertEqual(Test1.Fasit,1)
        self.assertEqual(Test2.Fasit,3)
        self.assertEqual(Test3,True)
        self.assertEqual(Test4,True)

    def testkorrekt_svar_sjekk(self):
        Test1 = QuizTest("Sporsmal1",["Svar1","Svar2","Svar3"],1)
        Test2 = QuizTest("Spørsmal2",["Svar1","Svar2","Svar3","Svar4"],3)
        self.assertEqual(Test1.Sporsmal,"Sporsmal1")
        self.assertEqual(Test2.Sporsmal,"Spørsmal2")
        self.assertEqual(Test1.Svar,["Svar1","Svar2","Svar3"])
        self.assertEqual(Test2.Svar,["Svar1","Svar2","Svar3","Svar4"])
        self.assertEqual(Test1.Fasit,1)
        self.assertEqual(Test2.Fasit,3)


if __name__ == '__main__':
    unittest.main()