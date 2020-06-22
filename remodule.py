# coding=utf-8
author = 'ljj'
time = '2020-06-08-21:49'
function = "Count whether the sign in form is absent"
rel_csdn = "https://blog.csdn.net/l641208111/article/details/106867207"
str = "一段字符串z首字a段是d否匹配"
import pandas as pd
import numpy as np
import re

# ^ ：
#检测字符串开始字符是否匹配，如果匹配，返回字符列表，如果不匹配，返回空列表
result=re.findall('^段字符',str)
print(result)#不匹配，返回空列表：[]

result=re.findall("^一段字符",str)
print(result)#匹配，返回匹配的字符列表['一段字符']

#^元字符   ①如果写到[]字符集里就是反取；②可以在[]中添加多个^字符；③匹配方式是以单个字符匹配，而非字符串。

result=re.findall("[^一段字符,^a-z]",str)
print(result)#匹配，结果：['串', '首', '是', '否', '匹', '配']

 #$元字符   以什么结尾
import  re
str="匹配s规则这s个字符串是否s匹配f规则则re则则则"
result=re.findall("则$",str)
print(result) #字符串结束位置与则符合就匹配，否则不匹配，返回值是list，结果：['则']

result=re.findall("[匹配]",str)
print(result) #字符串结束位置与则符合就匹配，否则不匹配，返回值是list，结果：['则']

print(np.zeros((2,3,4)))

###########findall:找到匹配的所有子串############################
import re
line="this hdr-biz model server args= server"
patt=r'server'
pattern = re.compile(patt)
result = pattern.findall(line)
print(result)
###############match:起始位置匹配字符串#############################
line="this hdr-biz 123 model server 456"
pattern=r"123"
matchObj = re.match( pattern, line)
print(matchObj)
#############search：扫码整个字符串，返回第一个匹配#######################
line="this hdr-biz model server"
pattern=r"hdr-biz"
m = re.search(pattern, line)
print(m,m.groupdict())
###########finditer：找到匹配的所有子串，返回迭代器######################
it = re.finditer("\d+","12a32bc43jf3")
for i in it:
    print(i)#匹配的内容
    print(i.group)#匹配的数据
    print(i.group(0))#匹配的第一个数据
    print(i.span())#匹配数据的序号
################################