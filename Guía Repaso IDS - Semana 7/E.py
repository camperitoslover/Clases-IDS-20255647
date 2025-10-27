N = int(input())
P = input().split()
Pa = int(P[0])
Pb = int(P[1])
Pc = int(P[2])
combos = []
for i in range(N):
    combos.append(input().upper())
for C in combos:
    Da = C.count("A")
    Db = C.count("B")
    Dc = C.count("C")
    daño = ((Pa*Da) + (Pb*Db) + (Pc*Dc))
    print(daño)