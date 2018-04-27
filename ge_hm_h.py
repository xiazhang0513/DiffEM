#!/usr/bin/python
# -*- coding: UTF-8 -*-
#对txt里的MIX数据进行处理 formal test 1
# written by MajestyLee 2017/4/12
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')
from numpy import *
data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(23):
	filename1 = "/Users/majestylee/Downloads/Gene_chr/Gene_x_chr" + str(i+2) + ".txt"
	filename2 = "/Users/majestylee/Downloads/Gene_chr/Gene_or_chr" + str(i+2) + ".txt"
	filename3 = "/Users/majestylee/Downloads/Gene_chr/Gene_mix_chr" + str(i+2) + ".txt"
	file3 = open(filename1)
	file4 = open(filename2)
	file5 = open(filename3)
	count = 0
	th1 = 0
	th2 = 0
	th3 = 0
	while True:
		line1 = file3.readline()
		if not line1:
			break
		L = line1.split()
		line2 = file4.readline()
		if not line2:
			break
		L2 = line2.split()
		line3 = file5.readline()
		if not line3:
			break
		L3 = line3.split()
		ii = 0
		iii = 0
		iiii = 0
		for ii in range(5):
			th1 = th1 + int(L[ii+1])
			count = count + 1
		for iii in range(15):
			th2 = th2 + int(L2[iii+1])
		for iiii in range(10):
			th3 = th3 + int(L3[iiii+1])
		# 	print th3
		# if th3 < 0:
		# 	print L[0]
		# 	break
	file3.close()
	file4.close()
	file5.close()
	th1 = th1 / count
	th2 = th2 / count
	th2 = th2 / 3
	th3 = th3 / count
	th3 = th3 / 2
	print th1,th2,th3
	file3 = open(filename1)
	file4 = open(filename2)
	file5 = open(filename3)
	filename6 = "/Users/majestylee/Downloads/Gene_chr_hm/Gene_x_chr" + str(i+2) + "_hm.txt"
	filename7 = "/Users/majestylee/Downloads/Gene_chr_hm/Gene_or_chr" + str(i+2) + "_hm.txt"
	filename8 = "/Users/majestylee/Downloads/Gene_chr_hm/Gene_mix_chr" + str(i+2) + "_hm.txt"
	file6 = open(filename6,'w')
	file7 = open(filename7,'w')
	file8 = open(filename8,'w')
	while True:
		line1 = file3.readline()
		if not line1:
			break
		L = line1.split()
		line2 = file4.readline()
		if not line2:
			break
		L2 = line2.split()
		line3 = file5.readline()
		if not line3:
			break
		L3 = line3.split()
		ii = 0
		LL = L
		for ii in range(5):
			if int(L[ii+1]) > th1:
				LL[ii+1] = '1'
			else:
				LL[ii+1] = '0'
		ii = 0
		hm = 0
		for ii in range(5):
			if LL[ii+1] == '1':
				hm = hm + 1
		ii = 0
		for ii in range(5):
			if LL[ii+1] == '1':
				data[ii] = 5 - hm
			else:
				data[ii] = hm
		# str_final = LL[0]
		ii = 0
		x_sum = 0
		for ii in range(5):
			x_sum = x_sum + data[ii]
		str_final = LL[0] + " " + str(x_sum) + '\n'
	# print str_final
			# file2.write(str_final)
			# str_final = " ".join(LL) + "\n"
			# print str_final
		file6.write(str_final)
		LL = L2
		ii = 0
		for ii in range(15):
			if int(L2[ii+1]) > th2:
				LL[ii+1] = '1'
			else:
				LL[ii+1] = '0'
		ii = 0
		hm = 0
		for ii in range(15):
			if LL[ii+1] == '1':
				hm = hm + 1
		ii = 0
		for ii in range(15):
			if LL[ii+1] == '1':
				data[ii] = 15 - hm
			else:
				data[ii] = hm
			# str_final = LL[0]
		ii = 0
		x_sum = 0
		for ii in range(15):
			x_sum = x_sum + data[ii]
		str_final = LL[0] + " " + str(x_sum) + '\n'
			# str_final = " ".join(LL) + "\n"
			# print str_final
		file7.write(str_final)
		LL = L3
		ii = 0
		for ii in range(10):
			if int(L3[ii+1]) > th3:
				LL[ii+1] = '1'
			else:
				LL[ii+1] = '0'
		ii = 0
		hm = 0
		for ii in range(10):
			if LL[ii+1] == '1':
				hm = hm + 1
		ii = 0
		for ii in range(10):
			if LL[ii+1] == '1':
				data[ii] = 10 - hm
			else:
				data[ii] = hm
			# str_final = LL[0]
		ii = 0
		x_sum = 0
		for ii in range(10):
			x_sum = x_sum + data[ii]
		str_final = LL[0] + " " + str(x_sum) + '\n'
			# str_final = " ".join(LL) + "\n"
			# print str_final
		file8.write(str_final)
	file3.close()
	file4.close()
	file5.close()
	file6.close()
	file7.close()
	file8.close()


