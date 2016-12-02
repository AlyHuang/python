s = 'abcdefghijk'
for i in range(0,len(s),2):
    print (s[i])
	
for (index,char) in enumerate(s):
    print (index,char)
	
	
sroce={"语文":87,"数学":100,"英语":90,"体育":30}
index,char=zip(*sroce)
print (index,char)


def test(y):
	if y<20:
		yield y
	if y<10:
		yield y*2
	yield y+2
			
for i in test(9):
	print(i)

a=test(9)
print(type(a))