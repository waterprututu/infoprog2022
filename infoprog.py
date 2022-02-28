import math

hosszusagi = []
szelessegi = []
zsakok_szama = []
fordulatok = 0
tavolsag = 0
<<<<<<< HEAD
=======
#sdf
>>>>>>> Initial commit

# A harmadik feladat megoldó algoritmusa 

# koordinatak - raktár koordinátái
# kivant_zsakok_szama - raktar feltotesehez szukseges zsakok szama
# zsakok_szama_szanon - a zsakok szama a szonon
# jelenlegi - a szan jelenlegi pozicioja
# elozo_kord - elozo raktar koordinataja
# nem_elso - boolean, nem az elso raktar a listan
# return - kimaradt zsakok szama, jelenlegi pozicio
def kiszallitas2(koordinatak, kivant_zsakok_szama, zsakok_szama_szanon, jelenlegi, elozo_koord, nem_elso):
    global fordulatok
    global tavolsag
    
    if nem_elso and (zsakok_szama_szanon < kivant_zsakok_szama):
        print(f"{elozo_koord} -> {raktar_koordinatak()}")
        tavolsag += tavolsag_szamitas(elozo_koord, raktar_koordinatak())
        jelenlegi = raktar_koordinatak()
        zsakok_szama_szanon = 125

    while True:
        if zsakok_szama_szanon > kivant_zsakok_szama:
            zsakok_szama_szanon -= kivant_zsakok_szama
            print(f"{jelenlegi} -> {koordinatak}")
            if jelenlegi == raktar_koordinatak():
                fordulatok += 1 
            tavolsag += tavolsag_szamitas(jelenlegi, koordinatak)
            return (zsakok_szama_szanon, koordinatak)

        elif zsakok_szama_szanon < kivant_zsakok_szama:
            kivant_zsakok_szama -= zsakok_szama_szanon
            print(f"{jelenlegi} -> {koordinatak}")
            if jelenlegi == raktar_koordinatak():
                fordulatok += 1
            tavolsag += tavolsag_szamitas(jelenlegi, koordinatak)
            print(f"{koordinatak} -> {raktar_koordinatak()}")
            tavolsag += tavolsag_szamitas(koordinatak, raktar_koordinatak())
            jelenlegi = raktar_koordinatak()
            zsakok_szama_szanon = 125
        
        elif zsakok_szama_szanon == kivant_zsakok_szama:
            print(f"{jelenlegi} -> {koordinatak}")
            if jelenlegi == raktar_koordinatak():
                fordulatok += 1
            tavolsag += tavolsag_szamitas(jelenlegi, koordinatak)
            print(f"{koordinatak} -> {raktar_koordinatak()}")
            tavolsag += tavolsag_szamitas(koordinatak, raktar_koordinatak())
            return (125, raktar_koordinatak())

# Ket raktar kozti tavolsag kiszamitasara hasznalando
def tavolsag_szamitas(koordinatak1, koordinatak2):
    return math.sqrt((int(koordinatak1[0]) - int(koordinatak2[0])) ** 2 + (int(koordinatak1[1]) - int(koordinatak2[1])) ** 2)

# A elso feladat megoldó algoritmusa 

