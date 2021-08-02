n = float(input('Digite um valor em metros: '))
c = (n*100)
mm = (n*1000)
dm = n/10
dc = n*10
hm = n/100
km = n/1000
print('{:.0f}m equivalem a {:.0f} centímetos'.format(n, c))
print('{:.0f}m equivalem a {:.0f} milímetros'.format(n, mm))
print('{:.0f}m equivalem a {:.0f} decímetros'.format(n, dc))
print('{:.0f}m equivalem a {:.2f} hectômetros'.format(n, hm))
print('{:.0f}m equivalem a {:.2f} kilometros'.format(n, km))