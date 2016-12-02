a=8
b=0
print(a,type(a))
if a>(-1):
	a=a+1
else:
	b=4
print (a,b)

sroce={"语文":87,"数学":100,"英语":90,"体育":30}

print (sroce)
print (sroce.keys())
print (sroce.values())
del sroce["语文"]
print (sroce)
f=open("1.txt","r")
f2=open("2.txt","r+")
for line in open("1.txt"):  
    #line =f.readline()  
	f2.write(line)

f.close()
f2.close()


f3=open("2.txt","r")
showlines=f3.readlines()
print (showlines,"showlines")
show=f3.read(100)
print (show)


