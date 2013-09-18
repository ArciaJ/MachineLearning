#!/usr/bin/python
from sklearn.naive_bayes import MultinomialNB
from ReadData import *
import datetime
startTime = datetime.datetime.now();
trainImage = getTrainImage()
trainLabel = getTrainLabel()
testImage = getTestImage()
testLabel = getTestLabel()
mnb = MultinomialNB()
mnb.fit(trainImage,trainLabel)
match = 0
for i in range(len(testImage)):
	predictResult = int(mnb.predict(testImage[i])[0])
	if(predictResult==testLabel[i]):
		match += 1
	print i,' ',predictResult ,' ',testLabel[i]

endTime = datetime.datetime.now()
print 'match:',match
print 'use time: '+str(endTime-startTime)
print 'error rate: '+ str(1-(match*1.0/len(testImage)))