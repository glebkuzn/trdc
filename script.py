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

FLAG=[0,0,0,0,0,0]
devia=[0,0,0,0,0,0]
FAM_baseline=[0,0,0,0,0,0]
CY5_baseline=[0,0,0,0,0,0]
Cp=[0,0,0,0,0,0]
Cp2=[0,0,0,0,0,0]
devia2=[0,0,0,0,0,0]
fig = matplotlib.figure.Figure((10,5))
from matplotlib.backends import backend_svg as backend
backend.new_figure_manager_given_figure(1, fig)

ax = fig.add_axes((0.1,0.1,0.9,0.9), frameon=True)
ax.grid(True)

if trdc_pcr_loaded:
  data = trdc_pcr.get_all_data()
else:
  data = \
    [[[13296, 39759, 41013, 24378, 43834, 30710],
      [14879, 10210, 44665, 10020, 50394, 45862],
      [40501, 11252, 13219, 51764, 10178, 10308],
      [47722, 38840, 26149, 19665, 42453, 50124],
      [43994, 31305, 32838, 55408, 59680, 19092],
      [57537, 29257, 11479, 12962, 10554, 29594]],
     [[18579, 10091, 59640, 52044, 35009, 55495],
      [47482, 32409, 52265, 13291, 28428, 13408],
      [20886, 53591, 58564, 12974, 58714, 57898],
      [34652, 15057, 32860, 24612, 30811, 11373],
      [51887, 46251, 18786, 41068, 12272, 48347],
      [50759, 47702, 23693, 34006, 58530, 14746]],
     [[50900, 51944, 28037, 30247, 22826, 51062],
      [30416, 16946, 17137, 47097, 27372, 26753],
      [28456, 26076, 59976, 52787, 50046, 23753],
      [34667, 30159, 12489, 14834, 36240, 25249],
      [44785, 24593, 38251, 14606, 44524, 43427],
      [21157, 26000, 12664, 26560, 11078, 40468]],
     [[24557, 51507, 18157, 58238, 40557, 27952],
      [50806, 16569, 36464, 20780, 36692, 24442],
      [59627, 12904, 20323, 35924, 21868, 48548],
      [44924, 33269, 39614, 44727, 39224, 56743],
      [34872, 33627, 31676, 49402, 13114, 26363],
      [46031, 13654, 14394, 24690, 48437, 40107]],
     [[27992, 46232, 12496, 29577, 59409, 11334],
      [17682, 24910, 45042, 29556, 54189, 33967],
      [38756, 16735, 44486, 28472, 27316, 40742],
      [54014, 10305, 16057, 25912, 50012, 33921],
      [48538, 12968, 38549, 20205, 48815, 12312],
      [24074, 58515, 28119, 21614, 41508, 54837]],
     [[27992, 46232, 12496, 29577, 59409, 11334],
      [17682, 24910, 45042, 29556, 54189, 33967],
      [38756, 16735, 44486, 28472, 27316, 40742],
      [54014, 10305, 16057, 25912, 50012, 33921],
      [48538, 12968, 38549, 20205, 48815, 12312],
      [24074, 58515, 28119, 21614, 41508, 54837]],
     [[27992, 46232, 12496, 29577, 59409, 11334],
      [17682, 24910, 45042, 29556, 54189, 33967],
      [38756, 16735, 44486, 28472, 27316, 40742],
      [54014, 10305, 16057, 25912, 50012, 33921],
      [48538, 12968, 38549, 20205, 48815, 12312],
      [24074, 58515, 28119, 21614, 41508, 54837]],
     [[27992, 46232, 12496, 29577, 59409, 11334],
      [17682, 24910, 45042, 29556, 54189, 33967],
      [38756, 16735, 44486, 28472, 27316, 40742],
      [54014, 10305, 16057, 25912, 50012, 33921],
      [48538, 12968, 38549, 20205, 48815, 12312],
      [24074, 58515, 28119, 21614, 41508, 54837]],
     [[27992, 46232, 12496, 29577, 59409, 11334],
      [17682, 24910, 45042, 29556, 54189, 33967],
      [38756, 16735, 44486, 28472, 27316, 40742],
      [54014, 10305, 16057, 25912, 50012, 33921],
      [48538, 12968, 38549, 20205, 48815, 12312],
      [24074, 58515, 28119, 21614, 41508, 54837]]]


