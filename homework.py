#!/usr/bin/python
#-*-coding:utf-8-*-

# def leadyear(y):
		# if y%4==0:
			# print(y,"is lead year!")
		# else:
			# print(y,"isn't lead year!")

# y=int(input("输入年份："))
# leadyear(y)

def Pass_Sroce(x):
	if(x<60):
		return False
	else:
		return True

def sp(str):
	return str.startswith("L")
'''
读取文本并输出为列表
'''
f=open("record.txt","r")
name_age={}
name_sroce={}
for i in f.readlines():
	j=(i.split("\n"))
	list=j[0].split(",")
	name_age[list[0]]=int(list[1])
	name_sroce[list[0]]=int(list[2])

standard=filter(Pass_Sroce,name_sroce.values())
print (*standard)
namex=filter(sp,name_sroce.keys())
print (*namex)
print (sum(name_sroce.values()))

print (*filter(any,name_sroce.keys()))

a="34.5"
print(a.isdigit())

	

	

	

	