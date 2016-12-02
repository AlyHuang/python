import HTMLTestRunner
import time

	def report(path='./')
		timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
		filename =path+timestr+'.html'
		fp = open(filename,'wb')
		runner = HTMLTestRunner.HTMLTestRunner(
			stream=fp,
			title='result',
			description='report'
		)