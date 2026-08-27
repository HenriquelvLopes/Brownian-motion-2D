import random
import math
import matplotlib.pyplot as plt

T = int(input("tempo total da simulação: "))
t = 0.01
N = int(T / t)

D = 1
particulas = int(input("número de partículas: "))

trajetorias = int(input("número de trajetórias: "))

pontos_x = []

x_nuvem = []
y_nuvem = []

tempos = [1, 2, 5, 10]

pontos_x = {}

for tempo in tempos:
    pontos_x[tempo] = []

pontos_r = {}

for tempo in tempos:
    pontos_r[tempo] = []

pontos_xy = {}

for tempo in tempos:
    pontos_xy[tempo] = []

def deslocax(x):
    x = x + math.sqrt(2 * D * t) * random.gauss(0, 1)
    return x

def deslocay(y):
    y = y + math.sqrt(2 * D * t) * random.gauss(0, 1)
    return y


for e in range(trajetorias):

    x = 0
    y = 0
    trajetoria_x = []
    trajetoria_y = []

    for i in range(N):

        x = deslocax(x)
        y = deslocay(y)

        trajetoria_x.append(x)
        trajetoria_y.append(y)

        r2 = x**2 + y**2

    plt.plot(trajetoria_x, trajetoria_y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trajetórias Brownianas")
plt.grid()
plt.show()


for p in range(particulas):

    x = 0
    y = 0

    for i in range(N):

        x = deslocax(x)
        y = deslocay(y)

        passo = i + 1

        for tempo in tempos:

            if passo == int(tempo / t):

                pontos_x[tempo].append(x)

                r = math.sqrt(x**2 + y**2)
                pontos_r[tempo].append(r)

                pontos_xy[tempo].append((x, y))

                

for tempo in tempos:

    plt.hist(
        pontos_r[tempo],
        bins=50,
        density=True,
        alpha=0.5,
        label=f"t = {tempo}"
    )

plt.xlabel("r")
plt.ylabel("Densidade de probabilidade")
plt.title("Evolução da distribuição radial")
plt.legend()
plt.grid()
plt.show()

for ponto in pontos_xy[10]:

    x_nuvem.append(ponto[0])
    y_nuvem.append(ponto[1])

plt.scatter(x_nuvem, y_nuvem, s=5)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Nuvem de partículas em t = 10")
plt.axis("equal")
plt.grid()

plt.show()
