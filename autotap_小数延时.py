import subprocess
import random
import time

#模拟点击坐标，加上随机数避免每次点击同一点
def tap(x, y):
    subprocess.call('adb shell input tap {} {}'.format(x + random.randint(0,5), y + random.randint(0,5)),shell = True)
    
#最后一关大师难度(鲁班周瑜芈月)，可自行换英雄
def start(i):
 
    print('下一步')
    #tap(1670, 920)
    tap(1850, 990)
    t1 = 0.5 + round(random.uniform(0,0.5),1)
    print('等待' , t1 , '秒')
    time.sleep( t1 )

    print('点击闯关')
    tap(1600, 870)
    
    t2 = 11.6 + round(random.uniform(0,0.5),1)
    print('加载界面，' , '等待' , t2 , '秒')
    time.sleep( t2 )
    
    print('跳过开始对话')
    tap(2070, 50)
    t3 = 63 + round(random.uniform(0,0.3),1)
    print('等待' , t3 , '秒')
    time.sleep( t3 )
    
    print('跳过墨子对话')
    tap(2070, 50)
    t4 = 21 + round(random.uniform(0,0.2),1)
    print('等待' , t4 , '秒')
    time.sleep( t4 )
    
    print('跳过白起对话')
    tap(2070, 50)
    t5 = 36.3 + round(random.uniform(0,0.5),1)
    print('等待' , t5 , '秒')
    time.sleep( t5 )
    
    print('跳过最后对话')
    tap(2070, 50)

    t6 = 9 + round(random.uniform(0,0.5),1)
    print('等待结束' , '等待' , t6 , '秒')
    time.sleep(t6)

    print('点击任意位置')
    tap(1850, 990)
    #time.sleep(0.5)
    #tap(1820, 890)
    t7 = 4 + round(random.uniform(0,0.5),1)
    print('等待' , t7 , '秒')
    time.sleep(t7)

    print('完成' , (i+1) , '次,耗时：' , (t1+t2+t3+t4+t5+t6+t7) , '\n')

if __name__ == "__main__":    
    for i in range(12):
        start(i)
    time.sleep(5)
    
    for i in range(14):
        start(i)
    time.sleep(5)
  
    for i in range(14):
        start(i)
    time.sleep(5)
    pass
