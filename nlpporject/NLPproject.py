from __future__ import print_function
import torch
import thulac
import re, string
import shutil
import random
import numpy as np
from sklearn.model_selection import train_test_split
import numpy


chinToken = thulac.thulac(seg_only=True, T2S=True, filt=True, deli='_')
chinToken.cut_f("UN.en-zh.zh", 'tokenizedOriginal.txt')
def getChinese():
	file = open('tokenizedOriginal.txt', "r", encoding="utf8")
	context = file.read()
	#for line in context:
	line = context.split('\n')
	lines = []
	for i in line:
		lines.append(re.sub("\W", " ", i))
	# print(lines)
	line2 = []
	for i in lines:
		line2.append(" ".join(i.split()))
	
	#context = filtrate.sub(r'', context) # remove all non-Chinese characters
	file.close()
	return line2
a = getChinese()
# print(a)
nopunc = open('nopuncoriginal.txt', 'w', encoding="utf8")
for i in range(len(a)):
	nopunc.write(a[i])
	nopunc.write('\n')
nopunc.close()





#validation set
with open('nopuncoriginal.txt','r') as d:
	temp1 = d.read().split('\n')
with open('validation.txt', 'w') as e:
	num = np.random.choice(len(temp1), 5000)
	for i in range(len(num)):
		e.write(temp1[i])
		e.write('\n')


#delete sentences in validation
copytemp = temp1
with open('validation.txt','r') as f:
	temp2 = f.read().split('\n')
for i in temp2:
	if i in copytemp:
		copytemp.remove(i)

#80 train 20 test split
testx, trainx = train_test_split(copytemp, test_size=0.20, train_size=0.80, shuffle=True) #random_state=101
test = open('traindataOriginal.txt', 'w', encoding="utf8")
for i in range(len(testx)):
	test.write(testx[i])
	test.write('\n')
train = open('testdataOriginal.txt', 'w', encoding="utf8")
for i in range(len(trainx)):
	train.write(trainx[i])
	train.write('\n')





