saldo = print('Bem vindo ao banco MUNDIAL!\n Seu saldo é de: R$ 1000.00')
dinheiro = 1000
print(''' Digite a operação desejara:
[ 1 ] SAQUE
[ 2 ] DEPOSITO''')
op = float(input('Digite a operação: '))
if op == 1:
    print('SAQUE')
    saque = float(input('Digite o valor para o saque: '))
    saldo = (dinheiro - saque)
    print('Seu saldo é de R$ {:.2f}'.format(saldo))
if op == 2:
    print('DEPOSITO')
    deposito = float(input('Digite o valor do depósito: '))
    saldo = (dinheiro + deposito )
    print('Seu saldo agora é de R$ {:.2f}'.format(saldo))
else:
    print('Opção inválida')
