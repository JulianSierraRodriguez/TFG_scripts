import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import json

file1 = "bak_B3a_dist.dat"
#file1_rep = "bak_bir_NB_GaMD_OBS_dist2.dat"
file2 = "bak_B3a_dist.dat"
#file2_rep = "bak_a61_c0_c9_dist.dat"

data1 = np.loadtxt(file1)[:, 1]
#data1_rep = np.loadtxt(file1_rep)[:, 1]
data2 = np.loadtxt(file2)[:, 1]
#data2_rep = np.loadtxt(file2_rep)[:, 1]

min_data1 = min(data1)
max_data1 = max(data1)

min_data2 = min(data2)
max_data2 = max(data2)

print('Minimum of d1:', min_data1)
print('Maximum of d1:', max_data1)
print('Minimum of d2:', min_data2)
print('Maximum of d2:', max_data2)

n = 0.1
s = 1

d1 = np.arange(min_data1, max_data1+n, n)
d2 = np.arange(min_data2, max_data2+n, n)
pop = []
temp2 = []
for i in d1:
   for j in d2:
       i = round(i, s)
       j = round(j, s)
       temp = [i, j, 0]
       temp2 = pop.append(temp)

l_data = len(data1)
l_pop = print(len(pop))

m = 0

for i1 in range(l_data):
    i1=int(i1)
    temp_data1 = data1[i1]
    temp_data1 = round(temp_data1, 1)
    temp_data2 = data2[i1]
    temp_data2 = round(temp_data2, 2)
    m = m + 1
    
    for i2 in range(len(pop)):
        i2 = int(i2)
        if  pop[i2][0] == temp_data1 and pop[i2][1] == temp_data2:
            pop[i2][2] = pop[i2][2] + 1
            #print(pop[i2])
            #print(m)
###############################

f = open("pop_d1_d2_birNB.dat", "w")
lpop = len(pop)

for line in range(lpop):
        n = int(line)
        l = ""

        a = pop[n][0]
#        if a in np.arange(-200.0, -99.0, 1):
#                a = str(a)+" "
#        elif a in np.arange(-99.0, -9.0, 1):
#                a = " " + str(a) + " "
#        elif a in np.arange(-9.0, 0.0, 1):
#                a = "  " + str(a) + " "
#        elif a in np.arange(0.0, 10.0, 1):
#                a = "   " + str(a) + " "
#        elif a in np.arange(10.0, 100.0, 1):
#                a = "  " + str(a) + " "
#        elif a in np.arange(100.0, 200.0, 1):
#                a = " " + str(a) + " "
        a = str(pop[n][0])
        b = str(pop[n][1])
        c = str(pop[n][2])

        l= a + " " + b + " " + c
        f.write(l + "\n")

f.close()

###########################################

#x = np.take(pop, indices=0, axis=1)
#y = np.take(pop, indices=1, axis=1)
#color = np.take(pop, indices=2, axis=1)
#
#
#fig1, ax1 = plt.subplots(figsize=(9, 6))
#hexbin = ax1.hexbin(x = x, y = y, C = color, gridsize = 40, 
#                   cmap = 'Reds')
#ax1.set_xlabel(r'dihedral $\alpha$6 and $\alpha$5')
#ax1.set_ylabel(r'distance $\alpha$6 and $\alpha$1')
#cb = fig1.colorbar(hexbin, ax = ax1, label = 'Population')
#
#ax1.set_title('Population', size = 14)
#
#plt.savefig('pop_def.png', dpi=600)
#
#
#fig2, ax2 = plt.subplots(figsize=(9, 6))
#hexbin = ax2.hexbin(x = x, y = y, C = color, gridsize = 40,
#                   cmap = 'Reds')
#ax2.set_xlabel(r'dihedral $\alpha$6 and $\alpha$5')
#ax2.set_ylabel(r'distance $\alpha$6 and $\alpha$1')
#cb = fig2.colorbar(hexbin, ax = ax2, label = 'Population')
#ax2.set_title('Population', size = 14)
#
#ax2.scatter(data_rep[0], data2_rep[0], c='darkviolet', marker = ".", linestyle = "", label = 'c0')
#ax2.scatter(data_rep[1], data2_rep[1], c='r', marker = "*", linestyle = "", label = 'de peu(c1)')
#ax2.scatter(data_rep[2], data2_rep[2], c='b', marker = "*", linestyle = "", label = 'inclinat(c2)')
#ax2.scatter(data_rep[3], data2_rep[3], c='b', marker = ".", linestyle = "", label = 'c3')
#ax2.scatter(data_rep[4], data2_rep[4], c='m', marker = "*", linestyle = "", label = 'recolzat(c4)')
#ax2.scatter(data_rep[5], data2_rep[5], c='r', marker = ".", linestyle = "", label = 'c5')
#ax2.scatter(data_rep[6], data2_rep[6], c='b', marker = ".", linestyle = "", label = 'c6')
#ax2.scatter(data_rep[7], data2_rep[7], c='m', marker = "v", linestyle = "", label = 'c7')
#ax2.scatter(data_rep[8], data2_rep[8], c='m', marker = "v", linestyle = "", label = 'c8')
#ax2.scatter(data_rep[9], data2_rep[9], c='m', marker = "v", linestyle = "", label = 'c9')
#
#
#plt.savefig('pop_def_repr.png', dpi=600)
#
#
#plt.show()
