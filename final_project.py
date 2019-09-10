import time
import random
import math

" Traveling Salesman Problem "
start_time = time.time()
#店家名稱
name = []
name.append('吳記火雞肉飯')
name.append('阿信美食')
name.append('郭家雞肉飯')
name.append('桃城南門火雞肉飯')
name.append('阿樓師火雞肉飯')
name.append('阿霞火雞肉飯')
name.append('大嘉義得火雞肉飯')
name.append('阿里山火雞肉飯')
name.append('嘉義車頭火雞肉飯')
name.append('大同火雞肉飯')
name.append('阿志火雞肉飯')
name.append('東門雞肉飯')
name.append('民主火雞肉飯')
name.append('呆獅雞肉飯')
name.append('嘉義噴水雞肉飯')
name.append('阿宏師火雞肉飯')
name.append('嘉義人火雞肉飯')
name.append('桃城三禾火雞肉飯')
name.append('溫好記火雞肉飯')
name.append('噴水雞肉飯')
name.append('頭家火雞肉飯')
name.append('民國火雞肉飯')
name.append('鼎莊火雞肉飯')
name.append('和平嘉義火雞肉飯')
#兩兩之間距離
dist = []
dist.append([6.7,3.6,1,0,1,0.5,0.4,0.13,0.9,0.95,1.1,3.2,0.3,1.1,0.55,1.1,1.5,5.8,0.13,0.07,0.75,1.3,2.2,1.1])
dist.append([6.7,3.7,1.1,0.12,1,0.4,0,0.07,1,0.9,1,3.1,0.28,1,0.55,1.3,1.6,5.9,0.24,0.04,0.7,1.3,2.4,1.1])
dist.append([6.8,3.6,1.1,0.13,1.1,0.35,0.55,0,1,1,0.9,2.9,0.45,1.2,0.6,1.2,1.6,6,0.26,0.06,0.7,1.4,2.4,1.3])
dist.append([5.6,4.1,2,1.1,0.06,0.95,1.4,1,0.4,0.13,1.5,3.9,0.75,0,0.6,0.55,1.2,6.3,1.1,1.2,0.55,0.3,2.1,0.23])
dist.append([6.2,3.7,1.5,0.65,0.6,0.65,0.9,0.5,0.55,0.45,1.1,3.1,0.25,0.6,0,0.65,1.6,5.9,0.65,0.7,0.55,0.8,2.3,0.8])
dist.append([6.7,3.6,1.1,0.72,1.2,0.4,0.5,0.61,1,1.1,1,0.2,0.35,1.2,0.65,1.3,1.5,5.9,0.2,0,0.8,1.6,2.3,1.4])
dist.append([0,9.4,7.8,6.7,5.7,6.5,17,16,6.7,5.8,7.2,11,6.5,17,6.2,9.1,7.3,15,6.9,6.9,7.6,5.4,12,5.6])
dist.append([9.4,0,2.1,3.3,3.6,2.8,3.1,3.5,3.8,3.5,2.1,2.1,3.6,3.6,3.2,3.8,4.6,6.9,3.3,3.4,4.1,4.4,4.5,3.9])
dist.append([7.7,2.8,0,0.9,2,1.2,0.8,0.85,1.8,1.9,0.5,2.1,1.2,2.5,1.4,2.1,2.7,6.3,0.8,0.95,1.6,2.7,2.7,2.2])
dist.append([5.7,4.2,2.4,1.1,0,0.95,1.4,0.95,0.35,0.1,1.5,3.5,0.7,0.06,0.6,0.6,1.1,6.2,1.1,1.2,0.5,0.25,2,0.3])
dist.append([6.5,3.2,1.6,0.5,0.95,0,0.85,0.35,1.1,0.85,0.7,3,0.65,0.95,0.5,0.85,2.1,6.5,0.6,0.4,1.1,1.2,2.9,1])
dist.append([6.1,4.3,1.9,0.9,0.4,1.1,1.3,0.75,0,0.28,1.7,4.1,0.5,0.4,0.55,0.75,1,0.9,0.9,0.85,0.17,0.65,1.9,0.45])
dist.append([0.8,4,1.8,1,0.1,0.85,1.3,0.85,0.28,0,1.4,3.4,0.6,0.13,0.45,0.5,1.2,6.1,1,1.1,0.4,0.35,2.1,0.21])
dist.append([7.2,2.7,0.9,1.1,1.5,0.7,1,0.9,1.7,1.4,0,2,1.2,1.5,1.1,1.6,2.6,6.8,1,1,1.6,1.8,3.2,1.7])
dist.append([9.1,1,1.8,3,3.3,2.5,2.8,3.2,3.5,3.2,1.8,0,3.3,3.4,2.9,3.5,4,7.1,3,3.1,3.5,3.6,4.6,3.6])
dist.append([6.4,3.9,1.2,0.4,0.75,0.6,0.65,0.3,0.6,0.65,1.2,3.2,0,0.75,0.25,0.75,1.6,6,0.4,0.45,0.6,1,2.4,0.85])
dist.append([5.6,3.9,2.2,1.3,0.45,1,1.6,1.2,0.6,0.35,1.8,3.8,0.95,0.4,0.8,0,1.5,6.5,1.3,1.4,0.75,0.65,2.4,0.15])
dist.append([6.2,4.7,2.7,1.5,1.1,2.1,1.8,1.6,1,1.2,2.7,4.8,1.5,1.2,1.6,1.7,0,5.8,1.5,1.6,1,0.95,1,1.7])
dist.append([15,7,6.3,5.9,6.2,6.4,6.1,6,5.9,6.1,7.2,7.1,5.9,6.3,5.9,6.6,5.6,0,5.9,5.9,5.8,6.7,5.7,6.4])
dist.append([6.7,3.5,0.85,0.69,1.1,0.55,0.29,0.2,1,1,1,1.8,0.35,1.1,0.75,1.1,1.5,5.9,0,0.14,0.8,1.8,2.3,1.2])
dist.append([6.3,4.3,1.7,0.8,0.55,1.1,1.1,0.75,0.17,0.4,1.6,0.8,0.5,0.55,0.55,0.7,1,5.7,0.8,0.9,0,0.8,1.9,0.6])
dist.append([5.4,4.4,2.2,1.3,0.25,1.2,1.6,1.2,0.65,0.35,1.8,1.3,1,0.3,0.8,0.85,0.95,6.6,1.3,1.4,0.8,0,1.8,0.55])
dist.append([12.2,5,2.8,2.3,2,2.9,2.6,2.4,1.8,2.1,3.1,2.3,2.3,2,2.4,2.6,1,5.7,2.3,2.4,1.8,1.8,0,2.3])
dist.append([5.6,3.9,2.3,1.2,0.3,1,1.5,1.1,0.45,0.21,1.7,1.2,0.8,0.23,0.7,0.4,1.5,6.3,1.2,1.5,0.6,0.5,2.4,0])
"""
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
"""
"""
model = pulp.LpProblem("value min", pulp.LpMinimize)

# pulp.LpVariable()加入變數
x = {}
for i in range(6):
    for j in range(6):
        x[i, j] = pulp.LpVariable('x_%d_%d' % (i, j), lowBound = 0, cat='Binary')

# model += 設置目標函數
model += sum(x[a, b]*dist[a][b] for a in range(24) for b in range(24))

# model += 加入限制式
for i in range(24):
    model += sum(x[i, j] for j in range(24)) == 1
for j in range(24):
    model += sum(x[i, j] for i in range(24)) == 1

for k in range(24):
    model += x[k, k] == 0


# model.solve()求解
model.solve()

# 透過屬性value(model.objective)顯示最佳解

for v in model.variables():
    if v.varValue == 1:
        print(v.name, "=", v.varValue)

print('obj=', pulp.value(model.objective))
"""
#無法增加我們需要的限制
#因此更換變數設定
#營業時間
sell = []
#宵夜店家(23-5)
sell.append([1,1,1,1,1,1])
sell.append([1,1,1,1,1,1])
sell.append([1,1,1,1,1,1])
sell.append([0,0,0,0,1,1])
sell.append([1,0,0,0,0,0])
sell.append([1,1,1,1,0,0])
#白天店家(5-23)
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0])
sell.append([0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
sell.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0])
sell.append([0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0])
sell.append([0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0])
sell.append([0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0])
sell.append([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0])
sell.append([0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
sell.append([0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0])
sell.append([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
sell.append([0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0])
#更換計算方法
#使用模擬退火法
#宵夜店家TSP
#paramater initial
rate = 0.95
t = 100
times = 50000
x = [1,2,3,4,5,6]
xx = [0,1,2,3,4,5]
count = 0
value = 0

for i in range(5):
    value += dist[x[i]-1][x[i+1]-1]
#print("{0},distance=".format(x),value)
valuebest = value
xbest = x

while(count<times):
    #隨機兩點交換
    y = random.sample(xx, 2)
    x[y[0]],x[y[1]] = x[y[1]],x[y[0]]
    
    #確認營業時間符合
    temp = 0
    for i in range(6):
        temp += sell[x[i]-1][i]
    #print(temp)

    if temp == 6:
        #計算出新值
        valuenew = 0
        for i in range(5):
            valuenew += dist[x[i]-1][x[i+1]-1]
    
        #若新值較大
        if valuenew >= value:
            if random.random() <= math.exp(-(valuenew-value)/t):
                value = valuenew
            else:
                continue
        #若新值較小
        else:
            value = valuenew
            if value < valuebest:
                valuebest = value
                xbest = x;
        #print("{0},distance=".format(x),value)
    count += 1
    t = t*rate
x_optimal = []
x_optimal.append(xbest)
optimal = 0
optimal += valuebest
x_name = []
for i in range(6):
    x_name.append(name[xbest[i]-1])
#白天店家TSP
rate = 0.95
t = 100
times = 100000
x = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
xx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
count = 0
value = 0

for i in range(17):
    value += dist[x[i]-1][x[i+1]-1]
#print("{0},distance=".format(x),value)
valuebest = value
xbest = x

while(count<times):
    #隨機兩點交換
    y = random.sample(xx, 2)
    x[y[0]],x[y[1]] = x[y[1]],x[y[0]]
    
    #確認營業時間符合
    temp = 0
    for i in range(18):
        temp += sell[x[i]-1][i]
    #print(temp)

    if temp == 6:
        #計算出新值
        valuenew = 0
        for i in range(17):
            valuenew += dist[x[i]-1][x[i+1]-1]
    
        #若新值較大
        if valuenew >= value:
            if random.random() <= math.exp(-(valuenew-value)/t):
                value = valuenew
            else:
                continue
        #若新值較小
        else:
            value = valuenew
            if value < valuebest:
                valuebest = value
                xbest = x;
        #print("{0},distance=".format(x),value)
    count += 1
    t = t*rate

x_optimal.append(xbest)
optimal += valuebest
for i in range(18):
    x_name.append(name[xbest[i]-1])

print("approximate optimal solution: {0}".format(x_name))
print("fitness function value: ", optimal)

print("running time: %s" % (time.time() - start_time))
