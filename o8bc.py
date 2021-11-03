# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:45:34 2021

@author: Einar
"""
Poeng = 0
Totaltspr = 0

class QuizTest:
    
    def __init__(self,Sporsmalx,Svaralt,Fasit):
        self.Sporsmal = Sporsmalx
        self.Svar = Svaralt
        self.Fasit = Fasit

    def __str__(self):
        for j in range(len(Sporsmal)-1):
            x = ("-----------------------------------"+"\n"+str(Sporsmal[Totaltspr])+"\n"+"-----------------------------------"+"\n")
            for i in Svar[Totaltspr]:
                x+= str(i)+"\n"
        return f"{x}"
    
    def svarsjekk():
        if Brukersvar == Rett_svar[Totaltspr-1]:
            print("\n"+"Korrekt!"+"\n")
            return True
        else:
            print("\n"+"Feil!"+"\n")
            return False
    
    def Endeligsum():
        if Totaltspr == len(Rett_svar):
            Endeligsum = (Poeng/Totaltspr)*100
            print("-----------------------------------")
            print(f"Du fikk {Endeligsum:.1f}% riktig.")

if __name__ == '__main__':
    Poeng = 0
    Sporsmal = ["Hvilken er den lengste elven i Norge?","Hva er det høyeste Fjellet i Møre og Romsdal?","Hvem er kjent som Ole Brum?","Hvilket land er nr 1?"]
    Svar = [["1. Pasvikelva","2. Glomma","3. Tana","4. Otra"],["1. Pyttegga","2. Katritind","3. Storskrymten","4. Kleneggen"],["1. Donald Trump","2. Boris Johnson","3. Vladimir Putin","4. Xi Jinping"],["1. China","2. Taiwan","3. Hong Kong","4. Japan"]]
    Rett_svar = [2,1,4,2]
    
    p = QuizTest(Sporsmal[Totaltspr],Svar[Totaltspr],Rett_svar[Totaltspr])
    
    for k in Sporsmal:
        print(p)
        Brukersvar = int(input("Skriv inn ditt endelige svar(1, 2, 3 eller 4): "))
        print("-----------------------------------")
        Totaltspr += 1
        
        if QuizTest.svarsjekk() == True:
            Poeng+=1
        
        QuizTest.Endeligsum()
        
        