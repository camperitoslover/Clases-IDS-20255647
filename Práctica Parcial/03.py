X = int(input())
A = input()
B = input()
n1 = (len(A)/X).__round__()
n2 = (len(B)/X).__round__()
p1 = A[:n1]
p2 = B[-n2:]
print(f"{p1+p2}")