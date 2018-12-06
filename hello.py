# -*- coding: utf-8 -*-
#print(100 + 200 + 300)
#name = input('please enter your name: ')
#print('hello,', name)
#print('1024 * 768 =', 1024 * 768)

#s = 'Python-中文'
#print(s)
#b = s.encode('utf-8')
#print(b)
#print(b.decode('utf-8'))

#并用字符串格式化显示出'xx.x%'，只保留小数点后1位
#r = 13 / 72
#print('小明成绩提升了：%.1f' % r)
#print('%.2f' % 3.1415926)

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
#print('growth rate: %d %%' % 7)
#print('Hi, %s, you have $%d.' % ('Michael', 1000000))

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
#print('Apple: %s' % L[0][0])
#print('Apple ： ',L[0][0])

# 打印Python:
#print('Python : %s' % L[1][1])

# 打印Lisa:
#print('Lisa : %s' % L[2][2])

age = 3
#注意不要漏写了冒号
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
	
#===========================================

#只要x是非零数值、非空字符串、非空list等
x = 2
if x:
    print('True')	
	
#s = input('birth: ')
#先把str转换成整数
#birth = int(s)
#if birth < 2000:
 #   print('90后')
#else:
 #   print('00后')	
	
#=========================================
	
#请根据BMI公式（体重除以身高的平方）计算BMI指数:	
height = 1.75
weight = 80.5	
bmi = 80.5/ pow(1.75,2)
#print('bmi = %.1f' % bmi)

bmi = 80.5/(1.75 ** 2)
#print('bmi = %.1f' % bmi)

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
	
#============================================

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
#print('sum = ',sum)	

#==================================================

#range(5)生成的序列是从0开始小于5的整数
#通过list()函数可以转换为list

print('data = ',list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
#print(sum)

#计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
#print(sum)

#===================================================

L = ['Bart', 'Lisa', 'Adam']
for x in L:
   #print('Hello, %s!' % x)
   
#=====================================================

#n = 1
#while n <= 100:
    #if n > 10: # 当n = 11时，条件满足，执行break语句
     #   break # break语句会结束当前循环
    #print(n)
    #n = n + 1
#print('END')   

#============================================================

#continue的作用是提前结束本轮循环，并直接开始下一轮循环
#n = 0
#while n < 10:
    #n = n + 1
    #if n % 2 == 0: # 如果n是偶数，执行continue语句
    #   continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    #print(n)

#=================map结构=======================

dd = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#print('dd[\'Michael\'] = ',dd['Michael'])
#print('dd[\'Michael\'] = %d' % dd['Michael'])

#如果key不存在，可以返回None，或者自己指定的value
print('Bob多大岁数呢？',dd.get('Bob'))
print('炮爷多大岁数呢？',dd.get('pao',3))

#通过in判断key是否存在 
'pao' in dd















	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	















