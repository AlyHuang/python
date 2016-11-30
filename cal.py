
def Pass_Sroce(x):
	if(x<60):
		return False
	else:
		return True





if __name__=="__main__":
	# a=15
	# b=6
	# print(a,"+",b,"=",plus(a,b))
	# print(a,"-",b,"=",suntract(a,b))
	# print(a,"*",b,"=",multiply(a,b))
	# print(a,"/",b,"=",division(a,b))

	# c=[3,4,0.3]
	# d=[8,12,9,12]

	# result=map(plus,c,d)
	# print(*result)
	# print(*map(suntract,[1,4,12,9],[2,6,7,4]))
	sroce={"语文":87,"数学":100,"英语":90,"体育":30}
	standard=filter(Pass_Sroce,sroce.values())
	print (*standard)



