# Desvios condicionais. IF ELSE
n1 = n2 = 0.0
media = 0.0
print('Esse código solicita duas notas ao usuário, calcula a média e verifica se a média é maior ou igual a 70.\nSe for, imprime uma mensagem de aprovação; caso contrário, imprime uma mensagem de reprovação.\nO código usa um loop infinito (while True) e trata exceções para garantir que o usuário forneça valores numéricos.')
# Inicia um loop infinito
while True: 
    try: 
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        media = (n1 + n2) / 2
        print(f'Suas notas foram {n1} e {n2} e sua média é de {media:.2f}')
        if media >= 70.0:
            print('Parabéns! Você foi aprovado!')
            break
        else:
            print('Infelizmente você não foi aprovado!')
            break
    except:
        # Se ocorrer uma exceção (por exemplo, se o usuário não digitar um número),
        # imprime mensagem de erro e continua o loop.
        print('Erro! Digite um número.')


