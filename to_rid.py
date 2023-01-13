import matplotlib.pyplot as plt
a = int(input('How many coins do you have in the current system of your country? '))
listofcoinsoutthere = []
for i in range(1,a+1):
    print('What is your coin number ', i, ', in pence?')
    c = float(input(''))
    listofcoinsoutthere.append(c)


def coinscounterinpence(pence, listofcoins):
    listofcoins = sorted(listofcoins, reverse=True)
    counter = 0
    for i in range(0, len(listofcoins)):
        while pence >= listofcoins[i]:
            pence -= listofcoins[i]
            counter += 1
    return counter


def coinsaveragebelowfivequid(thelistofcoins):
    listofminimums = []
    for g in range(1,500):
        listofminimums.append(coinscounterinpence(g, thelistofcoins))
    return float(sum(listofminimums)/len(listofminimums))

print('The average minimum number of coins for values from 1p to £4.99 is ', coinsaveragebelowfivequid(listofcoinsoutthere))

for i in listofcoinsoutthere:
    if i != min(listofcoinsoutthere):
        dummylistt = list(listofcoinsoutthere)
        dummylistt.remove(i)
        print('If you remove ', i, 'pence coin, then the average minimum changes to ', (coinsaveragebelowfivequid(dummylistt)))

print('We do not consider removing 1p in this analysis')
