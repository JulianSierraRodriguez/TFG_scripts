#!/usr/bin/env python3

import numpy as np
import os

path_prot = '/scr2/julian/TFG/analysis/PDB_repr/4G' #path repr cMD con BIM, no poner / al final

path_4G = '/scr2/julian/TFG/MD/4G/analysis/'
top_4G  = 'NoWat.bak_4G.top'

path_4GG = '/scr2/julian/TFG/MD/4G_GaMD/MD_frags/bak4G/analysis/'
top_4GG  = 'NoWat.bak4G.top'

path_4GN = '/scr2/julian/TFG/MD/4G_NB/analysis/'
top_4GN  = 'NoWat.NB_4G.top'

path_4GNG = '/scr2/julian/TFG/MD/4G_NB_GaMD/MD_frags/4GNB/analysis/'
top_4GNG  = 'NoWat.4GNB.top'

end_dyn_4G  = '_NoWat_RMSD_dyn.nc'

clusters = 'cluster.res'

#####

def n_molec_PDB(path):
	n_molec = []
	cont = sorted(os.listdir(path))
	for fitx in cont:
		if fitx.endswith('.pdb'):
			fitx = path + fitx
			lines = len(open(fitx, 'r').readlines())
			molec = np.genfromtxt(fitx, skip_header = lines-2, skip_footer = 1, usecols = 3)
			molec = int(molec.item())
			n_molec.append(molec)
	n = n_molec[0]
	for i in range(len(n_molec)):
		I = int(i)
		if n_molec[I] != n:
			print('Error en el PDB del repr: c'+str(n))
	n = str(n)
	return n

###

def frame_to_dyn(path, frames):
	trajin = ''
	for l in range(len(frames)):
		L = int(l)
		if 0 < frames[L] < 10000:
			dyn = dyn1
		elif 10000 < frames[L] < 30000:
			dyn = dyn2
			frames[L] = frames[L] - 10000
		elif 30000 < frames[L] < 50000:
			dyn = dyn3
			frames[L] = frames[L] - 30000
		dyn = path + dyn
		inp = ' trajin ' + dyn
		t_in = inp + ' ' + str(int(frames[L])) + ' ' + str(int(frames[L])) + ' 1' + '\n'
		trajin = trajin + t_in
	return trajin

#####

path = path_prot + '/'
n_molec = n_molec_PDB(path)

calc1 = ' principal :221-'+n_molec +' dorotation mass \n' 
calc1 = calc1 + ' vector Mem principal x \n'
calc1 = calc1 + ' vector a9 :172@CA :192@CA \n'
calc1 = calc1 + ' vectormath vec1 Mem vec2 a9 dotangle out '


path_N = path_prot + 'N/'
n_molec_N = n_molec_PDB(path_N)

calc2 = ' principal :196-'+ n_molec_N +' dorotation mass \n' 
calc2 = calc2 + ' vector Mem principal x \n'
calc2 = calc2 + ' vector a9 :172@CA :192@CA \n'
calc2 = calc2 + ' vectormath vec1 Mem vec2 a9 dotangle out '

#####

for j in range(4):
	inp_file = 'cpptraj_'
	out_file = 'bak_'
	if j == 0:
		inp_file = inp_file + '4G'
		out_file = out_file + '4G'
		path = path_4G
		top = path + top_4G
		contenido = os.listdir(path_4G)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_4G):
				files.append(fichero)
		dyn1 = files[2]
		dyn2 = files[0]
		dyn3 = files[1]
		clust = path + clusters
		frames = np.loadtxt(clust)[:,5]
		trajin = ''
		trajin = frame_to_dyn(path, frames)
		calc = calc1
	if j == 1:
		inp_file = inp_file + '4GG'
		out_file = out_file + '4GG'
		path = path_4GG
		top = path + top_4GG
		contenido = os.listdir(path_4GG)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_4G):
				files.append(fichero)
		dyn1 = files[2]
		dyn2 = files[0]
		dyn3 = files[1]
		clust = path + clusters
		frames = np.loadtxt(clust)[:,5]
		trajin = ''
		trajin = frame_to_dyn(path, frames)
		calc = calc1
	if j == 2:
		inp_file = inp_file + '4GN'
		out_file = out_file + '4GN'
		path = path_4GN
		top = path + top_4GN
		contenido = os.listdir(path_4GN)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_4G):
				files.append(fichero)
		dyn1 = files[2]
		dyn2 = files[0]
		dyn3 = files[1]
		clust = path + clusters
		frames = np.loadtxt(clust)[:,5]
		trajin = ''
		trajin = frame_to_dyn(path, frames)
		calc = calc2
	elif j == 3:
		inp_file = inp_file + '4GNG'
		out_file = out_file + '4GNG'
		path = path_4GNG
		top = path + top_4GNG
		contenido = os.listdir(path_4GNG)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_4G):
				files.append(fichero)
		dyn1 = files[2]
		dyn2 = files[0]
		dyn3 = files[1]
		clust = path + clusters
		frames = np.loadtxt(clust)[:,5]
		trajin = ''
		trajin = frame_to_dyn(path, frames)
		calc = calc2



	inp_files = 'en_' + inp_file + '_sbatch'
	out_file = out_file + '_a_mem_a9.dat'
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
	trajin = ' trajin '+path+dyn1+ '\n' + ' trajin '+path+dyn2+ '\n' + ' trajin '+path+dyn3+ '\n'
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

