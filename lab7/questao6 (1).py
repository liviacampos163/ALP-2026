print('cardapio :)')
print('1. açaí 300ml - R$12')
print('2.Mousse - R$6,50')
print('3.Salada de frutas - R$10')
print('4.fechar conta')

somador=+1
while True:
    num= int(input('digite um numero para escolher o que deseja'))
    if num==0: break

    if num ==1:
           print('açaí 300ml - 12')
    if num==2:
        print('mousse - 6,50')
    if num == 3:
        print('3. salada de frutas - R$10')
    if num == 4: break
print('fechar conta')
    