# koordinatak - raktár koordinátái
# kivant_zsakok_szama - raktar feltotesehez szukseges zsakok szama
# zsakok_szama_szanon - a zsakok szama a szonon
# jelenlegi - a szan jelenlegi pozicioja
# return - kimaradt zsakok szama, jelenlegi pozicio
def kiszallitas1(koordinatak, kivant_zsakok_szama, zsakok_szama_szanon, jelenlegi):
    global fordulatok
    global tavolsag
    while True:
        if zsakok_szama_szanon > kivant_zsakok_szama:
            zsakok_szama_szanon -= kivant_zsakok_szama
            print(f"{jelenlegi} -> {koordinatak}")
            if jelenlegi == raktar_koordinatak():
                fordulatok += 1 
            tavolsag += tavolsag_szamitas(jelenlegi, koordinatak)
            return (zsakok_szama_szanon, koordinatak)

        elif zsakok_szama_szanon < kivant_zsakok_szama:
            kivant_zsakok_szama -= zsakok_szama_szanon
            print(f"{jelenlegi} -> {koordinatak}")
            if jelenlegi == raktar_koordinatak():
                fordulatok += 1
            tavolsag += tavolsag_szamitas(jelenlegi, koordinatak)
            print(f"{koordinatak} -> {raktar_koordinatak()}")
            tavolsag += tavolsag_szamitas(koordinatak, raktar_koordinatak())
            jelenlegi = raktar_koordinatak()
            zsakok_szama_szanon = 125
        
        elif zsakok_szama_szanon == kivant_zsakok_szama:
            print(f"{jelenlegi} -> {koordinatak}")
            if jelenlegi == raktar_koordinatak():
                fordulatok += 1
            tavolsag += tavolsag_szamitas(jelenlegi, koordinatak)
            print(f"{koordinatak} -> {raktar_koordinatak()}")
            tavolsag += tavolsag_szamitas(koordinatak, raktar_koordinatak())
            return (125, raktar_koordinatak())

def raktar_koordinatak():
    return (raktar[0], raktar[1])

# Kinyitja az allomanyt es beolvassa soronkent
file1 = open("raktar.txt")
x = file1.readlines()
y = x.copy()
for i in range(len(x)):
    x[i] = x[i][:-1]
file1.close()

raktar = x.pop(0).split(",")
utolso = x.pop(-1).split(",")

# Feldarabolja a sorokat a 3 ","-vel elvalasztott szamra
for i in range(len(x)):
    a = []
    b = []
    c = []
    a, b, c = x[i].split(",")
    hosszusagi.append(a)
    szelessegi.append(b)
    zsakok_szama.append(int(c))

e = [125, raktar_koordinatak()]

# Minden egyes sorra hivja fuggvenyt 
for i in range(19):
    e = kiszallitas1((hosszusagi[i], szelessegi[i]), zsakok_szama[i], e[0], e[1])
    if i == 18:
        print(f"{(hosszusagi[i], szelessegi[i])} -> {raktar_koordinatak()}")
        tavolsag += tavolsag_szamitas((hosszusagi[i], szelessegi[i]), raktar_koordinatak()) 

print(f"[1] Fordulatok szama: {fordulatok}\n[1] Megtett tavolsag: {tavolsag * 1000} km")

# Elmenti az allomanyba az utolso raktar maradekjat
file2 = open("raktar.txt", "w")
y[-1] = y[-1][:-1] + "," + str(e[0])
for i in y:
    file2.write(i)
file2.close()


a, b, c = y[-1].split(",")
hosszusagi.append(a)
szelessegi.append(b)
zsakok_szama.append(c)

fordulatok = 0
tavolsag = 0
e = [125, raktar_koordinatak()]

# Minden egyes sorra hivja a fuggvenyt
for i in range(20):
    if i:
        e = kiszallitas2((hosszusagi[i], szelessegi[i]), int(zsakok_szama[i]), e[0], e[1], (hosszusagi[i-1],szelessegi[i-1]), True)
        if i == 19 and e[1] != raktar_koordinatak():
            print(f"{(hosszusagi[i], szelessegi[i])} -> {raktar_koordinatak()}")
            tavolsag += tavolsag_szamitas((hosszusagi[i], szelessegi[i]), raktar_koordinatak()) 
    else:
        e = kiszallitas2((hosszusagi[i], szelessegi[i]), int(zsakok_szama[i]), e[0], e[1], raktar_koordinatak(), False)

print(f"[3] Fordulatok szama: {fordulatok}\n[3] Megtett tavolsag: {tavolsag * 1000} km")