'''
Para a7=0 enquanto a7 menor que 10, incrementando 1, insira um outro while aninhado internamente contendo para a8=0 até
a8 menor que 10, incrementando 1, mostre na tela "(a7,a8)".
'''

a7 = 0
a8 = 0
while a7 < 10:
    a7 += 1
    while a8 < 10:
        a8 += 1
print(a7, a8)
print('(a7,a8)')