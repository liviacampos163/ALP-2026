import datetime


nom = input("Digite o nome da primeira pessoa: ")
data_str1 = input("Digite a data de nascimento (dd/mm/aaaa): ")

nom2 = input("Digite o nome da segunda pessoa: ")
data_str2 = input("Digite a data de nascimento (dd/mm/aaaa): ")


data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")


if data1 < data2:
    print(f"{nom} é a pessoa mais velha.")
elif data2 < data1:
    print(f"{nom2} é a pessoa mais velha.")
else:
    print("As duas pessoas têm a mesma data de nascimento.")

