N = int(input())
nombres = []

for i in range(N):
    nombres.append(input())
    
for n in nombres:
    if len(n) <= 6:
        print("No vale la pena")
    elif len(n) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    else:
        print("Dios no creo aguantar esta vez")