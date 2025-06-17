print("Criba de Eratóstenes")

N = list(range(1, 101))
B = [True] * 100
B[0] = False

for i in range(1, 99):
    for j in range(i+1, 100):
        if N[j] % N[i] == 0:
            B[j] = False

for i in range(100):
    if B[i]:
        print(N[i], end=" ")