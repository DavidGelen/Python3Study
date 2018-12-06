# -*- coding: utf-8 -*-

print(100 + 200 + 300)
name = input('please enter your name: ')
print('hello,', name)
print('1024 * 768 =', 1024 * 768)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#并用字符串格式化显示出'xx.x%'，只保留小数点后1位
r = 13 / 72
print('小明成绩提升了：%.1f' % r)
print('%.2f' % 3.1415926)

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)
print('Hi, %s, you have $%d.' % ('Michael', 1000000))


age = 3
#注意不要漏写了冒号
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#只要x是非零数值、非空字符串、非空list等
x = 2
if x:
    print('True')	
	
s = input('birth: ')
#先把str转换成整数
birth = int(s)
if birth < 2000:
    print('90后')
else:
    print('00后')		
	
#请根据BMI公式（体重除以身高的平方）计算BMI指数:	
height = 1.75
weight = 80.5	
bmi = 80.5/ pow(1.75,2)
#保留一位小数
print('bmi = %.1f' % bmi)

bmi = 80.5/(1.75 ** 2)
#保留一位小数
print('bmi = %.1f' % bmi)

if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
	print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')	

	






 














	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	















