def juge3_2(a):
    #a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''

    #字符串的替换
    a = a.replace("''",'"')
    #字符串截取
    a = a[2:-2]

    #print(a)

    #字符串的切片方法

    b = a.split('" , "')

    #print(b)

    #key 唯一；并且存一对数据
    #key存牌的大小，value存key出现的次数
    #{'1':3,"10":1,"7":2}
    #b=['D1', 'H1', 'H10', 'H7', 'S1', 'S7']
    c={}#字典
    for i in b:
        d=i[1:]#截取每个值的第二个值1,1,10,7,1,7
        #print(i[1:])
        if(d in c):#如果第二个值在c字典有
            c[d] +=1#则加上一次
        else:#如果字典里没有那些数字(第二个值)
            c[d]=1#则写上1
    #print(c)#{'1': 3, '10': 1, '7': 2}
    value_list = list(c.values())
    #print(value_list)
    if(3 in value_list and 2 in value_list):
        print("可以三代二")
    else:
        print("不可以三代二")
# open 是python的一个内置函数,作用是打开一个函数:文件路径,文件打开模式r只读,w可写,a可读写.路径如果有\要加一个
#\来区分换行符,with open 方法在打开文件出错时,释放资源.
# with open("D:\\softwaredata\\pycharm\\guoya1906a\\demo\\day04\\carddd.txt","r") as f:
# #readlines是把文件读出来并且存一个list中,read是读出来存到一个字符串中去.
#     lines = f.readlines()
# #循环遍历这个列表
#     for line in lines:
#         print(line)
# #把末尾换行符替换为空,也就是去掉换行符.
#         line=line.replace('\n','')
# #调用一个方法,判断是否能三代二
#         juge3_2(line)
with open("D:\softwaredata\pycharm\guoya1906a\demo\day04\carddd.txt") as g:
    g.lists = g.readlines()
    print(g.lists)
    for g.list in g.lists:
        g.list=g.list.replace("\n","")
        print(g.list)
        juge3_2(g.list)

