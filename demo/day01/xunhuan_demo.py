for i in range(50):
    if(2*i+1<100):
        print(2 * i + 1)
for i in range(50):
    print(i)
# --------------------
for i in range(1,10):
    for f in range(1,i+1):

        print(f,"*",end="")
        print(i,'\t',end="")
        print("=",f*i)
    print()
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"X",i,"=",i*j,'\t',end="")
    print()
# -------
for i in range(2,101):
    for j in range(2,i):
        if(i%j==0):
            break
        print(i)
# -----------
num=[];
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)








