#!/usr/bin/python
#-*-coding:utf-8-*-
#五险一金计算器
def Get_Sarary():
	#operator = {'1':standard,'2':personal} 

	while True:
		try:
			Sarary=input("请输入税前工资：")
			Sarary=float(Sarary)
			if Sarary<=0:
				print("工资输入错误,请重新输入！")
				continue
			while True:
				a=input("计算方法：\n 1. 标准五险一金和税收 \n 2. 计算五险一金 \n 3. 计算税收\n 4. 自定义\n 请选择：")
				a=int(a) 
				if (a<=0)or(a>4):
					print("类型选择错误,请重新输入！")
					continue
				else:
					return Sarary,a
		except Exception:
			print("输入错误,请重新输入！") 
			
def Personal_Tax(sarary,low_sarary):
	Ts=sarary-low_sarary
	if Ts<=0:
		return 0
	elif Ts<=1500:
		return Ts*0.03
	elif Ts<=4500:
		return Ts*0.1-105
	elif Ts<=9000:
		return Ts*0.2-555
	elif Ts<=35000:
		return Ts*0.25-1005
	elif Ts<=55000:
		return Ts*0.3-2755
	elif Ts<=80000:
		return Ts*0.35-5505
	else:
		return Ts*0.45-13505
	

def test_mothod(sarary,Endowment,Medical,Job,Fund,flag):
	ed_in=sarary*Endowment
	me_in=sarary*Medical
	job_in=sarary*Job
	fund_h=sarary*Fund
	Lost=ed_in+me_in+job_in
	if flag==True:
		tax=Personal_Tax(sarary-Lost-fund_h,3500)
	else:
		tax=0
	fact_sarary=sarary-Lost-fund_h-tax
	return sarary,ed_in,me_in,job_in,Lost,fund_h,Lost+fund_h,tax,fact_sarary
	
def FiveOne(sarary,method):
	Endowment=0.08
	Medical=0.02
	Job=0.002
	Fund=0.08
	
	if method==1:
		return test_mothod(sarary,Endowment,Medical,Job,Fund,True)
	elif method==2:
		return test_mothod(sarary,Endowment,Medical,Job,Fund,False)
	elif method==3:
		return test_mothod(sarary,0,0,0,0,True)
	elif method==4:
		while True:
			try:
				Endowment=float(input("请输入养老险%："))
				Medical=float(input("请输入医疗险%："))
				Job=float(input("请输入失业险%："))
				Fund=float(input("请输入公积金%："))
				return test_mothod(sarary,Endowment*0.01,Medical*0.01,Job*0.01,Fund*0.01,True)
			except Exception:
				print("输入错误,请重新输入！") 
	else:
		print("程序有问题，请联系开发人员")
		

if __name__=="__main__":
	print("=========================================")
	print("=============五险一金&税收===============")
	(x,y)=Get_Sarary()
	list=FiveOne(x,y)
	print("================纳税情况=================")
	show = ["税前工资","养老险","医疗险","失业险","保险缴纳","公积金","五险一金","纳税","税后工资"]
	i=0
	while(i!=len(show)):
		print(show[i],"%.2f" %list[i])
		i=i+1
	if list[len(list)-1]>50000:
		print("=========================================\n=\t\t\t\t\t=\n=\t土豪,留个号码交个朋友呗！\t=\n=\t\t\t\t\t=\n=========================================")
		
	






