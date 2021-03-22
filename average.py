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

np_data = np.array(data, dtype=float)
FAM_data_cell = np_data[:,0,:].T # теперь первый индекс - это номер ячейки на изотерме, второй индекс - номер измерения
CY5_data_cell = np_data[:,1,:].T
sh = CY5_data_cell.shape[1]


def avg(x):
  return np.average(x)
def rms(x):
  xa = avg(x)
  return np.sqrt(np.mean(np.square(x-xa)))
if sh!=0:
	if sh<11:
		for i in range(6):	
			print '%d FAM: %d	%d	%.2f	CY5: %d	%d	%.2f' % (i+1,avg(FAM_data_cell[i]),rms(FAM_data_cell[i]), rms(FAM_data_cell[i])/avg(FAM_data_cell[i])*100,   avg(CY5_data_cell[i][:sh]),rms(CY5_data_cell[i][:sh]),rms(CY5_data_cell[i][:sh])/avg(CY5_data_cell[i][:sh])*100)
	else:
		for i in range(6):	
			print '%d FAM: %d	%d	%.2f	CY5: %d	%d	%.2f' % (i+1,avg(FAM_data_cell[i][(sh-10):sh]),rms(FAM_data_cell[i][(sh-10):sh]), rms(FAM_data_cell[i][(sh-10):sh])/avg(FAM_data_cell[i][(sh-10):sh])*100,    avg(CY5_data_cell[i][(sh-10):sh-1]),rms(CY5_data_cell[i][sh-10:sh-1]),rms(CY5_data_cell[i][(sh-10):sh-1])/avg(CY5_data_cell[i][(sh-10):sh-1])*100)

