from __future__ import print_function
import torch
import thulac
import re, string
import shutil
import random
import numpy as np
from sklearn.model_selection import train_test_split

# with open("UN.en-zh.zh") as f:
# 	with open("smallChinese", "w") as f1:
# 		i=0
# 		for line in f:
# 			i+=1
# 			if i!=10:
# 				f1.write(line)
# 			else:
# 				break


# f = open("smallChineseNoPunc", "w", encoding="utf8")
# f.write(a)

chinToken = thulac.thulac(seg_only=True, T2S=True, filt=True, deli='_')
chinToken.cut_f("smallChinese", "tokenizedChinese")
def getChinese():
	file = open('tokenizedChinese', "r", encoding="utf8")
	context = file.read()
	#for line in context:
	line = context.split('\n')
	lines = []
	for i in line:
		lines.append(re.sub("\W", " ", i))
	print(lines)
	# filtrate = re.compile(u'[^\u4E00-\u9FA5]') # non-Chinese unicode range
	#
	# line = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*]+()", " ",line)
	# line = re.sub("[【】╮╯▽╰╭★→「」]+"," ",line)
	# line = re.sub("》", " ", line)
	# line = re.sub("《", " ", line)
	# line = re.sub("：", " ", line)
	# line = re.sub("」", " ", line)
	# line = re.sub("「", " ", line)
	# line = re.sub("！", " ", line)
	# line = re.sub("（", " ", line)
	# line = re.sub("）", " ", line)
	# line = re.sub("；", " ", line)
	# line = re.sub("～", " ", line)
	# line = re.sub("。", " ", line)
	# line = re.sub("，", " ", line)
	# line = re.sub("？", " ", line)
	# line = re.sub("】", " ", line)
	# line = re.sub("【", " ", line)
	# line = re.sub("、", " ", line)
	# line = re.sub("”", " ", line)
	# line = re.sub("“", " ", line)
	# line = re.sub("\(", " ", line)
	# line = re.sub("\)", " ", line)
	line2 = []
	for i in lines:
		line2.append(" ".join(i.split()))
	
	#context = filtrate.sub(r'', context) # remove all non-Chinese characters
	file.close()
	return line2
a = getChinese()
print(a)
nopunc = open('nopunc', 'w', encoding="utf8")
for i in range(len(a)):
	nopunc.write(a[i])
	nopunc.write('\n')
nopunc.close()

#80 20 split
'''
with open("nopunc", "rb") as f:
   data = f.read().split('\n')
   data = np.array(data)  #convert array to numpy type array

   x_train ,x_test = train_test_split(data,test_size=0.5)
   print(x_train ,x_test)
'''
'''
#Kyle did not solve this
file=open("nopunc","r")
data=list()
for line in file:
	data.append(line.split('\n'))
	print(line)
nopunc.close()
random.shuffle(data)
train_data = data[:int((len(data)+1)*.80)] #Remaining 80% to training set
test_data = data[int(len(data)*.80+1):]
train = open('traindata', 'w', encoding="utf8")
for i in train_data:
	train.write(i)
test = open('testdata', 'w', encoding="utf8")
for i in test_data:
	test.write(i)

'''

with open("nopunc", "r") as f:
	data = f.read().split('\n')

random.shuffle(data)
#print(data)
train_data = data[:80]
test_data = data[20:]
print(train_data)
print(test_data)

train = open('traindata', 'w', encoding="utf8")
# train.write((train_data))
for i in range(len(train_data)):
	train.write(train_data[i])
test = open('testdata', 'w', encoding="utf8")
# test.write((test_data))
for i in range(len(test_data)):
	test.write(test_data[i])


