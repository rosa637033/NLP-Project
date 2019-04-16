from __future__ import print_function
import torch
import thulac
import re, string
import shutil
import random
import numpy as np
from sklearn.model_selection import train_test_split


chinToken = thulac.thulac(seg_only=True, T2S=True, filt=True, deli='_')
chinToken.cut_f("UN.en-zh.zh", 'tokenizedOriginal')
def getChinese():
	file = open('tokenizedOriginal', "r", encoding="utf8")
	context = file.read()
	#for line in context:
	line = context.split('\n')
	lines = []
	for i in line:
		lines.append(re.sub("\W", " ", i))
	print(lines)
	line2 = []
	for i in lines:
		line2.append(" ".join(i.split()))
	
	#context = filtrate.sub(r'', context) # remove all non-Chinese characters
	file.close()
	return line2
a = getChinese()
print(a)
nopunc = open('nopuncoriginal', 'w', encoding="utf8")
for i in range(len(a)):
	nopunc.write(a[i])
	nopunc.write('\n')
nopunc.close()

#80 20 split
with open("nopuncoriginal", "r") as f:
	data = f.read().split('\n')

random.shuffle(data)
#print(data)
train_data = data[:80]
test_data = data[20:]
# print(train_data)
# print(test_data)

train = open('traindataOriginal', 'w', encoding="utf8")
# train.write((train_data))
for i in range(len(train_data)):
	train.write(train_data[i])
test = open('testdataOriginal', 'w', encoding="utf8")
# test.write((test_data))
for i in range(len(test_data)):
	test.write(test_data[i])

