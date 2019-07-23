b='https://www.baidu.com/s?wd=qwq%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D%E7%BD%91%E7%BB%9C%E7%94%A8%E8%AF%AD&rsv_spt=1&rsv_iqid=0x961fa9280009f810&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=3&rsv_sug1=2&rsv_sug7=100&rsv_t=0120JUZXuvalTNZCnhiXNlH2T9yJOP2D7v6%2F2I99GzfoSpNJ2QtA%2BSvAxOwhZQw6rJGs&rsv_sug2=1&prefixsug=qwq&rsp=0&inputT=1446&rsv_sug4=1446'
xieyi=b.split('://')[0]
print(xieyi)
b=b.split('://')[1]
yuming=b[:b.find('/')]
print(yuming)
uri=b[b.find('/'):]
print(uri)
# --------------------------------------------------------
c='http://qa.yansl.com:8080/admincreate'
xieyione=c.split('://')[0]
print(xieyione)
c=c.split('://')[1]
yumingtwo=c[:c.find('/')]
print(yumingtwo)
uriii=c[c.find('/'):]
print(uriii)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
d='https/www.qasjjf.com'