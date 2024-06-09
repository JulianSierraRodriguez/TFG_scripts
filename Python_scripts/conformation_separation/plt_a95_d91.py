import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import matplotlib as mpl
from PIL import Image


mpl.rcParams['mathtext.default'] = 'regular'

labels = False
size_label = 7
fig = 'plt_a95_d91.png'


##################

file_bir  = "data/bak_bir_a95.dat"
file2_bir = "data/bak_bir_d91.dat"

file_birG  = "data/bak_birG_a95.dat"
file2_birG = "data/bak_birG_d91.dat"

file_birN  = "data/bak_birN_a95.dat"
file2_birN = "data/bak_birN_d91.dat"

file_birNG  = "data/bak_birNG_a95.dat"
file2_birNG = "data/bak_birNG_d91.dat"

#####

file_17L  = "data/bak_17L_a95.dat"
file2_17L = "data/bak_17L_d91.dat"

file_17LG  = "data/bak_17LG_a95.dat"
file2_17LG = "data/bak_17LG_d91.dat"

file_17LN  = "data/bak_17LN_a95.dat"
file2_17LN = "data/bak_17LN_d91.dat"

file_17LNG  = "data/bak_17LNG_a95.dat"
file2_17LNG = "data/bak_17LNG_d91.dat"

#####

file_4G  = "data/bak_4G_a95.dat"
file2_4G = "data/bak_4G_d91.dat"

file_4GG  = "data/bak_4GG_a95.dat"
file2_4GG = "data/bak_4GG_d91.dat"

file_4GN  = "data/bak_4GN_a95.dat"
file2_4GN = "data/bak_4GN_d91.dat"

file_4GNG  = "data/bak_4GNG_a95.dat"
file2_4GNG = "data/bak_4GNG_d91.dat"

######

file_10  = "data/bak_10_a95.dat"
file2_10 = "data/bak_10_d91.dat"

file_10G  = "data/bak_10G_a95.dat"
file2_10G = "data/bak_10G_d91.dat"

file_10N  = "data/bak_10N_a95.dat"
file2_10N = "data/bak_10N_d91.dat"

file_10NG  = "data/bak_10NG_a95.dat"
file2_10NG = "data/bak_10NG_d91.dat"

####

data_bir  = np.loadtxt(file_bir)[:, 1]
data2_bir = np.loadtxt(file2_bir)[:, 1]

data_birG  = np.loadtxt(file_birG)[:, 1]
data2_birG = np.loadtxt(file2_birG)[:, 1]

data_birN  = np.loadtxt(file_birN)[:, 1]
data2_birN = np.loadtxt(file2_birN)[:, 1]

data_birNG  = np.loadtxt(file_birNG)[:, 1]
data2_birNG = np.loadtxt(file2_birNG)[:, 1]

#####

data_17L  = np.loadtxt(file_17L)[:, 1]
data2_17L = np.loadtxt(file2_17L)[:, 1]

data_17LG  = np.loadtxt(file_17LG)[:, 1]
data2_17LG = np.loadtxt(file2_17LG)[:, 1]

data_17LN  = np.loadtxt(file_17LN)[:, 1]
data2_17LN = np.loadtxt(file2_17LN)[:, 1]

data_17LNG  = np.loadtxt(file_17LNG)[:, 1]
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

fig1, ax1 = plt.subplots(figsize=(10,7))

########################################################

ax1.scatter(data_bir[0], data2_bir[0], c='m', marker = ".", linestyle = "", label = 'bir')
ax1.scatter(data_bir[1], data2_bir[1], c='m', marker = ".", linestyle = "")
ax1.scatter(data_bir[2], data2_bir[2], c='m', marker = ".", linestyle = "")
# data_bir[3] = data_bir[3] - 360
# data2_bir[3] = data2_bir[3] - 360
ax1.scatter(data_bir[3], data2_bir[3], c='m', marker = ".", linestyle = "")
ax1.scatter(data_bir[4], data2_bir[4], c='m', marker = ".", linestyle = "")
ax1.scatter(data_bir[5], data2_bir[5], c='m', marker = ".", linestyle = "")
ax1.scatter(data_bir[6], data2_bir[6], c='darkred', marker = ".", linestyle = "")
ax1.scatter(data_bir[7], data2_bir[7], c='m', marker = ".", linestyle = "")
ax1.scatter(data_bir[8], data2_bir[8], c='darkred', marker = ".", linestyle = "")
ax1.scatter(data_bir[9], data2_bir[9], c='crimson', marker = ".", linestyle = "")

