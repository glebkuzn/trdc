# coding=utf-8

import sys
import pprint
import os
import csv
import datetime
import configparser
trdc_pcr_loaded = False
try:
  import trdc_pcr
  trdc_pcr_loaded = True
except:
  pass

import matplotlib.figure
import numpy as np

CHIP_NAME = 's03-3'

DIR = '/home/trdc/Рабочий стол/' + CHIP_NAME

if not os.path.exists(DIR):
  os.makedirs(DIR)
else:
  raise Exception('DIR %s EXISTS' % DIR)

ini = configparser.ConfigParser()
ini['main'] = {}
ini['main']['chip_name'] = CHIP_NAME

#считывание данных
data = trdc_pcr.get_all_data()

date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ini['main']['date'] = date_str
ini['main']['mix'] = 'litech'
ini['main']['plotocol'] = '97C*10s+59C*30s'

ini['p1'] = {}
ini['p1']['thickness'] = ''
ini['p1']['Cp'] = ''
ini['p1']['Amp'] = ''
ini['p1']['k_last'] = ''

ini['p2'] = {}
ini['p2']['thickness'] = ''
ini['p2']['Cp'] = ''
ini['p2']['Amp'] = ''
ini['p2']['k_last'] = ''


ini['p3'] = {}
ini['p3']['thickness'] = ''
ini['p3']['Cp'] = ''
ini['p3']['Amp'] = ''
ini['p3']['k_last'] = ''

ini['p4'] = {}
ini['p4']['thickness'] = ''
ini['p4']['Cp'] = ''
ini['p4']['Amp'] = ''
ini['p4']['k_last'] = ''

ini['p5'] = {}
ini['p5']['thickness'] = ''
ini['p5']['Cp'] = ''
ini['p5']['Amp'] = ''
ini['p5']['k_last'] = ''

ini['p6'] = {}
ini['p6']['thickness'] = ''
ini['p6']['Cp'] = ''
ini['p6']['Amp'] = ''
ini['p6']['k_last'] = ''


with open(os.path.join(DIR,'data %s.csv'%date_str), 'w') as csvfile:
  csvfile.write('cell1-chan1;cell1-chan2;cell1-chan3;cell1-chan4;cell1-chan5;cell1-chan6;cell2-chan1;cell2-chan2;cell2-chan3;cell2-chan4;cell2-chan5;cell2-chan6;cell3-chan1;cell3-chan2;cell3-chan3;cell3-chan4;cell3-chan5;cell3-chan6;cell4-chan1;cell4-chan2;cell4-chan3;cell4-chan4;cell4-chan5;cell4-chan6;cell5-chan1;cell5-chan2;cell5-chan3;cell5-chan4;cell5-chan5;cell5-chan6;cell6-chan1;cell6-chan2;cell6-chan3;cell6-chan4;cell6-chan5;cell6-chan6\n')
  for r in data:
    for c in r:
      for ch in c:
        csvfile.write(str(ch))
        csvfile.write(';')
    csvfile.write('\n')



#разбиение данных
np_data = np.array(data, dtype=float)
FAM_data_cell = np_data[:,0,:].T # теперь первый индекс - это номер ячейки на изотерме, второй индекс - номер измерения
CY5_data_cell = np_data[:,1,:].T
colors = ['blue','lime','yellow','orange','red','maroon']
#FAM
# разбиение на четные и нечетные
FAM_2i = FAM_data_cell[:,::2]
FAM_2i_1 = FAM_data_cell[:,1::2]

sh = min(FAM_2i.shape[1],FAM_2i_1.shape[1])
FAM_2i = FAM_2i[:,:sh]
FAM_2i1 = FAM_2i[:,1:sh+1]
FAM_T2i=np.transpose([FAM_2i[:,sh-2:sh]])
#print FAM_T2i
FAM_2i1=np.insert(FAM_2i1,[sh-1],FAM_T2i[0],axis=1)
#print FAM_2i1
FAM_2i_1 = FAM_2i_1[:,:sh]
i=0.5
FAM_ratio = FAM_2i_1 / ((1-i)*FAM_2i+i*FAM_2i1)
# print FAM_ratio
FAM_ini=FAM_ratio[:,5:6].repeat(sh,axis=1)
FAM_fin=FAM_ratio[:,sh-2:sh-1].repeat(sh,axis=1)
FAM_2i_ini=FAM_2i[:,5:6].repeat(sh,axis=1)
FAM_2i_fin=FAM_2i[:,sh-2:sh-1].repeat(sh,axis=1)
# print FAM_2i_fin
# print FAM_test.repeat(sh,axis=1)
FAM_new = -(FAM_ratio-FAM_ini)/(((FAM_2i_fin-FAM_2i_ini)/FAM_2i_ini)*(FAM_ratio-FAM_fin)+FAM_ini-FAM_fin)
#нарисование графиков

#для Стаса старый метод
fig_FAM_old = matplotlib.figure.Figure((10,6))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig_FAM_old)
ax_FAM_old = fig_FAM_old.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax_FAM_old.grid(True)
ax_FAM_old.set_xlabel('cycle')
ax_FAM_old.set_ylabel('FAM old intensivity')
for chan_idx in range(6):
  ax_FAM_old.plot(FAM_2i_1[chan_idx,:], color=colors[chan_idx], label = chan_idx+1)
  ax_FAM_old.legend()
