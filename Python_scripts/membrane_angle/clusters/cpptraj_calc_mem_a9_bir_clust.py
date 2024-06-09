#!/usr/bin/env python3

import numpy as np
import os

path_prot = '/scr2/julian/TFG/analysis/PDB_repr/bir' #path repr cMD con BIM, no poner / al final

path_bir = '/scr2/julian/TFG/MD/birkinshaw_2017_20/analysis/'
top_bir  = 'NoWat.bak_bir.top'

path_birG = '/scr2/julian/TFG/MD/bir_GaMD/MD_frags/bakbir/analysis/'
top_birG  = 'NoWat.bakbir.top'

path_birN = '/scr2/julian/TFG/MD/bir_NB/analysis/'
top_birN  = 'NoWat.pur_bir.top'

path_birNG = '/scr2/julian/TFG/MD/bir_NB_GaMD/MD_frags/birNB/analysis/'
top_birNG  = 'NoWat.birNB.top'

end_dyn_bir  = '_NoWat_RMSD_dyn.nc'

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
print(n_molec)
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
		inp_file = inp_file + 'bir'
		out_file = out_file + 'bir'
		path = path_bir
		top = path + top_bir
		contenido = os.listdir(path_bir)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_bir):
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
		inp_file = inp_file + 'birG'
		out_file = out_file + 'birG'
		path = path_birG
		top = path + top_birG
		contenido = os.listdir(path_birG)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_bir):
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
		inp_file = inp_file + 'birN'
		out_file = out_file + 'birN'
		path = path_birN
		top = path + top_birN
		contenido = os.listdir(path_birN)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_bir):
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
		inp_file = inp_file + 'birNG'
		out_file = out_file + 'birNG'
		path = path_birNG
		top = path + top_birNG
		contenido = os.listdir(path_birNG)
		files = []
		for fichero in contenido:
			if fichero.endswith(end_dyn_bir):
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

