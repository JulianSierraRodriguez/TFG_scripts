from pymol import cmd

id = "c0"
system_name = "17L"
BIM = True 
GaMD = False

name = system_name

cmd.load("repr_"+id+"_mem.pdb")
cmd.load("fftmap."+id+".pdb")

cmd.align("repr_"+id+"_mem", "protein")
cmd.delete("protein")

cmd.zoom("repr_"+id+"_mem")

cmd.color("yellow", "(name C*) and repr_"+id+"_mem")
cmd.color("palecyan", "repr_"+id+"_mem and resi 1-195")

if BIM:
	cmd.color("gray20", "repr_"+id+"_mem and resi 196-220")
	if GaMD:
		name = name + "_GaMD"
elif BIM == False:
	name = name + "_NB"
	if GaMD:
		name = name + "_GaMD"

name = name + "_" + id +  "_BS.pse"

cmd.color("orange", "resi 73-83")
cmd.color("orange", "resi 90-102")
cmd.color("orange", "resi 108-127")

cmd.color("Salmon", "repr_"+id+"_mem and resi 26-46")
cmd.color("Salmon", "repr_"+id+"_mem and resi 67-78")
cmd.color("Salmon", "repr_"+id+"_mem and resi 121-128")


cmd.color("Marine", "repr_"+id+"_mem and resi 83-91")
cmd.color("Marine", "repr_"+id+"_mem and resi 122-141")


cmd.color("Green", "repr_"+id+"_mem and resi 21")
cmd.color("Green", "repr_"+id+"_mem and resi 24")
cmd.color("Green", "repr_"+id+"_mem and resi 28")
cmd.color("Green", "repr_"+id+"_mem and resi 48-64")


cmd.color("Red", "repr_"+id+"_mem and resi 99-107")
cmd.color("Red", "repr_"+id+"_mem and resi 145-155")

cmd.save(name)
	

