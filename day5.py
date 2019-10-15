'''
经典的例子
寻找水仙花数
说明：水仙花数被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
	该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3 + 3^3 = 153$
'''
'''
for num in range(100,1000):
	low = num % 10
	mid = num // 10 % 10
	high = num // 100
	if num == low ** 3 + mid ** 3 + high ** 3:
		print(num)
'''	

'''
正整数的反转
将12345变成54321
'''
'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
	reversed_num = reversed_num * 10 + num % 10
	num //= 10
print(reversed_num)
'''

'''
百钱百鸡问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，用1000块钱买100只鸡，问公鸡、母鸡、小鸡各有多少只？
'''
'''
for x in range(0,20):
	for y in range(0,33):
		z = 100 - x - y
		if 5 * x + 3 * y + z / 3 == 100:
			print('公鸡：%d只, 母鸡:%d只, 小鸡:%d只' % (x,y,z))
'''

'''
CRAPS赌博游戏
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，
玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。	
'''
'''
设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
'''

'''
from random import randint

money = 1000
while money > 0:
	print('你的总资产为:', money)
	needs_go_on = False
	while True:
		debt = int(input('请下注:'))
		if 0 < debt <= money:
			break
	first = randint(1,6) + randint(1,6)
	print('玩家摇出了%d点' % first)
	if first == 7 or first == 11:
		print('玩家胜！')
		money += debt
	elif first == 2 or first == 3 or first == 12:
		print('庄家胜！')
		money -= debt
	else:
		needs_go_on = True
	while needs_go_on:
		needs_go_on = False
		current = randint(1,6) + randint(1,6)
		print('玩家摇出了%d点' % current)
		if current == 7:
			print('庄家胜！')
			money -= debt
		elif current == first:
			print('玩家胜')
			money += debt
		else:
			needs_go_on = True
print('你破产了，游戏结束！')
'''

'''
###有用的练习

生成斐波那契数列的前20个数。

说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）
在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为"兔子数列"。斐波那契数列的特点是数列的前两个数都是1，
从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。

找出10000以内的完美数。

说明：完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
完美数有很多神奇的特性，有兴趣的可以自行了解。

输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）。
'''