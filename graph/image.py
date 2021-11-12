from matplotlib import pyplot
from PIL import Image

#이미지 출력
digitimage = Image.open("digit-5.jpg") #이미지 파일 불러오기
pyplot.imshow(digitimage) # 이미지 출력
pyplot.show() # 그래프 종료