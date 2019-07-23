for i in [1,60,30,90,100,20,70,59,69,71,80,84]:
    if(i>80):
        print(i,"成绩为优秀")
    if(i<=80 and i>70):
        print(i,"成绩为良好")
    if(i<=70 and i>=60):
        print(i,"成绩为及格")
    if(i<60):
        print(i,"成绩为不及格")
# ---------------------------------------------
b=1
for i in [90,100,16,84]:

    if(i<80):
           b=2
if(b==1):
    print("全优秀")
else:
    print("不全优秀")
# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

s=0
b=0
a="01010010001110001001001010101010010101"
for i in a:
    if(i=='0'):
        s=s+1
    else:
        b=b+1
# print("有",s,'个0',"有",b,'个1')
s=0
for i in range(1,101):
    while i<101:
        s=i+s
print(s)
#a=0
#for i in range(1,101):
    #a=a+i
#print(a)
s=0
j=1
while(i<=100):
    s=s+i
    i=i+1
print(s)