data_birG[0] = data_birG[0] - 360
ax1.scatter(data_birG[0], data2_birG[0], c='g', marker = ".", linestyle = "")
ax1.scatter(data_birG[1], data2_birG[1], c='g', marker = ".", linestyle = "")
ax1.scatter(data_birG[2], data2_birG[2], c='g', marker = ".", linestyle = "")
data_birG[3] = data_birG[3] - 360
ax1.scatter(data_birG[3], data2_birG[3], c='g', marker = ".", linestyle = "")
data_birG[4] = data_birG[4] - 360
ax1.scatter(data_birG[4], data2_birG[4], c='m', marker = ".", linestyle = "")
data_birG[5] = data_birG[5] - 360
ax1.scatter(data_birG[5], data2_birG[5], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birG[6], data2_birG[6], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birG[7], data2_birG[7], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birG[8], data2_birG[8], c='g', marker = ".", linestyle = "")
data_birG[9] = data_birG[9] - 360
ax1.scatter(data_birG[9], data2_birG[9], c='m', marker = ".", linestyle = "")

ax1.scatter(data_birN[0], data2_birN[0], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[1], data2_birN[1], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[2], data2_birN[2], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[3], data2_birN[3], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[4], data2_birN[4], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[5], data2_birN[5], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[6], data2_birN[6], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[7], data2_birN[7], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[8], data2_birN[8], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birN[9], data2_birN[9], c='m', marker = ".", linestyle = "")

ax1.scatter(data_birNG[0], data2_birNG[0], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[1], data2_birNG[1], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[2], data2_birNG[2], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[3], data2_birNG[3], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[4], data2_birNG[4], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[5], data2_birNG[5], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[6], data2_birNG[6], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[7], data2_birNG[7], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[8], data2_birNG[8], c='m', marker = ".", linestyle = "")
ax1.scatter(data_birNG[9], data2_birNG[9], c='m', marker = ".", linestyle = "")

##################################################

ax1.scatter(data_17L[0], data2_17L[0], c='b', marker = "s", linestyle = "", label = '17L')
ax1.scatter(data_17L[1], data2_17L[1], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17L[2], data2_17L[2], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17L[3], data2_17L[3], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17L[4], data2_17L[4], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17L[5], data2_17L[5], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17L[6], data2_17L[6], c='r', marker = "s", linestyle = "")
# data_17L[7] = data_17L[7] + 360
ax1.scatter(data_17L[7], data2_17L[7], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17L[8], data2_17L[8], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17L[9], data2_17L[9], c='r', marker = "s", linestyle = "")

ax1.scatter(data_17LG[0], data2_17LG[0], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[1], data2_17LG[1], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[2], data2_17LG[2], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[3], data2_17LG[3], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[4], data2_17LG[4], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[5], data2_17LG[5], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[6], data2_17LG[6], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[7], data2_17LG[7], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[8], data2_17LG[8], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LG[9], data2_17LG[9], c='r', marker = "s", linestyle = "")

ax1.scatter(data_17LN[0], data2_17LN[0], c='b', marker = "s", linestyle = "")
# data_17LN[1] = data_17LN[1] + 360
ax1.scatter(data_17LN[1], data2_17LN[1], c='r', marker = "s", linestyle = "")
# data_17LN[2] = data_17LN[2] + 360
ax1.scatter(data_17LN[2], data2_17LN[2], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LN[3], data2_17LN[3], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LN[4], data2_17LN[4], c='r', marker = "s", linestyle = "")
# data_17LN[5] = data_17LN[5] + 360
ax1.scatter(data_17LN[5], data2_17LN[5], c='b', marker = "s", linestyle = "")
# data_17LN[6] = data_17LN[6] + 360
ax1.scatter(data_17LN[6], data2_17LN[6], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LN[7], data2_17LN[7], c='b', marker = "s", linestyle = "")
# data_17LN[8] = data_17LN[8] + 360
ax1.scatter(data_17LN[8], data2_17LN[8], c='b', marker = "s", linestyle = "")
# data_17LN[9] = data_17LN[9] + 360
ax1.scatter(data_17LN[9], data2_17LN[9], c='r', marker = "s", linestyle = "")

