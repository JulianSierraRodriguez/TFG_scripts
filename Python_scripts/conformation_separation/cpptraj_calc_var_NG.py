#!/usr/bin/env python3

import numpy as np
import os


path_birNG = '/scr2/julian/TFG/MD/bir_NB_GaMD/MD_frags/birNB/analysis/'
top_birNG  = 'NoMem.NoWat.birNB.top'
dyn_birNG  = 'birNB_GaMD_superpose_a9_dyn.nc'

path_17LNG = '/scr2/julian/TFG/MD/17L_NB_GaMD/MD_frags/NB17L/analysis/'
top_17LNG  = 'NoMem.NoWat.NB17L.top'
dyn_17LNG  = 'NB17L_GaMD_superpose_a9_dyn.nc'

path_4GNG = '/scr2/julian/TFG/MD/4G_NB_GaMD/MD_frags/4GNB/analysis/'
top_4GNG  = 'NoMem.NoWat.4GNB.top'
dyn_4GNG  = '4GNB_GaMD_superpose_a9_dyn.nc'

path_10NG = '/scr2/julian/TFG/MD/10_NB_GaMD/MD_frags/NB10/analysis/'
top_10NG  = 'NoMem.NoWat.NB10.top'
dyn_10NG  = 'NB10_GaMD_superpose_a9_dyn.nc'


clusters = 'cluster.res'

#####

calc_d91 = ' distance :172-192@CA :7-36@CA out '
calc_a95 = ' dihedral :192@CA :172@CA :147@CA :107@CA range360 out '

#####

for j in range(8):
	inp_file = 'cpptraj_'
	out_file = 'bak_'
	if j == 0 or j == 1:
		inp_file = inp_file + 'birNG_'
		out_file = out_file + 'birNG_'
		top = path_birNG + top_birNG
		dyn = path_birNG + dyn_birNG
		clust = path_birNG + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 2 or j == 3:
		inp_file = inp_file + '17LNG_'
		out_file = out_file + '17LNG_'
		top = path_17LNG + top_17LNG
		dyn = path_17LNG + dyn_17LNG
		clust = path_17LNG + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 4 or j == 5:
		inp_file = inp_file + '4GNG_'
		out_file = out_file + '4GNG_'
		top = path_4GNG + top_4GNG
		dyn = path_4GNG + dyn_4GNG
		clust = path_4GNG + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 6 or j == 7:
		inp_file = inp_file + '10NG_'
		out_file = out_file + '10NG_'
		top = path_10NG + top_10NG
		dyn = path_10NG + dyn_10NG
		clust = path_10NG + clusters
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
