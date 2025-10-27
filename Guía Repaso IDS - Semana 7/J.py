N = int(input())
Pis = []
for i in range(N):
    Pis.append(int(input()))
for Pi in Pis:
    if Pi >= 3:
        print("Ok")
    else:
        print("No")