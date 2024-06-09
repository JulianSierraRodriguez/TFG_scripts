#!/usr/bin/env python3

import numpy as np
import os


path_birN = '/scr2/julian/TFG/MD/bir_NB/analysis/'
top_birN  = 'NoMem.NoWat.pur_bir.top'
dyn_birN  = 'birNB_superpose_a9_dyn.nc'

path_17LN = '/scr2/julian/TFG/MD/17L_NB/analysis/'
top_17LN  = 'NoMem.NoWat.bak17L.top'
dyn_17LN  = '17LNB_superpose_a9_dyn.nc'

path_4GN = '/scr2/julian/TFG/MD/4G_NB/analysis/'
top_4GN  = 'NoMem.NoWat.NB_4G.top'
dyn_4GN  = '4GNB_superpose_a9_dyn.nc'

path_10N = '/scr2/julian/TFG/MD/10_NB/analysis/'
top_10N  = 'NoMem.NoWat.NB_10.top'
dyn_10N  = '10NB_superpose_a9_dyn.nc'


clusters = 'cluster.res'

#####

calc_d91 = ' distance :172-192@CA :7-36@CA out '
calc_a95 = ' dihedral :192@CA :172@CA :147@CA :107@CA range360 out '

#####

#for i in range(2):
#	inp_file = 'cpptraj_'
#	out_file = 'bak_'
#	if i == 0:
#		inp_file = inp_file + 'd91_'
#		out_file = out_file + 'd91_'
#		calc = calc_d91
for j in range(8):
	inp_file = 'cpptraj_'
	out_file = 'bak_'
	if j == 0 or j == 1:
		inp_file = inp_file + 'birN_'
		out_file = out_file + 'birN_'
		top = path_birN + top_birN
		dyn = path_birN + dyn_birN
		clust = path_birN + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 2 or j == 3:
		inp_file = inp_file + '17LN_'
		out_file = out_file + '17LN_'
		top = path_17LN + top_17LN
		dyn = path_17LN + dyn_17LN
		clust = path_17LN + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 4 or j == 5:
		inp_file = inp_file + '4GN_'
		out_file = out_file + '4GN_'
		top = path_4GN + top_4GN
		dyn = path_4GN + dyn_4GN
		clust = path_4GN + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 6 or j == 7:
		inp_file = inp_file + '10N_'
		out_file = out_file + '10N_'
		top = path_10N + top_10N
		dyn = path_10N + dyn_10N
		clust = path_10N + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in


	if j == 0 or j == 2 or j == 4 or j == 6 :
		inp_file = inp_file + 'd91'
		out_file = out_file + 'd91'
		calc = calc_d91
	if j == 1 or j == 3 or j == 5 or j == 7 :
		inp_file = inp_file + 'a95'
		out_file = out_file + 'a95'
		calc = calc_a95

	inp_files = 'en_' + inp_file + '_sbatch'
	out_file = out_file + '.dat'
	file_cpptraj = open(inp_files, 'w')
	line = '#! /bin/csh' + '\n'
	file_cpptraj.write(line)
	line = '\n'
	file_cpptraj.write(line)
	line = '#SBATCH -J ' + inp_file + '\n' + '#SBATCH -n 1' + '\n' + '#SBATCH --ntasks-per-node=1' + '\n' + '#SBATCH --time=6-0' + '\n' + '\n'
	file_cpptraj.write(line)
	line = '#' + '\n'  + '###########################################################' + '\n' + '#' + '\n' + '\n'
	file_cpptraj.write(line)
	line = ' /home/prog/amber22/bin/cpptraj ' + top + ' > ' + inp_file + '.out << EOF' + '\n'
	file_cpptraj.write(line)
	line = '\n'
	file_cpptraj.write(line)
	file_cpptraj.write(trajin)
	line = '\n'
	file_cpptraj.write(line)
	calc = calc + out_file
	file_cpptraj.write(calc)
	line = '\n'
	file_cpptraj.write(line)
	line = ' go' + '\n' + 'EOF'
	file_cpptraj.write(line)
	file_cpptraj.close()
	run_cpptraj = 'sbatch ' + inp_files
	os.system(run_cpptraj)
	print(inp_file)

