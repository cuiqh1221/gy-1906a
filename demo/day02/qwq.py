i=1
s=0
while(i<=100):
    s=s+i
    i=i+1
print(s)
s=0
k=1
while(k<=1000):
    s=s+k
    k=k+1
print(s)
s=0
i=1
while(i<=10):
    s=s+i
    i=i+1
print(s)
x=1
y=1
while(x<=10):
    y=y*x
    x=x+1
print(y)
b=[1,8,3,2,5,5,2,0,6,0,8]
print(b[0:3])
print(b[2:8])
print(b[-2:-1])
print(b[-4:-2])


a='''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
a=a[1:-1]
print(a)
a_li=a.split('" , "')
print(a_li)

#截取
b='1,2,6,7,8,6'

split = a.split('://')
