# coding=utf-8

import sys
import pprint
trdc_pcr_loaded = False
try:
  import trdc_pcr
  trdc_pcr_loaded = True
except:
  pass

import matplotlib.figure
import numpy as np

if trdc_pcr_loaded:
  data = trdc_pcr.get_all_data()

def avg(x):
  return np.average(x)
  
np_data = np.array(data, dtype=float)
FAM_data_cell = np_data[:,0,:].T # теперь первый индекс - это номер ячейки на изотерме, второй индекс - номер измерения
sh = FAM_data_cell.shape[1]
place= [0,0,0,0]
#цикл на определение шага производной
if sh>10:
	for j in range(6):
		print 'лунка:	цикл:	шаг:	производная:'
		for dist in range(1,5):
			max=0
			for i in range(sh - dist-1):
				#print FAM_data_cell
				if max < abs(FAM_data_cell[j][i+dist]-FAM_data_cell[j][i]):
					max = abs(FAM_data_cell[j][i+dist]-FAM_data_cell[j][i])
					place[dist-1] = i+dist/2
			print '%d	%d	%d	%d' % (j+1,place[dist-1],dist,max/dist)
		print 'average:%d\n' %(avg(place))