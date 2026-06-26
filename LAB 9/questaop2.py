soma = 0
produto = 1
valor = int(input("Digite um valor: "))
cont = 1
while (cont <= valor):
    if soma<=valor:
        break
    soma += cont
    if cont % 2 == 0:
        produto *= cont
    cont += 1
print(soma,produto)

