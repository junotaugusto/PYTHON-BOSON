print(' ')
print('Operador AND:\nO operador and é um operador lógico que retorna True se ambas as condições à esquerda e à direita forem verdadeiras.\nSe pelo menos uma delas for falsa, o resultado será False. Aqui está um exemplo:')
a = True
b = False
resultado = a and b
print(resultado)  # Saída: False
print(' ')
print('Operador OR:\nO operador or é um operador lógico que retorna True se pelo menos uma das condições à esquerda ou à direita for verdadeira.\nSe ambas forem falsas, o resultado será False. Aqui está um exemplo:')
a = True
b = False
resultado = a or b
print(resultado)  # Saída: True

print(' ')
print('Operador NOT:\nO operador not é um operador unário que inverte o valor de uma expressão lógica. Se a expressão for verdadeira, not a tornará falsa, e vice-versa. Aqui está um exemplo:')
a = True
resultado = not a
print(resultado)  # Saída: False
print('\nVocê pode combinar esses operadores para criar expressões lógicas mais complexas. Por exemplo:')
idade = int(input('Digite sua idade: '))
tem_cartao = True

if idade >= 18 and tem_cartao:
    print("Você pode comprar este produto.")
else:
    print("Você não atende aos requisitos para comprar este produto.")
