# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:45:34 2021

@author: Einar
"""
Poeng = 0
Totaltspr = 0

class QuizTest:
    
    def __init__(self,Sporsmalx,Svaralt,Fasit):
        self.Sporsmaal = Sporsmalx
        self.Svaralternativ = Svaralt
        self.Rett_svar = Fasit

    def __str__(self):
        for j in range(len(Sporsmaal)-1):
            x = ("-----------------------------------"+"\n"+str(Sporsmaal[Totaltspr])+"\n"+"-----------------------------------"+"\n")
            Qnr=0
            for i in Svaralternativ[Totaltspr]:
                Qnr+=1
                x+= str(Qnr)+". "+str(i)+"\n"
        return f"{x}"
    
    def svarsjekk(Bruker):
        if Bruker-1 == Rett_svar[Totaltspr-1]:
            return True
        else:
            return False
    
    def Endeligsum(Poeng,SpNr):
        if Totaltspr == len(Rett_svar):
            Endeligsum = (Poeng/Totaltspr)*100
            print("-----------------------------------")
            print(f"Spiller {SpNr} fikk {Endeligsum:.1f}% riktig.")
            
    def korrekt_svar_tekst():
        Svarnr = int(Rett_svar[Totaltspr-1])
        Fasit = Svaralternativ[Totaltspr-1]
        print(f"Riktig svar var: {Fasit[Svarnr]}")
            
def Sporsmaalfunk():
    with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as rf:
        Quiz = []
        for line in rf:
            separate = line.split(":")
            Sporsmaal.append(separate[0])
            Rett_svar.append(int(separate[1].strip(" ")))
            yeks = separate[2].split(",")
            Svarliste = []
            for thelist in yeks:
                Cleaning = thelist.strip("[ ]")
                Cleaning = Cleaning.replace("]","")
                Svarliste.append(Cleaning)
                
            Svaralternativ.append(Svarliste)
            
            #for ans in separate[2].strip("[]").split(","):
            #    Svaralternativ.append(ans)
            Quiz.append(QuizTest(Sporsmaal,Svaralternativ,Rett_svar))
        return Sporsmaal, Rett_svar, Svaralternativ

if __name__ == '__main__':
    Spiller1 = 0
    Spiller2 = 0
    Sporsmaal = []
    Rett_svar = []
    Svaralternativ = []
    
    Sporsmaalfunk()
    
    p = QuizTest(Sporsmaal[Totaltspr],Svaralternativ[Totaltspr],Rett_svar[Totaltspr])

    for k in Sporsmaal:
        print(p)
        Brukersvar1 = int(input("Spiller 1 sitt enelige svar: "))
        Brukersvar2 = int(input("Spiller 2 sitt endelige svar: "))

        print("-----------------------------------")
        Totaltspr += 1
        QuizTest.korrekt_svar_tekst()
        print("-----------------------------------")
        
        if QuizTest.svarsjekk(Brukersvar1) == True:
            Spiller1+=1
            print("Spiller 1: Riktig!")
        else:
            print("Spiller 1: Feil!")
        
        if QuizTest.svarsjekk(Brukersvar2) == True:
            Spiller2+=1
            print("Spiller 2: Riktig!")
        else:
            print("Spiller 2: Feil!")
        
        QuizTest.Endeligsum(Spiller1, 1)
        QuizTest.Endeligsum(Spiller2, 2)        
        