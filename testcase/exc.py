def func(*num):
	print (num[3])
	
#numlist=
func(3,43,54,32)

xl = [1,3,4,7]
yl = [3,9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if (x<7)&(y>6)]

print(L)

try:
	y=3/0
except NameError:
	print("name error")
except ZeroDivisionError:
    print("Catch error in the main program")
finally:
	print("other error")

	