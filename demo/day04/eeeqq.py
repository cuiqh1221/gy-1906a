def absuan(a,b):
    print(a+b)
    print(a*b)
    print(a-b)
    print(a/b)
with open("D:\\softwaredata\\pycharm\\guoya1906a\\demo\\day04\\ab.txt") as f:
    flists = f.readlines()
    for i in flists:
        i=i.replace("\n","")
        i=i.split(',')
        absuan(int(i[0]),int(i[1]))

def sum(a,b):
    s=a+b
    print(a,"+",b,"=",s)
    return s
def cha(a,b):
    c=a-b
    print(a,"-",b,"=",c)
    return c
def pel(a,b):
    p=a*b
    print(a,"X",b,"=",p)
    return p
def tto(a,b):
    if(b==0):
        print("除数不能为0")
    else:
        t = a / b
        print(a,"÷",b,"=",t)
        return t

# sum(5,6)
# tto(96,6)
# tto(88,0)
sum(sum(1,2),3)
cha(cha(1,2),2)
pel(pel(5,9),8)
tto(tto(8,6),7)
#无参数,无返回值
def say_hello():
    print("hellokugou")
say_hello()
#有参数无返回值
def say_goodbay(a):
    print(a,'goodbay')
say_goodbay('W')
#无参数,有返回值
def uu_():
    return 'julo'
print(uu_())

#有参数,有返回值
def ff(h1,h2,m3):
    return "{}欠{}{}钱".format(h1,h2,m3)
print(ff("凉凉","qe","好多"))
def gg(k1,k2,k3):
    return '{w1}qian{w2}{w3}qian'.format(w1=k1,w2=k2,w3=k3)
print(gg(11,88,0))
#oooooooooooooooooooooooooooooooooooooooooooooooooooooo
def tto(a,b):
    t = a / b
    print(a,"÷",b,"=",t)
try:
    tto(2,0)
except:


