import re
import time
import os

'''
 替换文件中的字符
'''
# f=open("record.txt",'r')
# f1=open("newrecord.txt",'w')
# for i in f.readlines():
	# re.sub('\n','',i)
	# f1.writelines(i)

# f.close()
# f1.close()


# f1=open("newrecord.txt",'r')
# for i in f1.readlines():
	# print(i)
# f1.close()

def renamefile(oldfilename):
	oldfilename=file.name
	file.close()
	m=re.search("output_(?P<year>\d{4}).(?P<month>\d{2}).(?P<day>\d{2})", oldfilename)
	datestr=(m.group("year")+m.group("month")+m.group("day"))
	st=time.strptime(datestr,'%Y%m%d')
	l=time.strftime("%Y-%m-%d-%w",st)
	filename="output_"+l+".txt"
	print(filename)
	os.rename(oldfilename,filename)
	file.close()

print( time.strftime('%Y%m%d-%H%M%S', time.localtime() ))