np_data = np.array(data, dtype=float)
# print np_data[:,0,:]
#print np_data.shape
FAM_data_cell = np_data[:,0,:].T # теперь первый индекс - это номер ячейки на изотерме, второй индекс - номер измерения
#print FAM_data_cell.shape
CY5_data_cell = np_data[:,1,:].T
#print FAM_data_cell
colors = ['blue','lime','yellow','orange','red','maroon']

FAM_2i = FAM_data_cell[:,::2]
FAM_2i_1 = FAM_data_cell[:,1::2]

sh = min(FAM_2i.shape[1],FAM_2i_1.shape[1])
FAM_2i = FAM_2i[:,:sh]
FAM_2i_1 = FAM_2i_1[:,:sh]

FAM_ratio = FAM_2i_1 / FAM_2i

for chan_idx in range(6):
  ax.plot(FAM_2i_1[chan_idx,:], color=colors[chan_idx])

fig2=fig.savefig('img-fam.png', format="png")

#FAM_2i_1.T.tofile('fam.csv',sep=';',format='%i')
#np.savetxt("fam.csv", a, delimiter=";",format='%i')
#np.savetxt('fam', FAM_2i_1)
'''
CY5_2i = CY5_data_cell[:,::2]
CY5_2i_1 = CY5_data_cell[:,1::2]

sh = min(CY5_2i.shape[1],CY5_2i_1.shape[1])
CY5_2i = CY5_2i[:,:sh]
CY5_2i_1 = CY5_2i_1[:,:sh]

CY5_ratio = CY5_2i_1 / CY5_2i

for chan_idx in range(6):
  plot1=ax.plot(CY5_ratio[chan_idx,:], color=colors[chan_idx])

fig.savefig('img-CY5.png', format="png")
'''
def avg(x):
  return np.average(x)

def rms(x):
  xa = avg(x)
  return np.sqrt(np.mean(np.square(x-xa)))
'''
print '%i AVG RMS %%' % (len(FAM_data_cell[0]))
for i in range(6):
	print 'FAM#%d %d %d %.2f' % (i+1,avg(FAM_data_cell[i]),rms(FAM_data_cell[i]),rms(FAM_data_cell[i])/avg(FAM_data_cell[i])*100)
	for cycle in range(len(FAM_data_cell[0])):
		if cycle>10:
			if devia[i]<(FAM_data_cell[i][cycle]-FAM_data_cell[i][cycle-1]):
				devia[i]=FAM_data_cell[i][cycle]-FAM_data_cell[i][cycle-1]
				Cp[i]=cycle
				if cycle<10:
					if abs(devia[i])>1000:
						FLAG[i]=1
				if abs(devia[i])>1000:
					FLAG[i]=2
			if devia2[i]<(FAM_data_cell[i][cycle]-2*FAM_data_cell[i][cycle-2]+FAM_data_cell[i][cycle-4]):
				devia2[i]=FAM_data_cell[i][cycle]-2*FAM_data_cell[i][cycle-2]+FAM_data_cell[i][cycle-4]
				Cp2[i]=cycle
			if cycle==44:
				FAM_baseline[i]=(FAM_data_cell[i][42]-FAM_data_cell[i][38])/4																													

print '\n'

print '%i Cpmin Amp' % (len(FAM_data_cell[0]))
for i in range(6):
	Cpmin=max(Cp2[i],Cp[i]-2)
	print 'FAM#%d %d %d' % (i+1,Cpmin,min((FAM_data_cell[i][len(FAM_data_cell[0])-2]-FAM_data_cell[i][Cpmin]),(FAM_data_cell[i][len(FAM_data_cell[0])-2]-FAM_data_cell[i][Cpmin])-FAM_baseline[i]*(len(FAM_data_cell[0])-1-Cpmin)))
print '\n'
print '%i base Cp1 Cp2 Cpmin Amp Amp-base bubble' % (len(FAM_data_cell[0]))
for i in range(6):
	Cpmin=min(Cp2[i],Cp[i]-2)
	print 'FAM#%d %d %d %d %d %d %d %d' % (i+1,FAM_baseline[i],Cp[i],Cp2[i],Cpmin,(FAM_data_cell[i][len(FAM_data_cell[0])-2]-FAM_data_cell[i][Cpmin]),(FAM_data_cell[i][len(FAM_data_cell[0])-2]-FAM_data_cell[i][Cpmin])-FAM_baseline[i]*(len(FAM_data_cell[0])-1-Cpmin),FLAG[i])


#print CY5_data_cell
colors = ['blue','lime','yellow','orange','red','maroon']

for chan_idx in range(6):
  ax.plot(np_data[:,1,chan_idx], color=colors[chan_idx])
'''
def avg(x):
  return np.average(x)

