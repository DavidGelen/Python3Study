# -*- coding: utf-8 -*-

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
#print('sum = ',sum)	

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print('Apple: %s' % L[0][0])
print('Apple ： ',L[0][0])

# 打印Python:
print('Python : %s' % L[1][1])

# 打印Lisa:
print('Lisa : %s' % L[2][2])

#range(5)生成的序列是从0开始小于5的整数
#通过list()函数可以转换为list
print('data = ',list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
   #print('Hello, %s!' % x)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')   

#continue的作用是提前结束本轮循环，并直接开始下一轮循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: #如果n是偶数，执行continue语句
       continue 
    print(n)






