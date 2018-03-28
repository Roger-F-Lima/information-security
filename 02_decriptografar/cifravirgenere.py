def transformar(msg):
    if msg == "A":
        return 0
    elif msg == "B":
        return 1
    elif msg == "C":
        return 2
    elif msg == "D":
        return 3
    elif msg == "E":
        return 4
    elif msg == "F":
        return 5
    elif msg == "G":
        return 6
    elif msg == "H":
        return 7
    elif msg == "I":
        return 8
    elif msg == "J":
        return 9
    elif msg == "K":
        return 10
    elif msg == "L":
        return 11
    elif msg == "M":
        return 12
    elif msg == "N":
        return 13
    elif msg == "O":
        return 14
    elif msg == "P":
        return 15
    elif msg == "Q":
        return 16
    elif msg == "R":
        return 17
    elif msg == "S":
        return 18
    elif msg == "T":
        return 19
    elif msg == "U":
        return 20
    elif msg == "V":
        return 21
    elif msg == "W":
        return 22
    elif msg == "X":
        return 23
    elif msg == "Y":
        return 24
    elif msg == "Z":
        return 25

def descripta(i):
    if (i == 26):
        i = 0
    elif (i > 25):
        i = i - 26

    if i == 0:
        return "A"
    elif i == 1:
        return "B"
    elif i == 2:
        return "C"
    elif i == 3:
        return "D"
    elif i == 4:
        return "E"
    elif i == 5:
        return "F"
    elif i == 6:
        return "G"
    elif i == 7:
        return "H"
    elif i == 8:
        return "I"
    elif i == 9:
        return "J"
    elif i == 10:
        return "K"
    elif i == 11:
        return "L"
    elif i == 12:
        return "M"
    elif i == 13:
        return "N"
    elif i == 14:
        return "O"
    elif i == 15:
        return "P"
    elif i == 16:
        return "Q"
    elif i == 17:
        return "R"
    elif i == 18:
        return "S"
    elif i == 19:
        return "T"
    elif i == 20:
        return "U"
    elif i == 21:
        return "V"
    elif i == 22:
        return "W"
    elif i == 23:
        return "X"
    elif i == 24:
        return "Y"
    elif i == 25:
        return "Z"


def Guarda_mato(chave,msg):
    guarda = open("Guarda_chave.txt", "a")
    guarda.write("-------------------------------------------------------------------------------\n")
    guarda.write("\n")
    guarda.write("CHAVE: \n")
    guarda.write(chave)
    guarda.write("\n")
    guarda.write("MENSAGEM: \n")
    guarda.write(msg)
    guarda.write("\n")

    guarda.close()

alfa = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
msg="mllvo gjw axie, viog vlgbg dfptll n zoe fe gyyom j xof nr tuegr fg tfusfe ayqwxt rrpjnfy xg, mlm nbnju, tphuc kzg fltrf i ytamuyvi ig pzi qs or rrzzrgmtt spg acwfq, ux nnz xj eiqln ry akgphrfy"
m=""

for i in msg:
    if (i != " " and i !=","):
        m=m+i
msg = m.upper()

msgv = []

for i in msg:
    msgv.append(transformar(i))

aux = []
for a in alfa:
    for b in alfa:
        for c in alfa:
            for d in alfa:
                for e in alfa:
                    for f in alfa:
                        for g in alfa:
                            for h in alfa:
#                                print ("eu1")
                                cha = a+b+c+d+e+f+g+h
                                aux=[]
                                for i in cha:
                                    aux.append(transformar(i))
                                xx = len(msg)
                                x = 0
#                                print ("for 1")
                                while x < xx:
                                    x1 = 0
                                    x2 = len(aux)
                                    while x1 < x2:
                                        if (len(aux) < len(msg)):
                                            aux.append(aux[x1])
                                        x1 = x1 + 1
                                    x = x + 1
                                descri=[]

 #                               print ("w 1 e 2")
                                for i in range(len(msg)):
                                    soma = aux[i] + msgv[i]
                                    descri.append(soma)

  #                              print ("for 2")

                                testchave = []
                                for i in descri:
                                    testchave.append(descripta(i))

                                testchave.append("q")
                                testchave.append("q")
                                testchave.append("q")
                                testchave.append("q")
                                for i in range(len(testchave)):
                                    if (testchave[i] == "A" and testchave[i+1] == "M" and testchave[i+2] == "O" and testchave[i+3] == "R"):
                                        mensagem = ""
                                        for gu in testchave:
                                            mensagem = mensagem + gu
                                        Guarda_mato(cha,mensagem)
                                        print ("ebaaaaa")

print ("FIIIIIIIIIIIIIIIIIIIIIIIIIIIIIM")



