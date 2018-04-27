#!/usr/bin/python
# -*- coding: UTF-8 -*-
#对txt里的数据分类处理
# written by MajestyLee 2017/4/8
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')
from numpy import *
filename = "/Users/majestylee/Downloads/Gene_chr2"
for i in range(23):
	filename = "/Users/majestylee/Downloads/Gene_chr" + str(i+2) + "/Gene_chr" + str(i+2) + ".txt"
	filename1 = "/Users/majestylee/Downloads/Gene_chr/Gene_x_chr" + str(i+2) + ".txt"
	filename2 = "/Users/majestylee/Downloads/Gene_chr/Gene_or_chr" + str(i+2) + ".txt"
	filename3 = "/Users/majestylee/Downloads/Gene_chr/Gene_mix_chr" + str(i+2) + ".txt"
	file1 = open(filename)
	file2 = open(filename1,'w')
	file3 = open(filename2,'w')
	file4 = open(filename3,'w')
	line = file1.readline()
	while True:
		line = file1.readline()
		if not line:
			break
		# sprint line
		L = line.split()
		str_final1 = L[0] + " " + L[10] + " " + L[8] + " " + L[9] + " " + L[11] + " " + L[12] + '\n'
		str_final2 = L[0] + " " + L[2] + " " + L[4] + " " + L[6] + " " + L[7] + " " + L[13] + " " + L[14] + " " + L[15] + " " + L[16] + " " + L[17] + " " + L[23] + " " + L[18] + " " + L[19] + " " + L[21] + " " + L[22] + " " + L[20] + '\n'
		str_final3 = L[0] + " " + L[10] + " " + L[8] + " " + L[9] + " " + L[11] + " " + L[12] + " " + L[2] + " " + L[4] + " " + L[6] + " " + L[7] + " " + L[13] + '\n'
		file2.write(str_final1)
		file3.write(str_final2)
		file4.write(str_final3)
	print "ok"
	file3.close()
	file4.close()
	file1.close()
	file2.close()

