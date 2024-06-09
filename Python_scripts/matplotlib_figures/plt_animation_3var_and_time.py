import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.colorbar as colorbar
import matplotlib as mpl

mpl.rcParams['mathtext.default'] = 'regular'



file = "bak_B3a_dist.dat"
file2 = "bak_B3a_dist2.dat"
file3 = "bak_B3a_dist3.dat"

data = np.loadtxt(file)[:, 1]
data2 = np.loadtxt(file2)[:, 1]
data3 = np.loadtxt(file3)[:, 1]
ind =np.loadtxt(file)[:, 0]

time = []
fig, [ax, cax] = plt.subplots(1,2, gridspec_kw={"width_ratios":[50,1]})

for i in ind:
    t = i*(500/50000)
    time.append(t)

scat = ax.scatter(data, data2, c=[])
ax.set(title = "Bir_NB_GaMD", xlim=[15.5, 21], ylim = [11 , 17.5], xlabel = r'distance loop($\alpha$-4 - $\alpha$-5) and $\alpha$-2 / $\AA$', ylabel = r'distance N$\alpha$-1 and $\alpha$-2 / $\AA$')
#%%
n = 50

l = len(data)
x = slice(0, l+2, n)

time_cut = time[x]
data_cut = data[x]
data2_cut = data2[x]
data3_cut = data3[x]

def update(frame):
	global data_mean
	global data2_mean
	x = data_cut[:frame]
	y = data2_cut[:frame]
	dat = np.stack([x,y]).T
	scat.set_offsets(dat)
	scat.set_color(cmap(norm(data3_cut[:frame])))
	return(scat)

#min_tcut = min(time_cut)
#max_tcut = max(time_cut)

min_dcut = min(data3_cut)
max_dcut = max(data3_cut)

cmap = plt.cm.viridis
norm = plt.Normalize(vmin = min_dcut, vmax = max_dcut)
cb = colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, orientation='vertical')
cb.set_label(label= r"distance from the residues 1-4 to $\alpha$2")
ani = animation.FuncAnimation(fig, func=update, frames=len(time_cut), interval=1)

writer = animation.PillowWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('dist_vs_dist_vs_dist_B3a.gif', writer=writer)

plt.show()


