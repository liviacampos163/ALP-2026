for i in range(1,5):
    print(i*20)

soma = '0'
for num in range(10):
    soma = soma+ num
print('soma:',soma)


for num in range (3):
    print (f"o dobro de {num}e:")
print (num * 2)
#erro de sintaxe falta de parenteses no range 3 e nos prints e a indentaçao no ultimo print


import random

numero= random.randint(1,10)
for i in range (3):
    n=input('advinhe o numero:')
    if n == numero:
        print('correto')
        break

    #nao importou o random