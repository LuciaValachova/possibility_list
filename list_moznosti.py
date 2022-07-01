#   1. cyklus for...in
#    vypíše sa celý zoznam vopred uložených zvierat, pod seba

zvierata = ['kohút','ovca','prasa','krava','kôň']
for vypis in zvierata:
    print(vypis)

#   2. cyklus for.. in 
#     vypíše sa celý zoznam vopred uložených zvierat do riadku, oddelených čiarkou

zvierata = ['kohút','ovca','prasa','krava','kôň']
for vypis in zvierata:
    print(vypis, end=', ') #OK#

#   3. Cyklus while. zo vstupu vložit na požiadanie postupne 5 zvierat do zoznamu.   
#      Výstup: výpis zvierat do riadku
# A
zoznam = []
poradie = 0
n = 0

while poradie != 5 and n != 5:
 zviera = input("Napíš "  + str(poradie+1) + ".zviera: ")
 prevod = zviera.split()
 zoznam = zoznam + prevod
 poradie = poradie + 1
n = n + 1
print("\nVšetky zvieratá sa uložili do zoznamu: ")
for vypis in zoznam:
  print(vypis, end=', ')
print("\n") #OK#
	
#B - zvierata sa ulozili do retazca iba raz...

zoznam = []
poradie = 0
n = pocet_zvierat = 0

while poradie != 5 and n != 5:
 zviera = input("Napíš "  + str(poradie+1) + ".zviera: ")
 zviera = zviera.split()
 for retazec in zviera:
   if not retazec in zoznam:
      zoznam.append(retazec)
 poradie = poradie + 1
n = n + 1
print("\nVšetky zvieratá sa uložili do zoznamu: ")
for vypis in zoznam:
  print(vypis, end=', ')
print("\n")    
    
    
#   4. 	spojí (spočíta) 2 zoznamy na vstupe do jedného a vypíše to spolu na obrazovku

zvierata = ['kohút','ovca','prasa','krava','kôň']
veci = ['stol','pero','lopta']
zvierata = zvierata + veci
print(zvierata)

#   5.rozloží vstup na jednotlivé znaky, písmená a výpíše ich 
#   pr.: pes → ['p','e','s']

zviera = input("napis zviera:")
znaky_zviera = list(zviera)
print(znaky_zviera)

# 6. ak je počet premenných vľavo zhodný s počtom znakov vpravo, výstup bude zviera - postupnosť znakov

a, b, c, d, e, f = 'Bažant'
print(a, b, c, d, e, f)→ Bažant

# 7. PRIDANIE zvierata pomocou 'append' - jeden znak alebo reťazec, 'extend' - spoji zoznamy, 'insert'(poradie retazca(znaku)), 
#    vlozi nový reťazec a posunie vsetky retazce za nim o 1 poziciu doprava

zvierata = ['kohút','ovca','prasa','krava','kôň']
print(zvierata)
zvierata.append('koza') # pripoji kozu do zoznamu
print(zvierata)

zvierata.append(39) # pripoji cislo 39 do zoznamu
print(zvierata)
zvierata1 = ['kôň','králik','pes',45]
zvierata.extend(zvierata1)   #spoji zoznamy dokopy (do jedneho)
print (zvierata)

zvierata.insert(6,'LEOPARD') # vlozi na 6 poziciu leoparda a ostatne pokacuju za nim
print(zvierata)

prasaindex = zvierata.index('prasa') # zisti a vypise poziciu pre 'prasa'  
print(prasaindex)

# 8.    ODOBRATIE retazca zo zoznamu  

zvierata = ['kohút','ovca','prasa','krava','kôň']
zvierata.remove('ovca')  #odoberie ovcu zo zoznamu
print(zvierata)

zvierata = ['kohút','ovca','prasa','krava','kôň']
popped = zvierata.pop() # odoberie posledny reťazec na konci zoznamu
print(popped)
print(zvierata)       

zvierata = ['kohút','ovca','prasa','krava','kôň']
popped = zvierata.pop(1)# odoberie a vypise ovcu, lebo je na pozicii 1, rata sa od 0-ly
print(popped)
print(zvierata)