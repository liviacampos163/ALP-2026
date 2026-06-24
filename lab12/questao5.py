import random
import time 

V= random.randint(0,10)

print('numero sorteado:',V)

for i in range(1,V + 1):
    print(f"volta {i}: mais uma volta!")
    time.sleep(1)