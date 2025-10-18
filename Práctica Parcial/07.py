nom = input()
ape = input()
nick = (nom[0:5]+ape[0]).lower()
pin = (len(nom)*1000 + len(ape))%10000
print(f"Nick: {nick}")
print(f"Pin: {pin}")
print(f"ID: C3-{nick}-{pin}")