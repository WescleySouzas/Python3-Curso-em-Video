num = int(input('Digite um numero: '))

print('Soma:')
for i in range(10):
    print(f'{i} + {num} = {num + i}  ')
print('-'*10)
print('Subtração:')
for i in range(10):
    print(f'{i} - {num} = {num - i}')
print('-'*10)

print('Mutiplicação:')
for i in range(10):
    print(f'{i} * {num} = {num * i}')
print('-'*10)

print('Divisao:')
for i  in range(10):
    print(f'{i+ 1} % {num} = {num / (i+ 1)}')