ax1.scatter(data_17LNG[0], data2_17LNG[0], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[1], data2_17LNG[1], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[2], data2_17LNG[2], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[3], data2_17LNG[3], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[4], data2_17LNG[4], c='r', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[5], data2_17LNG[5], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[6], data2_17LNG[6], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[7], data2_17LNG[7], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[8], data2_17LNG[8], c='b', marker = "s", linestyle = "")
ax1.scatter(data_17LNG[9], data2_17LNG[9], c='r', marker = "s", linestyle = "")


####################################################

ax1.scatter(data_4G[0], data2_4G[0], c='c', marker = "^", linestyle = "", label = '4G')
ax1.scatter(data_4G[1], data2_4G[1], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[2], data2_4G[2], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[3], data2_4G[3], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[4], data2_4G[4], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[5], data2_4G[5], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[6], data2_4G[6], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[7], data2_4G[7], c='c', marker = "^", linestyle = "")
# data2_4G[8] = data2_4G[8] - 360
ax1.scatter(data_4G[8], data2_4G[8], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4G[9], data2_4G[9], c='c', marker = "^", linestyle = "")

# ax1.scatter(data_4GG[0], data2_4GG[0], c='mediumspringgreen', marker = "^", linestyle = "")
# ax1.scatter(data_4GG[1], data2_4GG[1], c='mediumspringgreen', marker = "^", linestyle = "")
# data_4GG[2] = data_4GG[2] + 360
# ax1.scatter(data_4GG[2], data2_4GG[2], c='mediumspringgreen', marker = "^", linestyle = "")
# data_4GG[3] = data_4GG[3] + 360
# ax1.scatter(data_4GG[3], data2_4GG[3], c='mediumspringgreen', marker = "^", linestyle = "")
# data_4GG[4] = data_4GG[4] + 360
# ax1.scatter(data_4GG[4], data2_4GG[4], c='mediumspringgreen', marker = "^", linestyle = "")
# data_4GG[5] = data_4GG[5] + 360
# ax1.scatter(data_4GG[5], data2_4GG[5], c='mediumspringgreen', marker = "^", linestyle = "")
# ax1.scatter(data_4GG[6], data2_4GG[6], c='mediumspringgreen', marker = "^", linestyle = "")
# ax1.scatter(data_4GG[7], data2_4GG[7], c='mediumspringgreen', marker = "^", linestyle = "")
# ax1.scatter(data_4GG[8], data2_4GG[8], c='mediumspringgreen', marker = "^", linestyle = "")
# data_4GG[9] = data_4GG[9] + 360
# ax1.scatter(data_4GG[9], data2_4GG[9], c='mediumspringgreen', marker = "^", linestyle = "")

ax1.scatter(data_4GN[0], data2_4GN[0], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[1], data2_4GN[1], c='c', marker = "^", linestyle = "")
# data2_4GN[2] = data2_4GN[2] - 360
ax1.scatter(data_4GN[2], data2_4GN[2], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[3], data2_4GN[3], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[4], data2_4GN[4], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[5], data2_4GN[5], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[6], data2_4GN[6], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[7], data2_4GN[7], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[8], data2_4GN[8], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GN[9], data2_4GN[9], c='c', marker = "^", linestyle = "")

ax1.scatter(data_4GNG[0], data2_4GNG[0], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[1], data2_4GNG[1], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[2], data2_4GNG[2], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[3], data2_4GNG[3], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[4], data2_4GNG[4], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[5], data2_4GNG[5], c='c', marker = "^", linestyle = "")
# data_4GNG[6] = data_4GNG[6] - 360
ax1.scatter(data_4GNG[6], data2_4GNG[6], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[7], data2_4GNG[7], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[8], data2_4GNG[8], c='c', marker = "^", linestyle = "")
ax1.scatter(data_4GNG[9], data2_4GNG[9], c='c', marker = "^", linestyle = "")

####################################################

# ax1.scatter(data_10[0], data2_10[0], c='y', marker = "*", linestyle = "", label = '10')
# ax1.scatter(data_10[1], data2_10[1], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10[2], data2_10[2], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10[3], data2_10[3], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10[4], data2_10[4], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10[5], data2_10[5], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10[6], data2_10[6], c='y', marker = "*", linestyle = "")
# data_10[7] = data_10[7] + 360
# ax1.scatter(data_10[7], data2_10[7], c='y', marker = "*", linestyle = "")
# data_10[8] = data_10[8] + 360
# ax1.scatter(data_10[8], data2_10[8], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10[9], data2_10[9], c='y', marker = "*", linestyle = "")

