from matplotlib import pyplot

#산점도 그래프 출력
import random
pyplot.title("data")
a = 0
for i in range(1000):
  x = random.uniform(0.0, 6.0)
  y = random.uniform(0.0, 100.0)
  pyplot.scatter(x, y, s=10) #산점도
  a += 1

pyplot.xlabel("x data") # 그래프 X축 제목
pyplot.ylabel("y data") # 그래프 Y축 제목
pyplot.show() # 그래프 종료