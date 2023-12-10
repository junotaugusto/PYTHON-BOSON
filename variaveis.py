print('Variável é uma área na memória do computador reservada que contém, no caso, a string em questão.')
print('')
estado = True
nome = 'Junot' 
nome_usuario = input('Digite seu nome: ')
print('')
print(nome)
print('Print é uma função. Toda função tem os parênteses e dentro dos parênteses insere-se os argumentos que esta função vai usar.')
print('')
print(f'Seu nome é {nome_usuario}')
print('='*193)
media = 0
print('Variáveis dos tipos numéricos não possuem aspas. Se eu precisar declarar várias variáveis diferentes, mas que contém o mesmo valor, python permite isso')
n1 = n2 = n3 = n4 = n5 = 0.0
print(n1, n2)
print('Escrevendo variáveis do tipo diferente')
seu_nome, idade = 'Lucas', 23
print(f'Seu nome é {seu_nome} e você tem {idade} anos')
print('='*193)
print('Imprimindo os tipos de variáveis com a função type()')
print(type(media))
print(type(n2))
print(type(seu_nome))
print(type(estado))
print(type(1+2j)) #Os números complexos são úteis em muitos contextos matemáticos, como na solução de equações que envolvem raízes quadradas de números negativos. Em Python, você pode realizar operações aritméticas, como adição, subtração, multiplicação e divisão, com números complexos da mesma forma que faria com números reais.

print('='*193)
print('A função isinstance() é uma função em Python que é usada para verificar se um objeto pertence a uma determinada classe ou tipo de dado. Ela retorna True se o objeto for uma instância da classe especificada e False caso contrário. ')
a = 10
b = 'Sol'
print(isinstance(a, int)) #True 

