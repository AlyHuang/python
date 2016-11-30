import function
#from function import time2
from function import *

a=3
i=0
b=0
while (a>i):
	i=i+1
	print (i,a)

while (b<15):
	b=b+1
	if b==10:
		b=b+2
	print (b)
	
f1=open("1.txt","r")
f2=open("2.txt","w")
for line in f1.read():
	#line=f1.readline()
	f2.write(line)
f1.close
f2.close

f2=open("2.txt","r")
lines=f2.read()
print(lines) 
f2.close

print(time1.learYear(2000))
print(time2.GetNowTime())



	