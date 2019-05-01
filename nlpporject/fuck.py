from __future__ import print_function
import torch
import thulac
import re
import string
import shutil
import random
import numpy as np
import sys
from sklearn.model_selection import train_test_split



f = open('tokenizedChinese', "r")
context = f.read()
a=r'\（.*?\）'
# a = '\([^)]*\)'
# b= '^[^\(]'
# ext = (re.sub(r"\（[^)]*\）", '', context))
ext = (re.sub(r'\（.*?\）', '', context))
ext = (re.sub(r'\(.+?\)', '', ext))
ext = (re.sub(r'/\A\/', '', ext))
ext = ext.replace("A", '')
print(ext)