from matplotlib import pyplot

# 실선 그래프 출력
pyplot.figure(figsize=(10,10)) # 그래프 크기
pyplot.subplot(2, 1, 1) # 그래프 비율
pyplot.title("test") # 그래프 제목
pyplot.plot([1,2,3,4,5],[1,2,3,4,5]) # 그래프 데이터
pyplot.plot([1,2,3,4,5],[1,2,3,4,5],'ro') #점 그래프
pyplot.axis([0, 6, 0, 12]) # [세로 시작점, 세로 끝점, 가로 시작점, 가로 끝점]
pyplot.show() # 그래프 종료