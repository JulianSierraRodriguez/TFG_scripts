from pymol import cmd

cmd.load("7ofm.pdb")
cmd.split_states("7ofm")
i = 1
for i in range(1,21):
    n = 4
    s = str(i).zfill(n)
    cmd.save("7ofm_"+s+".pdb", "7ofm_"+s)
    i=+1
cmd.delete("all")