# ax1.scatter(data_10G[0], data2_10G[0], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[1], data2_10G[1], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[2], data2_10G[2], c='orange', marker = "*", linestyle = "")
# data_10G[3] = data_10G[3] + 360
# ax1.scatter(data_10G[3], data2_10G[3], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[4], data2_10G[4], c='orange', marker = "*", linestyle = "")
# data_10G[5] = data_10G[5] + 360
# ax1.scatter(data_10G[5], data2_10G[5], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[6], data2_10G[6], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[7], data2_10G[7], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[8], data2_10G[8], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10G[9], data2_10G[9], c='orange', marker = "*", linestyle = "")

# ax1.scatter(data_10N[0], data2_10N[0], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[1], data2_10N[1], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[2], data2_10N[2], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[3], data2_10N[3], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[4], data2_10N[4], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[5], data2_10N[5], c='y', marker = "*", linestyle = "")
# data_10N[6] = data_10N[6] + 360
# ax1.scatter(data_10N[6], data2_10N[6], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[7], data2_10N[7], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[8], data2_10N[8], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10N[9], data2_10N[9], c='y', marker = "*", linestyle = "")

# ax1.scatter(data_10NG[0], data2_10NG[0], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[1], data2_10NG[1], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[2], data2_10NG[2], c='y', marker = "*", linestyle = "")
# data_10NG[3] = data_10NG[3] + 360
# ax1.scatter(data_10NG[3], data2_10NG[3], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[4], data2_10NG[4], c='orange', marker = "*", linestyle = "")
# data_10NG[5] = data_10NG[5] + 360
# ax1.scatter(data_10NG[5], data2_10NG[5], c='orange', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[6], data2_10NG[6], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[7], data2_10NG[7], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[8], data2_10NG[8], c='y', marker = "*", linestyle = "")
# ax1.scatter(data_10NG[9], data2_10NG[9], c='y', marker = "*", linestyle = "")

####################################################

def label():

 for i in range(0,10,1):
          l = str(i)
          i = int(i)
          ax1.annotate("c"+l, (data_bir[i]+0.1, data2_bir[i]+0.1), size = size_label, 
                  bbox=dict(boxstyle='ellipse,pad=0.1', fc='navajowhite', ec='black'))
 for i in range(0,10,1):
          l = str(i)
          i = int(i)
          ax1.annotate("c"+l, (data_birG[i]+0.1, data2_birG[i]+0.1), size = size_label,
                  bbox=dict(boxstyle='ellipse,pad=0.1', fc='lightblue', ec='black'))
 for i in range(0,10,1):
          l = str(i)
          i = int(i)
          ax1.annotate("c"+l, (data_birN[i]+0.1, data2_birN[i]+0.1), size = size_label,
                  bbox=dict(boxstyle='ellipse,pad=0.1', fc='lightgreen', ec='black'))
 
 for i in range(0,10,1):
           l = str(i)
           i = int(i)
           ax1.annotate("c"+l, (data_birNG[i]+0.1, data2_birNG[i]+0.1), size = size_label,
                   bbox=dict(boxstyle='ellipse,pad=0.1', fc='pink', ec='black'))

#####
 
 for i in range(0,10,1):
         l = str(i)
         i = int(i)
         ax1.annotate("c"+l, (data_17L[i]+0.1, data2_17L[i]+0.1), size = size_label, 
                 bbox=dict(boxstyle='square,pad=0.1', fc='navajowhite', ec='black'))
         
 for i in range(0,10,1):
         l = str(i)
         i = int(i)
         ax1.annotate("c"+l, (data_17LG[i]+0.1, data2_17LG[i]+0.1), size = size_label, 
                 bbox=dict(boxstyle='square,pad=0.1', fc='lightblue', ec='black'))

 for i in range(0,10,1):
        l = str(i)
        i = int(i)
        ax1.annotate("c"+l, (data_17LN[i]+0.1, data2_17LN[i]+0.1), size = size_label, 
                bbox=dict(boxstyle='square,pad=0.1', fc='lightgreen', ec='black'))

 for i in range(0,10,1):
       l = str(i)
       i = int(i)
       ax1.annotate("c"+l, (data_17LNG[i]+0.1, data2_17LNG[i]+0.1), size = size_label, 
               bbox=dict(boxstyle='square,pad=0.1', fc='pink', ec='black'))

