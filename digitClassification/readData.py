import numpy as np 
import struct
import matplotlib.pyplot as plt 

trainImageFileName = 'train-images.idx3-ubyte'
trainLabelFileName = 'train-labels.idx1-ubyte'
testImageFileName = 't10k-images.idx3-ubyte'
testLabelFileName = 't10k-labels.idx1-ubyte'
bigEndian = '>'
fourBytes = 'IIII'
twoBytes = 'II'
pictureBytes = '784B'
labelByte = '1B'
def getImage(filename):
	binFile = open(filename,'rb')
	buf = binFile.read()
	binFile.close()
	index = 0
	magic, numImages, numRows, numColums = struct.unpack_from(bigEndian+fourBytes,buf,index)
	print magic,' ',numImages,' ',numRows,' ',numColums
	index += struct.calcsize(bigEndian+fourBytes)
	images = [];
	for x in range(1000):
		im = struct.unpack_from(bigEndian+pictureBytes,buf,index)
		index += struct.calcsize(bigEndian+pictureBytes)
		im = list(im)
		for index in range(len(im)):
			if im[index]>1:
				im[index] = 1
		images.append(im)
	return np.array(images)

def getLabel(filename):
	binFile = open(filename,'rb')
	buf = binFile.read()
	binFile.close()
	index = 0
	magic, numItems= struct.unpack_from(bigEndian+twoBytes,buf,index)
	print magic,' ',numItems
	index += struct.calcsize(bigEndian+twoBytes)
	labels = [];
	for x in range(1000):
		im = struct.unpack_from(bigEndian+labelByte,buf,index)
		index += struct.calcsize(bigEndian+labelByte)
		labels.append(im[0])
	return np.array(labels)

def getTrainImage():
	return getImage(trainImageFileName)

def getTestImage():
	return getImage(testImageFileName)

def getTrainLabel():
	return getLabel(trainLabelFileName)

def getTestLabel():
	return getLabel(testLabelFileName)
