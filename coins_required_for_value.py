a = int(input('How many coins do you have in the current system in your country? '))
b = float(input('Minimum number of coins for what value in pounds do you want to count up to ?'))

lista=[]
for i in range(1,a+1):
    print('What is your coin number ', i, ', in pounds?')
    c = float(input(''))
    lista.append(c)

lista.sort()
lista.reverse()

newlista = [i*100 for i in lista]
thecoin = 100*b

counter = 0

for i in newlista:
    while thecoin>=i:
        counter = counter + 1
        thecoin = thecoin - i

print('')
print('')
print('')
print('')
print('Using your coinage system, it takes ', counter, ' coins to get to ', b)