fig_FAM_old.savefig(os.path.join(DIR,'FAM_old.png'), format="png")
np.savetxt(os.path.join(DIR,"FAM_old.csv"), FAM_2i_1.T, fmt='%i', delimiter=";",newline='\n')

#для меня обычный метод
fig_FAM_norm = matplotlib.figure.Figure((10,6))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig_FAM_norm)
ax_FAM_norm = fig_FAM_norm.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax_FAM_norm.grid(True)
ax_FAM_norm.set_xlabel('cycle')
ax_FAM_norm.set_ylabel('FAM norm intensivity')
for chan_idx in range(6):
  ax_FAM_norm.plot(FAM_ratio[chan_idx,:], color=colors[chan_idx], label = chan_idx+1)
  ax_FAM_norm.legend()
fig_FAM_norm.savefig(os.path.join(DIR,'FAM_norm.png'), format="png")
np.savetxt(os.path.join(DIR,"FAM_norm.csv"), FAM_2i_1.T, fmt='%i', delimiter=";",newline='\n')
# для меня новый метод
fig_FAM_new = matplotlib.figure.Figure((10,6))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig_FAM_new)
ax_FAM_new = fig_FAM_new.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax_FAM_new.grid(True)
ax_FAM_new.set_xlabel('cycle')
ax_FAM_new.set_ylabel('FAM new intensivity')
for chan_idx in range(6):
  ax_FAM_new.plot(FAM_new[chan_idx,:], color=colors[chan_idx], label = chan_idx+1)
  ax_FAM_new.legend()
fig_FAM_new.savefig(os.path.join(DIR,'FAM_new.png'), format="png")
np.savetxt("FAM_new.csv", FAM_2i_1.T, fmt='%i', delimiter=";",newline='\n')
#CY5

# разбиение на четные и нечетные
CY5_2i = CY5_data_cell[:,::2]
CY5_2i_1 = CY5_data_cell[:,1::2]

sh = min(CY5_2i.shape[1],CY5_2i_1.shape[1])
CY5_2i = CY5_2i[:,:sh]
CY5_2i_1 = CY5_2i_1[:,:sh]

CY5_ratio = CY5_2i_1 / CY5_2i
#нарисование графиков

#для Стаса старый метод
fig_CY5_old = matplotlib.figure.Figure((10,6))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig_CY5_old)
ax_CY5_old = fig_CY5_old.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax_CY5_old.grid(True)
ax_CY5_old.set_xlabel('cycle')
ax_CY5_old.set_ylabel('CY5 old intensivity')
for chan_idx in range(6):
  ax_CY5_old.plot(CY5_2i_1[chan_idx,:], color=colors[chan_idx], label = chan_idx+1)
  ax_CY5_old.legend()
fig_CY5_old.savefig(os.path.join(DIR,'CY5_old.png'), format="png")
np.savetxt(os.path.join(DIR,"CY5_old.csv"), CY5_2i_1.T, fmt='%i', delimiter=";",newline='\n')

#для меня нормальный метод
fig_CY5_norm = matplotlib.figure.Figure((10,6))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig_CY5_norm)
ax_CY5_norm = fig_CY5_norm.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax_CY5_norm.grid(True)
ax_CY5_norm.set_xlabel('cycle')
ax_CY5_norm.set_ylabel('CY5 norm intensivity')
for chan_idx in range(6):
  ax_CY5_norm.plot(CY5_ratio[chan_idx,:], color=colors[chan_idx], label = chan_idx+1)
  ax_CY5_norm.legend()
fig_CY5_norm.savefig(os.path.join(DIR,'CY5_norm.png'), format="png")
#np.savetxt(os.path.join(DIR,"CY5_norm.csv"), CY5_2i_1.T, fmt='%i', delimiter=";",newline='\n')

CY5_ini=CY5_ratio[:,5:6].repeat(sh,axis=1)
CY5_fin=CY5_ratio[:,sh-2:sh-1].repeat(sh,axis=1)
CY5_2i_ini=CY5_2i[:,5:6].repeat(sh,axis=1)
CY5_2i_fin=CY5_2i[:,sh-2:sh-1].repeat(sh,axis=1)
# print CY5_2i_fin
# print CY5_test.repeat(sh,axis=1)
CY5_new = -(CY5_ratio-CY5_ini)/(((CY5_2i_fin-CY5_2i_ini)/CY5_2i_ini)*(CY5_ratio-CY5_fin)+CY5_ini-CY5_fin)
# для меня новый метод
fig_CY5_new = matplotlib.figure.Figure((10,6))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig_CY5_new)
ax_CY5_new = fig_CY5_new.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax_CY5_new.grid(True)
ax_CY5_new.set_xlabel('cycle')
ax_CY5_new.set_ylabel('CY5 new intensivity')
for chan_idx in range(6):
  ax_CY5_new.plot(CY5_new[chan_idx,:], color=colors[chan_idx], label = chan_idx+1)
  ax_CY5_new.legend()
fig_CY5_new.savefig(os.path.join(DIR,'CY5_new.png'), format="png")
# np.savetxt("CY5_new.csv", CY5_2i_1.T, fmt='%i', delimiter=";",newline='\n')

with open(os.path.join(DIR,'params.ini'), 'w') as configfile:
   ini.write(configfile)
