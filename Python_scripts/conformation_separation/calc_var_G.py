#!/usr/bin/env python3

import numpy as np
import os


path_birG = '/scr2/julian/TFG/MD/bir_GaMD/MD_frags/bakbir/analysis/'
top_birG  = 'NoMem.NoWat.bakbir.top'
dyn_birG  = 'bir_GaMD_superpose_a9_dyn.nc'

path_17LG = '/scr2/julian/TFG/MD/17L_GaMD/MD_frags/bak17L/analysis/'
top_17LG  = 'NoMem.NoWat.bak17L.top'
dyn_17LG  = '17L_GaMD_superpose_a9_dyn.nc'

path_4GG = '/scr2/julian/TFG/MD/4G_GaMD/MD_frags/bak4G/analysis/'
top_4GG  = 'NoMem.NoWat.bak4G.top'
dyn_4GG  = '4G_GaMD_superpose_a9_dyn.nc'

path_10G = '/scr2/julian/TFG/MD/10_GaMD/MD_frags/bak10/analysis/'
top_10G  = 'NoMem.NoWat.bak10.top'
dyn_10G  = '10_GaMD_superpose_a9_dyn.nc'


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
		inp_file = inp_file + 'birG_'
		out_file = out_file + 'birG_'
		top = path_birG + top_birG
		dyn = path_birG + dyn_birG
		clust = path_birG + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 2 or j == 3:
		inp_file = inp_file + '17LG_'
		out_file = out_file + '17LG_'
		top = path_17LG + top_17LG
		dyn = path_17LG + dyn_17LG
		clust = path_17LG + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 4 or j == 5:
		inp_file = inp_file + '4GG_'
		out_file = out_file + '4GG_'
		top = path_4GG + top_4GG
		dyn = path_4GG + dyn_4GG
		clust = path_4GG + clusters
		frames = np.loadtxt(clust)[:,5]
		inp = ' trajin ' + dyn
		trajin = ''
		for l in range(len(frames)):
			L = int(l)
			t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
			trajin = trajin + t_in
	elif j == 6 or j == 7:
		inp_file = inp_file + '10G_'
		out_file = out_file + '10G_'
		top = path_10G + top_10G
		dyn = path_10G + dyn_10G
		clust = path_10G + clusters
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

