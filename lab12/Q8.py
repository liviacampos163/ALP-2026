import datetime



nom2 = input("Digite o nome da segunda pessoa: ")
data_str2 = input("Digite a data de nascimento (dd/mm/aaaa): ")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")

hoje= datetime.datetime.now()

dia= hoje.day
mes=hoje.month
ano= hoje.year

dife=hoje -  data2

if data2 < hoje :
    print(f"seu aniversario esta proximo!!!!")
else:
    print(f"{nom2} seu aniversario esta longe :(")