#####
 
 for i in range(0,10,1):
          l = str(i)
          i = int(i)
          ax1.annotate("c"+l, (data_4G[i]+0.1, data2_4G[i]+0.1), size = size_label, 
                  bbox=dict(boxstyle='sawtooth,pad=0.3', fc='navajowhite', ec='black'))
 
 # for i in range(0,10,1):
 #          l = str(i)
 #          i = int(i)
 #          ax1.annotate("c"+l, (data_4GG[i]+0.1, data2_4GG[i]+0.1), size = size_label, 
 #                  bbox=dict(boxstyle='sawtooth,pad=0.3', fc='lightblue', ec='black'))

 for i in range(0,10,1):
          l = str(i)
          i = int(i)
          ax1.annotate("c"+l, (data_4GN[i]+0.1, data2_4GN[i]+0.1), size = size_label, 
                  bbox=dict(boxstyle='sawtooth,pad=0.3', fc='lightgreen', ec='black'))

 for i in range(0,10,1):
        l = str(i)
        i = int(i)
        ax1.annotate("c"+l, (data_4GNG[i]+0.1, data2_4GNG[i]+0.1), size = size_label, 
                bbox=dict(boxstyle='sawtooth,pad=0.3', fc='pink', ec='black'))

#####

 # for i in range(0,10,1):
 #          l = str(i)
 #          i = int(i)
 #          ax1.annotate("c"+l, (data_10[i]+0.1, data2_10[i]+0.1), size = size_label,
 #                  bbox=dict(boxstyle='round,pad=0.3', fc='navajowhite', ec='black'))

 # for i in range(0,10,1):
 #          l = str(i)
 #          i = int(i)
 #          ax1.annotate("c"+l, (data_10G[i]+0.1, data2_10G[i]+0.1), size = size_label,
 #                  bbox=dict(boxstyle='round,pad=0.3', fc='lightblue', ec='black'))

 # for i in range(0,10,1):
 #          l = str(i)
 #          i = int(i)
 #          ax1.annotate("c"+l, (data_10N[i]+0.1, data2_10N[i]+0.1), size = size_label,
 #                  bbox=dict(boxstyle='round,pad=0.3', fc='lightgreen', ec='black'))

 # for i in range(0,10,1):
 #         l = str(i)
 #         i = int(i)
 #         ax1.annotate("c"+l, (data_10NG[i]+0.1, data2_10NG[i]+0.1), size = size_label,
 #                 bbox=dict(boxstyle='round,pad=0.3', fc='pink', ec='black'))
        
#####

 legend_elements = [Line2D([0], [0], marker = 's', lw= 0, color = 'navajowhite', label = 'cMD'),
		Line2D([0], [0], marker = 's', lw= 0, color = 'lightblue', label = 'GaMD'),
		Line2D([0], [0], marker = 's', lw= 0, color = 'lightgreen', label = 'cMD NB'),
		Line2D([0], [0], marker = 's', lw= 0, color = 'pink', label = 'GaMD NB'),
		Line2D([0], [0], marker = '$point$', lw= 0, label = 'bir', color = 'k', markersize=21),
		Line2D([0], [0], marker = '$square$', lw= 0, label = '17L', color = 'k', markersize=25),
		Line2D([0], [0], marker = '$round$', lw= 0, label = '10', color = 'k', markersize=21),
		Line2D([0], [0], marker = '$saw$', lw= 0, label = '4G', color = 'k', markersize=17)]
 
 plt.legend(handles = legend_elements)

##############

if labels:
 label()

else:
    plt.legend()

# ax1.hlines(200, 260, 450)
# ax1.hlines(297, 325, 450)

ax1.vlines(0, 40, 75)
ax1.vlines(360, 40, 75)
# ax1.vlines(194, 53.25, 85)
# ax1.vlines(150, 53.25, 85)

# ax1.set_xlim([250,300])

plt.xlabel(r'distance $\alpha$6 and $\alpha$1')
plt.ylabel(r'distance $\alpha$9 and $\alpha$6')

plt.savefig(fig, dpi=600)

plt.show()

plt.close()
