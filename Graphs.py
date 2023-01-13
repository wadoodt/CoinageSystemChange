import matplotlib.pyplot as plt
a = int(input('How many coins do you have in your country? '))

lista=[]
for i in range(1,a+1):
    print('What is your coin number ', i, ', in pounds?')
    c = float(input(''))
    lista.append(c)

lista.sort()
lista.reverse()


newlista = [i*100 for i in lista]

listforgraph = []
minimumcoins = []
for x in range (1, 500):
    listforgraph.append(x/100)
    thecoin = x

    counter = 0

    for i in newlista:
        while thecoin>=i:
            counter = counter + 1
            thecoin = thecoin - i
    minimumcoins.append(counter)

plt.plot(listforgraph, minimumcoins)
plt.xlabel('Values (£)')
plt.ylabel('Minimum N of coins required')
plt.title('Graph for Min N of Coins required')
plt.show()