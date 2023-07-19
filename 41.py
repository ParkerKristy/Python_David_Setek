import random
import math

print("Vítejte v aplikaci na hod mincí!")
#coin = (math.floor(random.random() *2))


coin = random.randint(0,1)

if coin == 0:
    print("Hlava")
else:
    print("Orel")

