'''
把爬取到的网页数据通过正则表达式把oid信息提取出来,然后存在一个字典再放入到文件里
'''
import re
filename = 'oid1.txt'
oid_dict = {}
list_oid_name = []
with open(filename,'r',encoding='utf-8') as fp:
    datatxt = fp.read()
ex = r'-1">(.*?)<'
list_oid_name = re.findall(ex,datatxt,re.S)
print(list_oid_name)
print(len(list_oid_name))
list_oid_value = []
ex2 = r'-2">(.*?)<'
list_oid_value = re.findall(ex2,datatxt,re.S)
print(list_oid_value)
print(len(list_oid_value))
#list_name_list中的值作为key存到oid_dict中
oid_dict = dict(zip(list_oid_name,list_oid_value))
print(oid_dict)
