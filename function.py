import time
class time1(object):
	def __init__(self):
		print ( "==========init============")
		
	def learYear(y):
		if (y%4==0):
			return True
		else:
			return False
		

class time2(time1):
	def GetNowTime():
		return time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))

if __name__ == '__main__':
	timename1 =time1()
	timename2 =time2()
	print(timename1.learYear(2000))
	print(time2.GetNowTime())
