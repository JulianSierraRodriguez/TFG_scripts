import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import json

f =         "pop_d1_d2_birNB.dat"



Population = True 
Histogram = False
Gibbs = False


######################

v1 = np.loadtxt(f)[:, 0]
v2 = np.loadtxt(f)[:, 1]
p = np.loadtxt(f)[:, 2]


######################


pl = int(len(p))
R = 8.314
T = 300
G = []
for i in range(0, pl, 1):
	i = int(i)
	if p[i] != 0:
		G.insert(i, R*T*np.log(p[i]/50000))
	else:
		G.insert(i, 0)

####################

def population():
	fig1, ax1 = plt.subplots(figsize=(9, 6))
	hexbin = ax1.hexbin(x = v1, y = v2, C = p, gridsize = 101, 
	                   cmap = 'viridis')
	ax1.set_xlabel(r'distance 1')
	ax1.set_ylabel(r'distance 2')
	cb = fig1.colorbar(hexbin, ax = ax1, label = 'Population')
	
	ax1.set_title('Population', size = 14)
	
	plt.savefig('pop_d1_d2_birNBGaMD.png', dpi=600)

####################

def histograms():
	fig3, ax3 = plt.subplots(figsize=(9, 6))
	ax3.bar(v1, p)#, c='darkviolet', marker = ".")#, linestyle = "")
	ax3.set_title('distance 1', size = 14)
	plt.savefig('pop_d1.png', dpi=600)

	fig4, ax4 = plt.subplots(figsize=(9, 6))
	ax4.bar(v2, p)#, c='darkviolet', marker = ".", linestyle = "")
	ax4.set_title('distance 2', size = 14)
	plt.savefig('pop_d2.png', dpi=600)

####################

def gibbs():
	fig5, ax5 = plt.subplots(figsize=(9, 6))
	hexbin = ax5.hexbin(x = v1, y = v2, C = G, gridsize = 21,
	                   cmap = 'winter')
	ax5.set_xlabel(r'dihedral 1')
	ax5.set_ylabel(r'distance 2')
	cb = fig5.colorbar(hexbin, ax = ax5, label = 'Gibbs Energy')
	
	ax5.set_title('Gibbs Energy', size = 14)
	
	plt.savefig('G_d93_d61.png', dpi=600)

####################

if Population:
	population()

if Histogram:
	histograms()

if Gibbs:
	gibbs()


plt.show()
