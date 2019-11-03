#使用tkinter做一个简单的GUI应用
'''
import tkinter
import tkinter.messagebox


def main():
    flag = True

    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello,world!')\
            if flag else ('blue', 'Goodbye,world!')
        label.config(text=msg, fg=color)    

    #确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
            top.quit()

    #创建顶层窗口
    top = tkinter.Tk()
    #设置窗口大小
    top.geometry('240x160')
    #设置窗口标题
    top.title('小游戏')
    #创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello,world!', font='Airal -32', fg='red')
    label.pack(expand=1)
    #创建一个装按钮的容器
    panel = tkinter.Frame(top)
    #创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    #开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
'''


#大球吃小球
#制作游戏窗口
import pygame


def main():
    #初始化导入的pygame中的模块
    pygame.init()
    #初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    #开启一个事件循环处理发生的事件
    while running:
        #从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()


#在窗口中绘图
import pygame


def main():
    #初始化导入的pygame中的模块
    pygame.init()
    #初始化用于显示窗口并设置窗口尺寸
    screen =  pygame.display.set_mode((800,600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    #设置窗口的背景色（颜色是由红绿蓝三原色构成的元组）
    screen.fill(242, 242, 242)
    #绘制一个圆(参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    #刷新当前窗口(渲染窗口将绘制的图形呈现出来) 
    pygame.display.flip()
    running = True
    #开启一个事件循环处理发生的事件
    while running:
        #从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()


#加载图像
import pygame


def main():
    #初始化导入的pygame中的模块
    pygame.init()
    #初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    #设置窗口的背景色（颜色是由红绿蓝三原色构成的元组）
    screen.fill(255, 255, 255)
    #通过指定的文件名加载图像
    screen.blit(ball_image, (50, 50))
    #刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    running = True
    #开启一个时间循环处理发生的事件
    while running:
        #从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()


#实现动画效果
import pygame


def main():
    #初始化导入的pygame中的模块
    pygame.init()
    #初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    #定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    #开启一个事件循环处理发生的事件
    while running:
        #从消息队列获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x,y), 30, 0)
        pygame.display.flip()
        #每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()


#碰撞检测
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other,alive = False
                self.radius = self.radius + int(other.radius * 0.146)
    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                            (self.x, self.y), self.radius, 0)


#事件处理
def mian():
    #定义用来装所有球的容器
    balls = []
    #初始化导入的pygame中的模块
    pygame.init()
    #初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    #设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    #开启一个事件循环处理发生的事件
    while running:
        #从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #处理鼠标事件的位置
            x, y = ev .pos
            radius = randint(10, 100)
            sx, sy = radius(-10, 10), randint(-10, 10)
            color = Color.random_color()
            #在点击鼠标的位置再创建一个球(大小、速度和颜色随机)
            ball = Ball(x, y, radius, sx, sy, color)
            #将球添加到列表容器中
            balls.append(ball)
        screen.fill((255, 255, 255))
        #取出容器中的球，如果没被吃掉就绘制，被吃掉就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        #每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            #检查球有没有迟到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()