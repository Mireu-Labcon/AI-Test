from matplotlib import pyplot

# 기본 그래프 출력
pyplot.bar([1,2,3,4],[1,2,3,4]) # 세로, 가로 대입 데이터
pyplot.axis([0,6,0,12]) # [세로 시작점, 세로 끝점, 가로 시작점, 가로 끝점]
pyplot.show() # 그래프 종료

#막대 그래프 출력
pyplot.subplot(2, 1, 2) # 그래프 비율
pyplot.title("test") # 그래프 제목
pyplot.bar([1,2,3,4,5],[1,7,5,10,11]) # 그래프 데이터
pyplot.axis([0,6,0,12]) # [세로 시작점, 세로 끝점, 가로 시작점, 가로 끝점]
pyplot.show() # 그래프 종료