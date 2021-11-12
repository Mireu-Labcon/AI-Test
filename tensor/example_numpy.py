import numpy
print("Numpy Version : {0}".format(numpy.__version__))

dimension1 = 1 # 1차원 데이터
dimension2 = [1,2,3,4,5] # 2차원 데이터
dimension3 = [1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5] # 3차원 데이터

dimension1data = numpy.array(dimension1)
text_data = "{0}차원, 데이터값 : {1}".format(dimension1data.ndim+1, dimension1)
print(text_data)

dimension2data = numpy.array(dimension2)
text_data = "{0}차원, 데이터값 : {1}".format(dimension2data.ndim+1, dimension2)
print(text_data)

dimension3data = numpy.array(dimension3)
text_data = "{0}차원, 데이터값 : {1}".format(dimension3data.ndim+1, dimension3)
print(text_data)