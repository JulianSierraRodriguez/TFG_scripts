import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from PIL import Image
import scipy.stats as st
import statistics



mpl.rcParams['mathtext.default'] = 'regular'

labels = False 
size_label = 7
fig = 'plt_a95_a_mem_a9.png'


##################

file_bir  = "data/bak_bir_a95.dat"
file2_bir = "data/bak_bir_a_mem_a9.dat"

file_birG  = "data/bak_birG_a95.dat"
file2_birG = "data/bak_birG_a_mem_a9.dat"

file_birN  = "data/bak_birN_a95.dat"
file2_birN = "data/bak_birN_a_mem_a9.dat"

file_birNG  = "data/bak_birNG_a95.dat"
file2_birNG = "data/bak_birNG_a_mem_a9.dat"

#####

file_17L  = "data/bak_17L_a95.dat"
file2_17L = "data/bak_17L_a_mem_a9.dat"

file_17LG  = "data/bak_17LG_a95.dat"
file2_17LG = "data/bak_17LG_a_mem_a9.dat"

file_17LN  = "data/bak_17LN_a95.dat"
file2_17LN = "data/bak_17LN_a_mem_a9.dat"

file_17LNG  = "data/bak_17LNG_a95.dat"
file2_17LNG = "data/bak_17LNG_a_mem_a9.dat"

#####

file_4G  = "data/bak_4G_a95.dat"
file2_4G = "data/bak_4G_a_mem_a9.dat"

file_4GG  = "data/bak_4GG_a95.dat"
file2_4GG = "data/bak_4GG_a_mem_a9.dat"

file_4GN  = "data/bak_4GN_a95.dat"
file2_4GN = "data/bak_4GN_a_mem_a9.dat"

file_4GNG  = "data/bak_4GNG_a95.dat"
file2_4GNG = "data/bak_4GNG_a_mem_a9.dat"

######

file_10  = "data/bak_10_a95.dat"
file2_10 = "data/bak_10_a_mem_a9.dat"

file_10G  = "data/bak_10G_a95.dat"
file2_10G = "data/bak_10G_a_mem_a9.dat"

file_10N  = "data/bak_10N_a95.dat"
file2_10N = "data/bak_10N_a_mem_a9.dat"

file_10NG  = "data/bak_10NG_a95.dat"
file2_10NG = "data/bak_10NG_a_mem_a9.dat"

#####

data_bir  = np.loadtxt(file_bir)[:, 1]
data2_bir = np.loadtxt(file2_bir)[:, 1]

data_birG  = np.loadtxt(file_birG)[:, 1]
data2_birG = np.loadtxt(file2_birG)[:, 1]

data_birN  = np.loadtxt(file_birN)[:, 1]
data2_birN = np.loadtxt(file2_birN)[:, 1]

data_birNG  = np.loadtxt(file_birNG)[:, 1]
data2_birNG = np.loadtxt(file2_birNG)[:, 1]

#####

data_17L  = 1 
data2_17L = np.loadtxt(file2_17L)[:, 1]

data_17LG  = 1
data2_17LG = np.loadtxt(file2_17LG)[:, 1]

data_17LN  = 1
data2_17LN = np.loadtxt(file2_17LN)[:, 1]

data_17LNG  = 1
data2_17LNG = np.loadtxt(file2_17LNG)[:, 1]

#####

data_4G  = np.loadtxt(file_4G)[:, 1]
data2_4G = np.loadtxt(file2_4G)[:, 1]

data_4GG  = np.loadtxt(file_4GG)[:, 1]
data2_4GG = np.loadtxt(file2_4GG)[:, 1]

data_4GN  = np.loadtxt(file_4GN)[:, 1]
data2_4GN = np.loadtxt(file2_4GN)[:, 1]

data_4GNG  = np.loadtxt(file_4GNG)[:, 1]
data2_4GNG = np.loadtxt(file2_4GNG)[:, 1]

######

data_10  = np.loadtxt(file_10)[:, 1]
data2_10 = np.loadtxt(file2_10)[:, 1]

