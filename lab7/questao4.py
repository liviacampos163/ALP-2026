import random
chances = 5
num_secreta = 'random.randint(1, 10)'
while chances > 0: 
    num = input(f"Qual o numero secreto? Você tem {chances} chances")
    chances -= 1
    if num == 'random.randint(1, 10)':
        print("Você acertou o numero, parabens!!!!!!!!!!!")
        break   
print(random.randint(1, 10))
