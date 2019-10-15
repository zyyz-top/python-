'''
函数和模块的使用
'''
'''
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1,m + 1):
	fm *= num
fn = 1
for num in range(1,n + 1):
	fn *= num
fmn = 1
for num in range(1,m - n + 1):
	fm *= num
print(fm // fn // fmn)
'''

'''
定义函数
def
'''
'''
def factorial(num):
	"""求阶乘"""
	result = 1
	for n in range(1,num + 1):
		result *= n
	return result


m = int(input('m = '))
n = int(input('n = '))
#当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(factorial(m) // factorial(n) // factorial(m - n))
'''

'''
函数的参数
'''
'''
from random import randint

def roll_dice(n=2):
	"""摇色子"""
	total = 0
	for _ in range(n):
		total += randint(1,6)
	return total

def add(a=0,b=0,c=0):
	"""三个数相加"""
	return a + b + c

#如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
#摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
#传递参数时可以不按照设定的顺序进行传递
print(add(c=50,a=100,b=200))
'''

#在参数名前面的*表示args是一个可变参数
'''
def add(*args):
	total = 0
	for val in args:
		total += val
	return total

#在调用add函数是可以传入0个或多个参数
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))
'''
'''
def foo():
	print('hello,world!')

def foo():
	print('goodbye,world!')

foo()
'''

'''
练习1:实现计算求最大公约数和最小公倍数的函数
'''
'''
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)
'''

'''
练习2：实现判断一个数是不是回文数的函数
'''
'''
def is_palindrome(num):
	"判断一个数是不是回文数"
	temp = num
	total = 0
	while temp > 0:
		total = total * 10 + temp % 10
		temp //= 10
	return total == num	
'''

'''
练习3：实现判断一个数是不是素数的函数
'''
'''
def is_prime(num):
	"判断一个数是不是素数"
	for factor in range(2,num):
		if num % factor == 0:
			return False
	 return True if num != 1 else False
'''

'''
练习4：写一个程序判断输入的正整数是不是回文素数
'''
'''
if __name__ == '__main__':
	num = int(input('请输入正整数:'))
	if is_palindrome(num) and is_palindrome(num):
		print('%d是回文素数' % num)
'''	

'''
#Python中有关变量作用域的问题
def foo():
	b = 'hello'

	#python中可以在函数内部再定义函数
	def bar():
		C = True
		print(a)
		print(b)
		print(c)

	bar()
	#print(c) #NameError:name 'c' is not defined

if __name__ == '__main__':
	a = 100
	#print(b) #NameError: name 'b' is not defined
	foo()
'''

'''
def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
'''

'''
def main():
    # Todo: Add your code here
    pass

if __name__ == '__main__':
    main()
'''