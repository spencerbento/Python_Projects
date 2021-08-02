n1 = int(input('Digite um número para saber a sua tabuada: '))
print('A tabuada do',n1, 'é: ')
m = 0
while (m<10):
    print('{} vezes {} é: {}'.format(n1,m+1,n1*(m+1)))
    m = (m+1)