data_10G  = np.loadtxt(file_10G)[:, 1]
data2_10G = np.loadtxt(file2_10G)[:, 1]

data_10N  = np.loadtxt(file_10N)[:, 1]
data2_10N = np.loadtxt(file2_10N)[:, 1]

data_10NG  = np.loadtxt(file_10NG)[:, 1]
data2_10NG = np.loadtxt(file2_10NG)[:, 1]

#####

def arreglador_de_puntos(data):
	for j in range(len(data)):
		J = int(j)
		if data[J] >100 :
			data[J] = 180 - data[J]
#	return data


#####

# fig1, ax1 = plt.subplots(figsize=(10,7))
# ax1.get_xaxis().set_visible(False)


########################################################
#%%
x = 0
data_bir = np.concatenate((data2_bir, data2_birG, data2_birN, data2_birNG), axis = None)
arreglador_de_puntos(data_bir)
# ax1.scatter(np.zeros_like(data_bir)+x,data_bir)
#ax1.errorbar(np.zeros_like(data_bir)+x,data_bir, color='black')
#ax1.boxplot(data_bir, whis=99, positions=[0,1])
#plt.setp(box['data_bir'][0], color='black')

##################################################

x = 1
data_17L = np.concatenate((data2_17L, data2_17LG, data2_17LN, data2_17LNG), axis = None)

arreglador_de_puntos(data_17L)

# ax1.scatter(np.zeros_like(data_17L)+x,data_17L)

####################################################
x = 2
data_4G = np.concatenate((data2_4G, data2_4GG, data2_4GN, data2_4GNG), axis = None)

arreglador_de_puntos(data_4G)

# ax1.scatter(np.zeros_like(data_4G)+x,data_4G)

####################################################
x = 3

data_10 = np.concatenate(( data2_10N, data2_10NG), axis = None)

arreglador_de_puntos(data_10)


# ax1.text(0-0.02,-4, 'bir', bbox=dict(facecolor='w', edgecolor = 'b'))
# ax1.text(1-0.02,-4, '17L', bbox=dict(facecolor='w', edgecolor = 'orange'))
# ax1.text(2-0.02,-4, '4G', bbox=dict(facecolor='w', edgecolor = 'g'))
# ax1.text(3-0.02,-4, '10', bbox=dict(facecolor='w', edgecolor = 'r'))

####################################################
#%%

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)
ax1.hist(data_bir, bins=400)
ax1.set_title('Bir')
ax1.set_xlabel('Protein angle of insertion')
# print(statistics.mean(data_bir), np.median(data_bir), st.iqr(data_bir))
ax2.hist(data_17L, bins=400)
ax2.set_title('17L')
ax2.set_xlabel('Protein angle of insertion')
ax3.hist(data_4G, bins=400)
ax3.set_xlabel('Protein angle of insertion')
ax3.set_title('4G')
ax4.hist(data_10, bins=400)
ax4.set_title('10')
ax4.set_xlabel('Protein angle of insertion')
plt.tight_layout()
plt.savefig('Complete_angle_histograms.png', dpi=600)

plt.show()

plt.close()
#%%

print('BIR:')
print('median:   '+str(np.median(data_bir)))
print('Quantiles:   '+str(np.quantile(data_bir, [0,0.25,0.5,0.75,1])))
print('IQR:    '+str(st.iqr(data_bir)))
print('\n')

print('17L:')
print('median:   '+str(np.median(data_17L)))
print('Quantiles:   '+str(np.quantile(data_17L, [0,0.25,0.5,0.75,1])))
print('IQR:    '+str(st.iqr(data_17L)))
print('\n')

print('4G:')
print('median:   '+str(np.median(data_4G)))
print('Quantiles:   '+str(np.quantile(data_4G, [0,0.25,0.5,0.75,1])))
print('IQR:    '+str(st.iqr(data_4G)))
print('\n')

print('10:')
print('median:   '+str(np.median(data_10)))
print('Quantiles:   '+str(np.quantile(data_10, [0,0.25,0.5,0.75,1])))
print('IQR:    '+str(st.iqr(data_10)))
print('\n')