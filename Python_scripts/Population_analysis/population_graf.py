import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import json

f =         "pop_d1_d2_birNB.dat"
#file_rep =  "data/bak_a93_c0_c9_dist.dat"
#file2_rep = "data/bak_a61_c0_c9_dist.dat"


Population = True 
Histogram = False
Gibbs = False


######################

v1 = np.loadtxt(f)[:, 0]
v2 = np.loadtxt(f)[:, 1]
p = np.loadtxt(f)[:, 2]

#data2_rep = np.loadtxt(file2_rep)[:, 1]
#data_rep = np.loadtxt(file_rep)[:, 1]


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

#	fig2, ax2 = plt.subplots(figsize=(9, 6))
#	hexbin = ax2.hexbin(x = v1, y = v2, C = p, gridsize = 21,
#	                   cmap = 'Purples')
#	ax2.set_xlabel(r'distance $\alpha$9 and $\alpha$3')
#	ax2.set_ylabel(r'distance $\alpha$6 and $\alpha$1')
#	cb = fig2.colorbar(hexbin, ax = ax2, label = 'Population')
#	ax2.set_title('Population', size = 14)
#	
#	ax2.scatter(data_rep[0], data2_rep[0], c='b', marker = ".", linestyle = "", label = 'c0')
#	ax2.scatter(data_rep[1], data2_rep[1], c='b', marker = "*", linestyle = "", label = 'de peu(c1)')
#	ax2.scatter(data_rep[2], data2_rep[2], c='r', marker = ".", linestyle = "", label = '(c2)')
#	ax2.scatter(data_rep[3], data2_rep[3], c='r', marker = ".", linestyle = "", label = 'c3')
#	ax2.scatter(data_rep[4], data2_rep[4], c='r', marker = "*", linestyle = "", label = 'recolzat(c4)')
#	ax2.scatter(data_rep[5], data2_rep[5], c='b', marker = ".", linestyle = "", label = 'c5')
#	ax2.scatter(data_rep[6], data2_rep[6], c='r', marker = ".", linestyle = "", label = 'c6')
#	ax2.scatter(data_rep[7], data2_rep[7], c='r', marker = "*", linestyle = "", label = 'c7')
#	ax2.scatter(data_rep[8], data2_rep[8], c='r', marker = "*", linestyle = "", label = 'c8')
#	ax2.scatter(data_rep[9], data2_rep[9], c='r', marker = "*", linestyle = "", label = 'c9')
#	
#	for i in range(0,10,1):
#	        l = str(i)
#	        i = int(i)
#	        plt.annotate("c"+l, (data_rep[i], data2_rep[i]))
#	
#	plt.savefig('pop_d93_d61_repr.png', dpi=600)

####################
def histograms():
	fig3, ax3 = plt.subplots(figsize=(9, 6))
	ax3.bar(v1, p)#, c='darkviolet', marker = ".")#, linestyle = "")
	ax3.set_title('distance 1', size = 14)
	plt.savefig('pop_d1.png', dpi=600)

####################

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
	
#	fig6, ax6 = plt.subplots(figsize=(9, 6))
#	hexbin = ax6.hexbin(x = v1, y = v2, C = G, gridsize = 21,
#	                   cmap = 'winter')
#	ax6.set_xlabel(r'distance $\alpha$9 and $\alpha$3')
#	ax6.set_ylabel(r'distance $\alpha$6 and $\alpha$1')
#	cb = fig6.colorbar(hexbin, ax = ax6, label = 'Gibbs Energy')
#	ax6.set_title('Gibbs Energy', size = 14)
#	
#	ax6.scatter(data_rep[0], data2_rep[0], c='b', marker = ".", linestyle = "", label = 'c0')
#	ax6.scatter(data_rep[1], data2_rep[1], c='b', marker = "*", linestyle = "", label = 'de peu(c1)')
#	ax6.scatter(data_rep[2], data2_rep[2], c='r', marker = ".", linestyle = "", label = '(c2)')
#	ax6.scatter(data_rep[3], data2_rep[3], c='r', marker = ".", linestyle = "", label = 'c3')
#	ax6.scatter(data_rep[4], data2_rep[4], c='r', marker = "*", linestyle = "", label = 'recolzat(c4)')
#	ax6.scatter(data_rep[5], data2_rep[5], c='b', marker = ".", linestyle = "", label = 'c5')
#	ax6.scatter(data_rep[6], data2_rep[6], c='r', marker = ".", linestyle = "", label = 'c6')
#	ax6.scatter(data_rep[7], data2_rep[7], c='r', marker = "*", linestyle = "", label = 'c7')
#	ax6.scatter(data_rep[8], data2_rep[8], c='r', marker = "*", linestyle = "", label = 'c8')
#	ax6.scatter(data_rep[9], data2_rep[9], c='r', marker = "*", linestyle = "", label = 'c9')
#	
#	for i in range(0,10,1):
#	        l = str(i)
#	        i = int(i)
#	        plt.annotate("c"+l, (data_rep[i], data2_rep[i]))
#	
#	plt.savefig('G_d93_d61_repr.png', dpi=600)

####################
if Population:
	population()

if Histogram:
	histograms()

if Gibbs:
	gibbs()


plt.show()
