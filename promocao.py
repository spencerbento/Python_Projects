produdo = float(input('Digite o valor do produto: '))
a = produdo - (produdo*15/100)
p = produdo + (produdo*8/100)
print('O produto que custa R${:.2f}, para pagamento a vista sai por R${:.2f} (15% de desconto!)'.format(produdo, a))
print('Para parcelamento em 8X, o produto que custa R${:.2f}, sairá por R${:.2f} (8% de juros!'.format(produdo, p))