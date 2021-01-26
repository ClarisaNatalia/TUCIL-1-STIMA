#TUCIL 1 STIMA
#Clarisa Natalia Edelin
#13519213
#cryptarithmatic solver

import time

def bacafile():
    teks = []
    with open('tes.txt','r') as t: #'tes.txt' diubah sesuai file tes yang ingin diuji
        for isiteks in t:
            if not isiteks.startswith("-"):
                teks.append(isiteks.rstrip('\n'))
        return(teks) #print(a)  #hasil : ['SEND', 'MORE', 'MONEY']

def listhurufunik(isifiletxt):
    listawal = []

    for i in range (0,(len(isifiletxt))):
        for j in range(0,(len(isifiletxt[i]))):
           listawal.append((isifiletxt[i])[j])

    listunik = list(set(listawal))
    #print(b) #hasil : ['Y', 'N', 'S', 'R', 'M', 'D', 'E', 'O']
    return listunik

def printsoal(isifiletxt):
    for i in range(0,len(isifiletxt)-1):
        print(isifiletxt[i], end = "\n")

    print("---- +", end = "\n")

    print(isifiletxt[len(isifiletxt)-1])

def printjawabanangka(jawabanangka):
    for i in range(0,len(jawabanangka)-1):
        print(jawabanangka[i], end = "\n")

    print("---- +", end = "\n")

    print(jawabanangka[len(jawabanangka)-1])

#mainprogram
isifiletext = bacafile()

start = time.time()
t = time.process_time()

arrayhurufunik = listhurufunik(isifiletext)


ketemu = False
jumlahsolusi = 0
jawaban = []
isitextdalamangka2 = ['' for p in range(len(isifiletext))]

for a in range(0,10):
    for b in range(0,10):
        if ketemu == False and b!=a:
            for c in range(0,10):
                if ketemu == False and c!=b and c!=a:
                    for d in range(0,10):
                        if ketemu == False and d!=c and d!= b and d!=a:
                            for e in range(0,10):
                                if ketemu == False and e!=d and e!=c and e!=b and e!=a:
                                    for f in range(0,10):
                                        if ketemu == False and f!=e and f!=d and f!=c and f!=b and f!=a:
                                            for g in range(0,10):
                                                if ketemu == False and g!=f and g!= e and g!=d and g!= c and g!=b and g!=a:
                                                    for h in range(0,10):
                                                        if ketemu == False and h!=g and h!=f and h!=e and h!=d and h!=c and h!=b and h!=a:
                                                            for i in range(0,10):
                                                                if ketemu == False and i!=h and i!=g and i!=f and i!=e and i!=d and i!=c and i!=b and i!=a:
                                                                    for j in range(0,10):
                                                                        if ketemu == False and j!=i and j!=h and j!=g and j!=f and j!=e and j!=d and j!=c and j!=b and j!=a:

                                                                            jumlahsolusi += 1
                                                                            jawaban = [a,b,c,d,e,f,g,h,i,j]
                                                                            isitextdalamangka = ['' for p in range(len(isifiletext))]
                                                                                                                               
                                                                            jawabansebanyakhurufunik = [0 for q in range(len(arrayhurufunik))]

                                                                            for z in range(len(arrayhurufunik)):
                                                                                jawabansebanyakhurufunik[z] = jawaban[z]


                                                                            maphurufjawaban = [arrayhurufunik,jawabansebanyakhurufunik]

                                                                            #bikin array isi angka dalam urutan huruf soal
                                                                            for w in range(0,len(isifiletext)):

                                                                                for hururfyangdiuji in range(len(isifiletext[w])):

                                                                                    for t in range(len(arrayhurufunik)):

                                                                                        if ((isifiletext[w])[hururfyangdiuji] == ((maphurufjawaban[0])[t])):
                                                                                            isitextdalamangka[w] += str((maphurufjawaban[1])[t])
                                                                                            
                                                                            apakahnol = False

                                                                            for y in range(0,len(isitextdalamangka)):
                                                                                if (isitextdalamangka[y])[0] == '0':
                                                                                    apakahnol = True
                                                                                    break

                                                                            jawabanangka = 0
                                                                            if apakahnol == False:
                                                                                for o in range(len(isitextdalamangka)-1):
                                                                                    jawabanangka += int(isitextdalamangka[o])


                                                                            if jawabanangka - int(isitextdalamangka[len(isitextdalamangka)-1]) == 0:
                                                                                ketemu = True 
                                                                                for angka in range(len(isitextdalamangka)):
                                                                                    isitextdalamangka2[angka] = isitextdalamangka[angka]


print("banyak percobaan yang dilakukan : ")
print(jumlahsolusi)
print("soal")
printsoal(isifiletext)
print("jawaban")
printjawabanangka(isitextdalamangka2)

print("waktu yang dibutuhkan :")
waktu = time.process_time() - t

print(waktu)
