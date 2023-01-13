import sys

print("How many coins do you have in the current system of your country? ")
a = int(sys.stdin.readline())
listofcoinsoutthere = []
for i in range(1,a+1):
    print('What is your coin number ', i, ', in pence?')
    c = float(sys.stdin.readline())
    listofcoinsoutthere.append(c)


def coinscounterinpence(pence, listofcoins):
    listofcoins = sorted(listofcoins, reverse=True)
    sizeofl = len(listofcoins)
    counter = 0
    for i in range(0, sizeofl):
        while pence >= listofcoins[i]:
            pence = pence - listofcoins[i]
            counter = counter + 1
    return counter


def coinsaveragebelowfivequid(thelistofcoins):
    listofminimums = []
    for g in range(1,500):
        listofminimums.append(coinscounterinpence(g, thelistofcoins))
    return float(sum(listofminimums)/len(listofminimums))


listofaveragesofallpotentialcoinsadded = []
listofallpotentialscoinsadded = []

for i in range(1, 500):
    if i not in listofcoinsoutthere:
        listofcoinsoutthere.append(i)
        listofallpotentialscoinsadded.append(i)
        listofaveragesofallpotentialcoinsadded.append(coinsaveragebelowfivequid(listofcoinsoutthere))
        listofcoinsoutthere.remove(i)

listofaveragesofallpotentialcoinsadded1 = sorted(set(listofaveragesofallpotentialcoinsadded))

listofmosthelpfulcoins = []
for j in listofaveragesofallpotentialcoinsadded1:
    counter = 0
    for i in listofaveragesofallpotentialcoinsadded:
        counter = counter + 1
        if i == j:
            listofmosthelpfulcoins.append(listofallpotentialscoinsadded[counter-1])
    print('Average minimum number of coins required for this range is ', j, ', when these coins are introduced: ', listofmosthelpfulcoins,' into the currency')
    listofmosthelpfulcoins = []


print('press enter')
a = sys.stdin.readline()