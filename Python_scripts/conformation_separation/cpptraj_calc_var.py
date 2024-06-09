#!/usr/bin/env python3

import numpy as np
import os


path_bir = '/scr2/julian/TFG/MD/birkinshaw_2017_20/analysis/'
top_bir  = 'NoMem.NoWat.bak_bir.top'
dyn_bir  = 'bak_bir_superpose_a9_dyn.nc'

path_17L = '/scr2/julian/TFG/MD/17L/analysis/'
top_17L  = 'NoMem.NoWat.bak_17L.top'
dyn_17L  = 'bak_17L_superpose_a9_dyn.nc'

path_4G = '/scr2/julian/TFG/MD/4G/analysis/'
top_4G  = 'NoMem.NoWat.bak_4G.top'
dyn_4G  = 'bak_4G_superpose_a9_dyn.nc'

path_10 = '/scr2/julian/TFG/MD/10/analysis/'
top_10  = 'NoMem.NoWat.bak_10.top'
dyn_10  = 'bak_10_superpose_a9_dyn.nc'


clusters = 'cluster.res'

#####

calc_d91 = ' distance :172-192@CA :7-36@CA out '
calc_a95 = ' dihedral :192@CA :172@CA :147@CA :107@CA range360 out '

#####

for j in range(8):
	inp_file = 'cpptraj_'
	out_file = 'bak_'
	if j == 0 or j == 1:
		inp_file = inp_file + 'bir_'
		out_file = out_file + 'bir_'
		top = path_bir + top_bir
		dyn = path_bir + dyn_bir
		clust = path_bir + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 2 or j == 3:
		inp_file = inp_file + '17L_'
		out_file = out_file + '17L_'
		top = path_17L + top_17L
		dyn = path_17L + dyn_17L
		clust = path_17L + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 4 or j == 5:
		inp_file = inp_file + '4G_'
		out_file = out_file + '4G_'
		top = path_4G + top_4G
		dyn = path_4G + dyn_4G
		clust = path_4G + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 6 or j == 7:
		inp_file = inp_file + '10_'
		out_file = out_file + '10_'
		top = path_10 + top_10
		dyn = path_10 + dyn_10
		clust = path_10 + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
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

