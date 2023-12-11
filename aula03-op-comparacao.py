x = y = z = False #Variáveis do tipo booleano.
n1 = n2 = 0

print('Digite um número: ')
n1 = int(input())
n2 = int(input('Digite outro número:\n'))
print(f'\nVocê escolheu os números {n1} e {n2}. Vamos analisá-los.\n')

x = n1 == n2
print(f'{n1} e {n2} são números iguais? -> {x} \n')
y = n1 > n2
print(f'{n1} é maior que {n2}? -> {y} \n')
z = n1 != n2
print(f'{n1} é diferente de {n2}? -> {z} \n')
