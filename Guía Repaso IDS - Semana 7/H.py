A = int(input())
edades = []
admitidos = []
for i in range(A):
    edades.append(int(input()))
for edad in edades:
    if edad >= 15:
        admitidos.append(edad)
print(len(admitidos))