def rms(x):
  xa = avg(x)
  return np.sqrt(np.mean(np.square(x-xa)))
'''
print '%i AVG RMS %%' % (len(CY5_data_cell[0]))
for i in range(6):
	print 'CY5#%d %d %d %.2f' % (i+1,avg(CY5_data_cell[i]),rms(CY5_data_cell[i]),rms(CY5_data_cell[i])/avg(CY5_data_cell[i])*100)
	for cycle in range(len(CY5_data_cell[0])):
		if cycle>10:
			if devia[i]<(CY5_data_cell[i][cycle]-CY5_data_cell[i][cycle-4]):
				devia[i]=CY5_data_cell[i][cycle]-CY5_data_cell[i][cycle-4]
				Cp[i]=cycle-2
				if cycle<10:
					if abs(devia[i])>1000:
						FLAG[i]=1
				if abs(devia[i])>1000:
					FLAG[i]=2
			if devia2[i]<(CY5_data_cell[i][cycle]-2*CY5_data_cell[i][cycle-1]+CY5_data_cell[i][cycle-2]):
				devia2[i]=CY5_data_cell[i][cycle]-2*CY5_data_cell[i][cycle-1]+CY5_data_cell[i][cycle-2]
				Cp2[i]=cycle
			if cycle==44:
				CY5_baseline[i]=(CY5_data_cell[i][42]-CY5_data_cell[i][38])/4																													

print '\n'

print '%i Cpmin Amp' % (len(CY5_data_cell[0]))
for i in range(6):
	Cpmin=max(Cp2[i],Cp[i]-6)
	print 'CY5#%d %d %d' % (i+1,Cpmin,min((CY5_data_cell[i][len(CY5_data_cell[0])-2]-CY5_data_cell[i][Cpmin]),(CY5_data_cell[i][len(CY5_data_cell[0])-2]-CY5_data_cell[i][Cpmin])-CY5_baseline[i]*(len(CY5_data_cell[0])-1-Cpmin)))
print '\n'

print '%i base Cp1 Cp2 Cpmin Amp Amp-base bubble' % (len(CY5_data_cell[0]))
for i in range(6):
	Cpmin=min(Cp2[i],Cp[i]-6)
	print 'CY5#%d %d %d %d %d %d %d %d' % (i+1,CY5_baseline[i],Cp[i],Cp2[i],Cpmin,(CY5_data_cell[i][len(CY5_data_cell[0])-2]-CY5_data_cell[i][Cpmin]),(CY5_data_cell[i][len(CY5_data_cell[0])-2]-CY5_data_cell[i][Cpmin])-CY5_baseline[i]*(len(CY5_data_cell[0])-1-Cpmin),FLAG[i])
'''
print '%i avg rms' % (len(CY5_data_cell[0]))
for i in range(6):	
	print 'CY5#%d %d %d' % (i+1,avg(CY5_data_cell[i]),rms(CY5_data_cell[i]))
for i in range(6):	
	print 'FAM#%d %d %d' % (i+1,avg(FAM_data_cell[i]),rms(FAM_data_cell[i]))
#~ print FAM_data_cell[0]
#~ print FAM_data_cell[1]
#~ print FAM_data_cell[2]
#~ print FAM_data_cell[3]
#~ print FAM_data_cell[4]
#~ print FAM_data_cell[5]

#~ print CY5_data_cell[0]
#~ print CY5_data_cell[1]
#~ print CY5_data_cell[2]
#~ print CY5_data_cell[3]
#~ print CY5_data_cell[4]
#~ print CY5_data_cell[5]

