
from functools import reduce

plus = lambda x,y:x+y
suntract = lambda x,y:x-y
multiply = lambda x,y:x*y
def division(x,y):
	try:
		return (lambda x,y:x/y)
	except ZeroDivisionError:
		print("不能除零") 
		return False

#=============获取计算方法================
def calmethod():
	operator = {'1':plus,'2':suntract,'3':multiply,'4':division} 
	while True:
		try:
			a=input("请输入计算方法：\n 1. 求和 \n 2. 减法 \n 3. 乘法 \n 4. 除法\n")
			return operator[a]
		except Exception:
			print("输入错误！请重新输入数字（1-4）") 

	

#输入方法1：使用循环依次获取输入
# list=[]
# for i in range(10):
	# list.append(int(input("请输入数字（用换行分隔）：")))
	# print(list)
	
#输入方法2：使用输入后字符分隔，这个方法更好
#=============获取数字输入================
def numberinput():
	while True:
		try:
			str=input("请输入数字（用空格分隔）：") 
			list=[float(i) for i in str.split()] #将输入的字符串以空格分隔，再转变为数字列表
			return list
		except ValueError:
			print("输入错误！请重新输入数字（用空格分隔）") 
		except Exception:
			print("出现错误，请联系管理人员")


		
def reduce_cal(methodname,list):
	try:
		result=reduce(methodname,list)
		return result
	except ZeroDivisionError:
		return False
	except Exception:
		print("出现错误，请联系管理人员")

if __name__=="__main__":
	methodname=calmethod()

	while True:
		list=numberinput()
		result=reduce_cal(methodname,list)
		if result!=False:
			break
		
	print("结果是：",result)