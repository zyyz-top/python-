'''
s1 = 'hello,world!'
s2 = 'hello,world!'
#以三个双引号或单引号开头的字符串可以拆行
s3 = """
hello,
woeld!
"""
print(s1,s2,s3,end='')
'''

'''
\n表示换行，\t表示制表符,表示'要写成\'，表示\要写成\\
'''
'''
s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'
print(s1,s2,end='')
'''
'''
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a87\u789a'
print(s1,s2)
'''

#在字符串最前加上r表示'\'不表示转义
'''
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
'''

'''
s1 = 'hello' * 3
print(s1) #hello hello hello
s2 = 'world'
s1 += s2
print(s1) #hello hello hello world
print('ll' in s1) #True
print('good' in s1) #False
str2 = 'abc123456'
#从字符串中取出指定位置的字符(下标运算)
print(str2[2]) #c
print(str2[2:5]) #c12
print(str2[2:]) #c123456
print(str2[2:2]) #c246
print(str2[::2]) #c246
print(str2[::-1]) #654321cba
print(str2[-3:-1]) #45
'''

'''
#字符串处理
str1 = 'hello,world!'
#通过内置函数len计算字符串的长度
print(len(str1)) #13
#获得字符串首字母大写的拷贝
print(str1.capitalize()) #Hello,world!
#获得字符串每个单词首字母大写的拷贝
print(str1.title()) #Hello,World!
#获得字符串变大写后的拷贝
print(str1.upper()) #HELLO,WORLD!
#从字符串查找子串所在位置
print(str1.find('or')) #8
print(str1.find('shit')) #-1
#与find类似但找不到子串时会引发异常
#print(str1,index('or'))
#print(str1,index('shit'))
#检查字符串是否以指定的字符串开头
print(str1.startswith('He')) #False
print(str1.startswith('hel')) #True
#检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) #True
#将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50,'*'))
#将字符串以指定的宽度靠居右放置左侧填充指定的字符
print(str1.rjust(50,' '))
str2 = 'abc123456'
#检查字符串是否由数字构成
print(str2.isdigit()) #False
#检查字符串是否是由字母构成
print(str2.isalpha()) #False
#检查字符串是否是由数字和字母构成
print(str2.isalnum()) #True
str3 = '   jackfrued@126.com '
print(str3)
#获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
'''

'''
#格式化字符串
a , b = 5 , 10
print('%d * %d = %d' % (a,b,a * b))

a , b = 5 , 10
print('{0} * {1} = {2}'.format(a , b , a * b))

a , b = 5 , 10
print(f'{a} * {b} = {a * b}')
'''

'''
#定义列表、遍历列表以及列表的下标运算
list1 = [1,3,5,7,100]
print(list1) #[1,3,5,7,100]
#乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) #['hello', 'hello', 'hello']
#计算列表长度(元素个数)
print(len(list1)) #5
#下标(索引)运算
print(list1[0]) #1
print(list1[4]) #100
#print(list1[5]) # IndexError: list index out of range
print(list1[-1]) #100
print(list1[-3]) #5
list2[2] = 300
print(list1) #[1,3,300,7,100]
#通过循环用下列遍历列表元素
for index in range(len(list1)):
	print(list1[index])
#通过for循环遍历列表元素
for elem in list1:
	print(elem)
#通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
	print(index, elem)
'''

'''
#向列表中添加元素以及从列表中移除元素
list1 = [1,3,5,7,100]
#添加元素
list1.append(200)
list1.insert(1,400)
#合并两个列表
#list1.extend([1000,2000])
list1 += [1000,2000]
print(list1) #[1,400,3,5,7,100,200,1000,2000]
print(len(list1)) #9
#先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
		list1.remove(3)
if 1234 in list1:
	list1.remove(1234)
print(list1) #[1,400,5,7,100,200,1000]
#从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) #[400,5,7,100,200,1000]
#清空列表元素
list1.clear()
print(list1) #[]
'''

'''
#列表切片操作
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
'''

'''
#列表的排序操作
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
#sorted函数返回后列表排序后的拷贝不会修改传入的列表
#函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
#通过key关键字参数指定字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)
#给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
'''

'''
#使用列表的生成式语法创建列表
f = [x for x in range(1,10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
#用列表的生成表达式语法创建列表容器
#用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
#请注意下面的代码创建的不是一个列表而是一个生成器对象
#通过生成器可以获取到数据但它不占用额外的空间存储数据
#每次需要数据的时候就通过内部的运算得到数据（需要花费额外的时间）
f = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f)) #相比生成器不占用存储数据的空间
print(f)
for val in f:
	print(val)
'''

'''
def fid(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
		yield a

def main():
	for val in fid(20):
		print(val)

if __name__ == '__main__':
	main()
'''

'''
#使用元组
#定义元组
t = ('刘洋', 19, True, '山西大同')
print(t)
#获取元组中的元素
print(t[0])
print(t[3])
#遍历元组中的值
for member in t:
	print(member)
#重新给元组赋值
#t[0] = '莫要逗我' #TypeError
#变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('莫要逗我', 19, True, '大同御东')
print(t)
#将元组转换成列表
person = list(t)
print(person)
#列表是可以修改它的元素的
person[0] = '杨抚云'
person[1] = 19
print(person)
#将列表转换成元组
fruits_list = ['apple','grapes','strawberry']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
'''

'''
#使用字典
scores = {'刘洋': 95, '莫要逗我': 78, '杨抚云': 82}
#通过建可以获取字典中对应的值
print(scores['刘洋'])
print(scores['杨抚云'])
#对字典进行遍历（遍历的其实是键再通过键取对应的值）
for elem in scores:
	print('%s\t--->\t%d' % (elem, scores[elem]))
#更新字典中的元素
scores['莫要逗我'] = 66
scores['乔布斯'] = 66.6
scores.update(马云=60, 马化腾=61)
print(scores)
if '马斯克' in scores:
	print(scores['马斯克'])
print(scores.get('马斯克'))
#get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('马斯克', 65))
#删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('刘洋', 99))
#清空字典
scores.clear()
print(scores)
'''

'''
#练习1：在屏幕上显示跑马灯文字
import os
import time

def main():
	content = '我爱Python'
	while True:
		#清理屏幕上的输出
		os.system('cls') #os.system('clear')
		print(content)
		#休眠200毫秒
		time.sleep(0.2)
		content = content[1:] + content[0]

if __name__ == '__main__':
	main()
'''

'''
#练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
'''

'''
#练习3：设计一个函数返回给定文件名的后缀名
def get_suffix(fillename, has_dot=False):
	"""
	获取文件名的后缀名
	:param filename:文件名
	:param hat_dot:返回的后缀名是否需要带点
	"""
	pos = filename.rfind('.')
	if 0 < pos < len(filename) - 1:
		index = pos if has_dot else pso + 1
		return filename[index:]
	else:
		return ''
'''


#练习4：设计一个函数返回传入的列表中最大和第二大的元素的值
'''
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
'''

'''
#练习5：计算指定的年月日是这一年的第几天
def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()
'''


#练习6:打印杨辉三角
'''
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    main()
'''


'''
#案例1：双色球选号。
from random import randrange, randint, sample

def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()
#说明： 上面使用random模块的sample函数来实现从列表中选择不重复的n个元素。
'''

'''
#综合案例2：约瑟夫环问题。
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

if __name__ == '__main__':
    main()
'''


#综合案例3：井字棋游戏
'''
import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()
'''