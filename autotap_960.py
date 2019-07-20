import subprocess
import random
import time
#夜神模拟器   adb connect 127.0.0.1:62001
#天天模拟器   adb connect 127.0.0.1:6555
#夜神模拟器
#模拟点击坐标，加上随机数避免每次点击同一点
def tap(x, y):
    subprocess.call('adb shell input tap {} {}'.format(x + random.randint(0,8), y + random.randint(0,8)),shell = True)
    
#最后一关大师难度(鲁班周瑜芈月)，可自行换英雄
def start(i):

    print('冒险之旅')
    tap(745, 395)
    s1 = 1 + random.randint(0,1)
    print('等待' , s1 , '秒')
    time.sleep( s1 )

    print('冒险模式')
    tap(575, 255)
    s2 = 1 + random.randint(0,1)
    print('等待' , s2 , '秒')
    time.sleep( s2 )

    print('选择挑战')
    tap(475, 265)
    s3 = 1 + random.randint(0,1)
    print('等待' , s3 , '秒')
    time.sleep( s3 )
    
    print('下一步')
    tap(745, 460)
    t1 = 2 + random.randint(0,1)
    print('等待' , t1 , '秒')
    time.sleep( t1 )

    print('点击闯关')
    tap(720, 438)
    
    t2 = 15 + random.randint(0,1)
    print('加载界面，' , '等待' , t2 , '秒')
    time.sleep( t2 )
    
    print('跳过开始对话')
    tap(920, 20)
    t3 = 64 + random.randint(0,1)
    print('等待' , t3 , '秒')
    time.sleep( t3 )
    
    print('跳过墨子对话')
    tap(920, 20)
    t4 = 24 + random.randint(0,1)
    print('等待' , t4 , '秒')
    time.sleep( t4 )
    
    print('跳过白起对话')
    tap(920, 20)
    t5 = 35 + random.randint(0,1)
    print('等待' , t5 , '秒')
    time.sleep( t5 )
    
    print('跳过最后对话')
    tap(920, 20)

    t6 = 12 + random.randint(0,1)
    print('等待结束' , '等待' , t6 , '秒')
    time.sleep(t6)

    print('完成' , (i+1) , '次,耗时：' , (s1+s2+s3+t1+t2+t3+t4+t5+t6) , '\n')

if __name__ == "__main__":    
    for i in range(12):
        start(i)
    time.sleep(5)

    for i in range(12):
        start(i)
    time.sleep(5)
    
    for i in range(12):
        start(i)
    time.sleep(5)
      
    pass
