#增:创建,添加,

a={}
a["姓名"]='dogi'
print(a)
#改:字典中key唯一且不能改变,元组可以做key,但前提是元组里不能有列表.字典没有下标,无序.
a["姓名"]='皮皮虾'
print(a)
a[(1,2)]='11'
print(a)
#a[(0,[11])]=56
#删除:a.pop(key),清空:clear
a.pop((1,2))
print(a)
#a.clear()
print(a)
#查
print(a["姓名"])
for i in a :
    print("姓名")
#字典的合并
# c={"姓名":'ew',"办卡":"补办"}
# f={"性别":"男"}
# #c.update(f)
# #print(c)
# #合并后原字典没有发生变化.
# print(dict(c,**f))
# print(c)
# print(f)
# #成员判断
# if("姓名" in c):
#     print("hellokugou")
# #长度啊
# print(len(c))