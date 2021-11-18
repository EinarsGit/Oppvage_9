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
    
    def Endeligsum(Spiller,Poeng,Totspr):
        Endeligsum = (Poeng/Totspr)*100
        print("-----------------------------------")
        print(f"{Spiller} vant med {Endeligsum:.1f}% riktige svar!")
        
    def Sporsmaalfunk(): # Oppgave 9d   MED TEKST FIL NAVN
        with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as rf:
            for line in rf:
                separate = line.split(":")
                yeks = separate[2].split(",")
                Svarliste = []
                for thelist in yeks:
                    Cleaning = thelist.strip("[ ]")
                    Cleaning = Cleaning.replace("]","")
                    Svarliste.append(Cleaning)
                Quiz.append(QuizTest(separate[0].strip(),Svarliste,int(separate[1])))

    def korrekt_svar_tekst(self): # Oppgave 9e
        Fasitnr = self.Fasit
        Svar = self.Svar[Fasitnr]
        print(f"Riktig svar var: {Svar}")
        
    def ranking(self):
        Nummerering = 1
        for line in self:
            print(f"{Nummerering}. {line.Navn} - {(line.Poengsum/Totspr)*100}% Riktig")
            Nummerering += 1
        
class Spiller:
    
    def __init__(self,Navn,Poengsum):
        self.Navn = Navn
        self.Poengsum = Poengsum
    
    def __str__(self):
        Notes = f"{self.Navn}: {self.Poengsum} av {Totspr} riktige."
        return Notes
    
    def antspillere():      # <--- Flytte til if __main__?
        nrspillere = int(input("Hvor mange ønsker å delta? "))
        ki = 0
        while ki < nrspillere:
            SpillerListe.append(Spiller(input("Navn: "),0))
            ki += 1


if __name__ == '__main__':
    Quiz = []
    SpillerListe = []
    Totspr = 0
    Spiller.antspillere()
    QuizTest.Sporsmaalfunk()
    
    for j in Quiz:
        print(j)
        Totspr += 1
        Spillersvar = []
        SpillerIndex = 0
        for spiller in SpillerListe:
            
            Spillersvar.append(int(input(f"{spiller.Navn} sitt enelige svar: ")))
        SpillerAntall = len(SpillerListe)
        
        print("-----------------------------------\n")
        
        for svr in Spillersvar:
            if QuizTest.svarsjekk(Quiz[Totspr-1],svr) == True:
                print(f"{SpillerListe[SpillerIndex].Navn}: Riktig!")
                Poeng = SpillerListe[SpillerIndex].Poengsum +1
                SpillerListe[SpillerIndex] = Spiller(SpillerListe[SpillerIndex].Navn,Poeng)
            else:
                print(f"{SpillerListe[SpillerIndex].Navn}: Feil!")
            SpillerIndex += 1
        print("-----------------------------------")
        QuizTest.korrekt_svar_tekst(Quiz[Totspr-1])
        print("-----------------------------------")


    TopScore = SpillerListe[0].Poengsum  #-----------------------
    TopScoreNr = 0
    for me in range(len(SpillerListe)-1):
        if TopScore < SpillerListe[me+1].Poengsum:
            TopScore = SpillerListe[me+1].Poengsum
            TopScoreNr = me+1                   # Kan Slettes!
        else:
            continue
    print(SpillerListe[TopScoreNr])
                                        #------------------------

    Ranking = []
    RankingDelete = SpillerListe
    for antall in range(len(SpillerListe)):
        TopScore = RankingDelete[0].Poengsum
        TopScoreNr = 0
        for me in range(len(RankingDelete)-1):
            if TopScore < RankingDelete[me+1].Poengsum:
                TopScore = RankingDelete[me+1].Poengsum
                TopScoreNr = me+1
            else:
                continue
        Ranking.append(SpillerListe[TopScoreNr])
        RankingDelete.remove(SpillerListe[TopScoreNr])
    print("-----------------------------------")
    QuizTest.ranking(Ranking)