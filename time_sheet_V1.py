# coding=utf-8
author='ljj'
time='2020-06-08-21:49'
function="Count whether the sign in form is absent"
import pandas as pd 
import numpy as np 
import re
str="一段字符串z首字a段是d否匹配"
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

'''
function:check time sheet of students
file:123.csv
'''
import pandas as pd
#读取签到学生的信息excel文件
csv_path=(r"C:\Users\Administrator\Desktop\1231.xlsx")
datafile=pd.read_excel(csv_path)
#csv_path=(r"C:\Users\Administrator\Desktop\123.csv")
#datafile=pd.read_csv(csv_path,"rb",engine='python',sep=",")#此处“rb”,是为了能够打开gbk编码格式的文件,'engine'=python：利用python打开，读取为1列的问题是因为没有加分隔符(sep='seperator')
df=pd.DataFrame(datafile)
print(df)#输出所有的数据
print(df.index)#输出行索引
print(df.columns)#输出列名称
print(df.head())#默认前五行
print(df.tail())#默认后五行
df=df.dropna(axis=0, how='any', inplace=False)#每一行只要有一个空值就去掉这一行
print(df)#输出所有的数据
#index=df.index.split(',')#行索引按逗号分隔
#print(index)
index=['name','qq','time','device4']#更改列名称
df.columns=index
print(df.columns)#输出更改后的列名
print(type(df.qq))#输出类型，Series数据类型
qq=(df.qq).astype('str')#将数据类型转换为字符串
print(type(qq),qq)#（比如数据是qq号,数值较大会以科学计数出现，不方便）
print(df.qq[7])#输出指定qq列的index为7的元素
print(df.shape)
name_list=[]
for i in range(df.shape[0]):
    print(df.iloc[i,0])#通过位置编号索引来获取所有行的姓名数据
    #print(df.loc[i,['name']])#通过标签值索引数据
    #ix：既可以通过行（列）标签索引数据，也可以通过行（列）位置编号索引数据
    name_list.append(df.iloc[i,0])#获取得到的姓名数据
print(name_list)


#读取学生的名字
name_path=(r"C:\Users\Administrator\Desktop\name.xlsx")   
student_sheet=pd.read_excel(name_path,sheet_name=None)#读取所有的sheet表

allSheet=student_sheet.keys()#通过keys()方法获取所有的表名信息
#print(allSheet)#查看excel中所有的表名信息

sheetname=["计应一","计应二","计应三"]#选取需要获取的表名信息
student_sheet=pd.read_excel(name_path,sheet_name=sheetname)#读取指定sheet表信息，返回的是元组列表，[('元组第一个是sheet表名'，后面是对应表的内容)]
print(student_sheet)#打印3个班级的信息,
print(student_sheet.get('计应一'))#通过get方法获取指定的df
print(student_sheet.get('计应二'))#通过get方法获取指定的df
print(student_sheet.get('计应三'))#通过get方法获取指定的df
name_c12=pd.concat([student_sheet.get('计应一'),student_sheet.get('计应二')],axis=0,ignore_index=True)#横向连接，重建索引,
print(name_c12)#输出计应12班的学生信息
name_c123=pd.concat([name_c12,student_sheet.get('计应三')],axis=0,ignore_index=True)#横向连接，重建索引,
print(name_c123)#输出计应123班的学生信息
ori_student_name=[]#保存计应123班的学生信息名字
for i in range(len(name_c123)):
    name=name_c123.iloc[i,0]#获取学生名字
    print(name)
    ori_student_name.append(name)#保存学生名字为列表
print(ori_student_name)#输出原始学生名单 

#对不符合格式的签到名单进行处理，方面后面缺勤比较,返回的是处理好的数据
#矩阵里面是空格，列表里面是逗号
list=[]#匹配是否是空列表
qinadao_pro=[]
for j in range(len(name_list)):#遍历签到名单列表
    for i in range(len(ori_student_name)):#遍历原始学生名单列表 
            result=re.findall(ori_student_name[i],name_list[j])#长的在后面，短的在前面，在长中找短的字符。
            if  result!=list:
                qinadao_pro.append(result)
print(qinadao_pro)
#print(qinadao_pro.shape)列表没有维度的概念，查看列表维度需转换为矩阵
qinadao_pro_array=(np.array(qinadao_pro))#列表转化为矩阵
print((qinadao_pro_array).shape) 
print((qinadao_pro_array)) 
qinadao_pro_array=np.reshape(qinadao_pro_array,((qinadao_pro_array).shape[0],))#矩阵转化为一维     
print(qinadao_pro_array)
print("矩阵的形状",qinadao_pro_array.shape,"矩阵的维度",qinadao_pro_array.ndim)#
qinadao_proList=qinadao_pro_array.tolist()#一维矩阵转化为列表
print(qinadao_proList)

#学生缺席比较
absence=[]#存储缺席学生
for j in ori_student_name:#遍历原始学生名单列表
    #for i in range(len(ori_student_name)):#遍历原始学生名单列表
      if j not in qinadao_proList:#原始学生名单不是签到表中的就是缺勤
        absence.append(j)      
print(absence,len(absence))
print(type(student_sheet))

while True:
    a=1;
df=pd.DataFrame(name_c123)#将合并数据转换为数据流
file_path=('C:/Users/Administrator/Desktop/1.xlsx')#保存合并的内容
df.to_excel(file_path,sheet_name='Data1',startcol=0, index=False)#表名：Data1；从0列开始，不保存行索引


df1=pd.DataFrame(name_c123)#将合并数据转换为数据流
df2=pd.DataFrame(name_c123)#将合并数据转换为数据流
df3=pd.DataFrame(name_c123)#将合并数据转换为数据流
file_path=('C:/Users/Administrator/Desktop/11.xlsx')#保存合并的内容
#create a Pandas Excel writer using xlswriter 
with pd.ExcelWriter(file_path) as writer:
    df1.to_excel(writer,sheet_name='Data1',startcol=0,index=False)#表名：Data1；从0列开始，不保存行索引
    df2.to_excel(writer,sheet_name='Data2',startcol=0,index=False)#表名：Data2；从0列开始，不保存行索引
    df3.to_excel(writer,sheet_name='Data3',startcol=0, index=False)#表名：Data3；从0列开始，不保存行索引
    print("同一个excel文件中，写入多个sheet")



#同一个excel文件中，写入多个sheet，
#方法：#只要使用pd.ExcelWriter建立一个writer，然后，将df1，df2都使用to_excel（writer, sheet名），最后一次性将这些数据保存，并关闭writer就完成了
#create some Pandas DateFrame from some data
df1=pd.DataFrame({'Data1':[1,2,3,4,5,6,7]})
df2=pd.DataFrame({'Data2':[8,9,10,11,12,13]})
df3=pd.DataFrame({'Data3':[14,15,16,17,18]})
All=[df1,df2,df3]
#create a Pandas Excel writer using xlswriter 
# writer=pd.ExcelWriter('C:/Users/Administrator/Desktop/test1.xlsx')

# df1.to_excel(writer,sheet_name='Data1',startcol=0,index=False)
# df2.to_excel(writer,sheet_name='Data1',startcol=1,index=False)
# df3.to_excel(writer,sheet_name='Data3',index=False)
# writer.save()
# writer.close()

#或者不需要再单独写save和close，自动完成
with pd.ExcelWriter('C:/Users/Administrator/Desktop/test1.xlsx') as writer:
    df1.to_excel(writer,sheet_name='Data1',startcol=0,index=False)
    df2.to_excel(writer,sheet_name='Data1',startcol=1,index=False)
    df3.to_excel(writer,sheet_name='Data3',index=False)
