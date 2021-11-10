# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:45:34 2021

@author: Einar
"""

class QuizTest:
    
    def __init__(self,Sporsmalx,Svaralt,Fasit):
        self.Sporsmal = Sporsmalx
        self.Svar = Svaralt
        self.Fasit = Fasit

    def __str__(self):
        x = ("-----------------------------------"+"\n"+self.Sporsmal+"\n"+"-----------------------------------"+"\n")
        for i in range(len(self.Svar)):
            x+= str(i+1)+": "+str(self.Svar[i])+"\n"
        return x
    
    def svarsjekk(self,Brukersvar):
        if Brukersvar-1 == self.Fasit:
            return True
        else:
            return False
    
    def Endeligsum(Spiller,Poeng, Totspr):
        Endeligsum = (Poeng/Totspr)*100
        print("-----------------------------------")
        print(f"{Spiller} fikk {Endeligsum:.1f}% riktig.")
        
    def Sporsmaalfunk(): # Oppgave 9d
        with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as rf:
            Quizzers = []
            for line in rf:
                separate = line.split(":")
                yeks = separate[2].split(",")
                Svarliste = []
                for thelist in yeks:
                    Cleaning = thelist.strip("[ ]")
                    Cleaning = Cleaning.replace("]","")
                    Svarliste.append(Cleaning)
                Quiz.append(QuizTest(separate[0].strip(),Svarliste,int(separate[1])))
            return Quizzers

    def korrekt_svar_tekst(): # Oppgave 9e
        Fasit = Quiz[Totspr-1]
        Fasitnr = Fasit.Fasit
        Svar = Fasit.Svar[Fasitnr]
        print(f"Riktig svar var: {Svar}")


if __name__ == '__main__':
    Quiz = []
    Spiller1 = 0
    Spiller2 = 0
    Totspr = 0
    QuizTest.Sporsmaalfunk()
    for j in Quiz:
        print(j)
        Brukersvar1 = int(input("Spiller 1 sitt enelige svar: "))
        Brukersvar2 = int(input("Spiller 2 sitt endelige svar: "))

        print("-----------------------------------")
        Totspr += 1
        QuizTest.korrekt_svar_tekst()
        print("-----------------------------------")
        
        if QuizTest.svarsjekk(Quiz[Totspr-1],Brukersvar1) == True:
            Spiller1+=1
            print("Spiller 1: Riktig!")
        else:
            print("Spiller 1: Feil!")
        
        if QuizTest.svarsjekk(Quiz[Totspr-1],Brukersvar2) == True:
            Spiller2+=1
            print("Spiller 2: Riktig!")
        else:
            print("Spiller 2: Feil!")
        
    QuizTest.Endeligsum("Spiller1",Spiller1, Totspr)
    QuizTest.Endeligsum("Spiller2",Spiller2, Totspr)