#!/usr/bin/python
from sklearn import svm
from ReadData import *
import datetime
startTime = datetime.datetime.now();
trainImage = getTrainImage()
trainLabel = getTrainLabel()
testImage = getTestImage()
testLabel = getTestLabel()
clf = svm.SVC(kernel='rbf')
clf.fit(trainImage,trainLabel)
match = 0
for i in range(len(testImage)):
	predictResult = int(clf.predict(testImage[i])[0])
	if(predictResult==testLabel[i]):
		match += 1
	print i,' ',predictResult ,' ',testLabel[i]

endTime = datetime.datetime.now()
print 'match:',match
print 'use time: '+str(endTime-startTime)
print 'error rate: '+ str(1-(match*1.0/len(testImage)))