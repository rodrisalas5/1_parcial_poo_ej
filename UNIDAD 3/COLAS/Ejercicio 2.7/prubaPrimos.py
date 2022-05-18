i = 1
n = 1

for i in range(1, 100):
    contador_divisores = 0
    for n in range(1, 100):
        if i % n == 0:
            contador_divisores = contador_divisores + 1
    if contador_divisores == 2:
        print(f"{i} es primo")