from pymol import cmd
import os


dir = os.getcwd()
contenido = os.listdir(dir)

files = []
for fichero in contenido:
        if os.path.isfile(os.path.join(dir, fichero)) and fichero.endswith('.pse'):
                files.append(fichero)

sessio = files[0]
file = sessio.split('_')
print(sessio)
n = len(file)
system_name = file[0]
NB = str(file[1])
GaMD = file[n-3]
id = file[n-2]
end = file[n-1]
prub = str(dir) + '\\' + str(sessio)

cmd.load(prub)
cmd.color("palecyan", "repr_"+id+"_mem and resi 1-195")


name = system_name


if NB == "NB":
	print("I have no BIM.")
	name = name + "_" + NB

	if GaMD == "GaMD":
		print("I am a Gaussian accelerated dynamic.")
		name = name + "_" + GaMD

	elif GaMD != "GaMD":
		print("I am a conventional dynamic.")

elif NB != "NB":
    print("I have BIM.")
    cmd.select("BIM", "repr_"+id+"_mem and resi 196-220")
    cmd.alter('(BIM)', 'chain = "B"')
    cmd.sort("repr_"+id+"_mem")
    if GaMD == "GaMD":
        print("I am a Gaussian accelerated dynamic.")
        name = name + "_" + GaMD

    elif GaMD != "GaMD":
        print("I am a conventional dynamic.")


name = name + "_" + id


cmd.ray(1400, 1400)
cmd.png(dir + '\\' + name + "_front_BS.png" )

cmd.rotate("y", 180)

cmd.ray(1400, 1400)
cmd.png(dir + '\\' + name + "_back_BS.png" )
