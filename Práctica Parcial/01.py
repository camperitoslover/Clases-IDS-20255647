correo = input()
c1 = correo.count("@")==1
c2 = correo.index("@")>=3
c3 = correo.count(".")>=1
c4 = correo.count(" ")==0
c5 = correo[0]!="."
c6 = correo[-1]!="."
print(c1 and c2 and c3 and c4 and c5 and c6)