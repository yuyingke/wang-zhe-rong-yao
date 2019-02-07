import subprocess
import random
import time

#模拟点击坐标，加上随机数避免每次点击同一点
def tap(x, y):
    subprocess.call('adb shell input tap {} {}'.format(x + random.randint(0,8), y + random.randint(0,8)),shell = True)
    
#最后一关(鲁班周瑜芈月)
def start(i):
    print('下一步')
    tap(1500, 960)
    time.sleep(7 + random.randint(0,1))

    print('点击闯关')
    tap(1500, 880)
    print('加载界面')
    time.sleep(22 + random.randint(0,1))
    
    print('跳过开始对话')
    tap(1840, 40)
    time.sleep(65 + random.randint(0,1))
    print('跳过墨子对话')
    tap(1840, 40)
    time.sleep(30 + random.randint(0,1))
    print('跳过白起对话')
    tap(1840, 40)
    time.sleep(38 + random.randint(0,1))
    print('跳过最后对话')
    tap(1840, 40)
    print('等待结束')
    time.sleep(5 + random.randint(0,2))

    print('点击任意位置')
    tap(1450, 900)
    time.sleep(5 + random.randint(0,1))

    print('完成' + str(i+1) + '次\n')

if __name__ == "__main__":    
    for i in range(12):
        start(i)
    time.sleep(15)   
    pass
