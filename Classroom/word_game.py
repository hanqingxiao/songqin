'''游戏分解:找出游戏涉及的对象：类的概念
    1- 老虎
        1- 属性：俗称：特征  本质是:变量
            1- 静态属性
                1- 叫声
            2- 实例属性：每一个实例都可以不一样
                1- 体重
        2- 方法：俗称：行为  本质是:函数
        3- 构造方法
    2- 羊
    3- 房间
2- 关系组网
'''

class Tiger:
    nickName = 'Tiger'
    #2- 实例属性
    def __init__(self,inWeight=200):#初始化方法  构造方法
        self.weight = inWeight#
    #3- 实例方法
    def roar(self):
        print('wow!!!-----体重减5斤')
        self.weight -= 5
    #吃--喂食
    def feed(self,food):
        if food == 'meat':
            print('恭喜，喂食正确，体重增加10斤！')
            self.weight += 10
        else:
            print('抱歉，喂食错误，体重减少10斤！')
            self.weight -= 10
class Sheep:
    nickName = 'Sheep'
    def __init__(self, inWeight=100):  # 初始化方法  构造方法
        self.weight = inWeight  #
    def roar(self):
        print('mie~~-----体重减5斤')
        self.weight -= 5
    def feed(self, food):
        if food == 'grass':
            print('恭喜，喂食正确，体重增加10斤！')
            self.weight += 10
        else:
            print('抱歉，喂食错误，体重减少10斤！')
            self.weight -= 10

class Room:#实例属性：编号 动物
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal
import requests
import xlrd

from random import randint
#-------------游戏初始化-------------
roomList = []#里面元素是房间的实例
for one in range(1,11):
    if randint(0,1) == 1:
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    room = Room(one,ani)
    roomList.append(room)
# #time
import time
startTime = time.time()
flag=True
while True:
    curTime = time.time()
    if (curTime - startTime) > 180:
        print('\n\n **********  game over ********** \n\n')
        for idx, room in enumerate(roomList):
            print('room :%s' % (idx + 1), room.animal.nickName, room.animal.weight)
        break
    roomno = randint(1, 10)
    room = roomList[roomno-1]  # why -1 ?
    ch = input('we come room # %s, dork?[y/n]' % roomno)
    if ch == 'y':
        room.animal.roar()

    food = input('please feed:')
    room.animal.feed(food.strip())

    # while True:
    #     curTime = time.time()
    #     if flag:
    #         for idx, room in enumerate(roomList):
    #             if room.animal.weight <= 0:
    #                 for idx, room in enumerate(roomList):
    #                     print('room :%s' % (idx + 1), room.animal.nickName, room.animal.weight)
    #                 flag = False
    #                 break
    #
    #         if (curTime - startTime) > 20:
    #             print('\n\n **********  game over ********** \n\n')
    #             for idx, room in enumerate(roomList):
    #                 print('room :%s' % (idx + 1), room.animal.nickName, room.animal.weight)
    #             flag = False
    #             break
    #         roomno = randint(1, 10)
    #         room = roomList[roomno - 1]  # why -1 ?
    #         ch = input('we come room # %s, dork?[y/n]' % roomno)
    #         if ch == 'y':
    #             room.animal.roar()
    #
    #         food = input('please feed:')
    #         room.animal.feed(food.strip())
    #     else:
    #         break