from pymol import cmd

i = 1
n = 4
cmd.load("5vwv_clean.pdb")
cmd.select("L_5vwv_clean", "all and resi 183")
cmd.select("G_5vwv_clean", "all and resi 186")
cmd.color("salmon", "5vwv_clean")
cmd.color("red", "ss h and 5vwv_clean")
cmd.color("Gray20", "ss h and 5vwv_clean and chain B")

for i in range (1,21):
    s = str(i).zfill(n)
    cmd.load("7ofm_"+s+".pdb")
    cmd.color("palecyan", "7ofm_"+s)
    cmd.color("cyan", "ss h and 7ofm_"+s)
    cmd.alter("7ofm_"+s, "resi=str(int(resi)+181)")
    cmd.select("L_7ofm_"+s, "7ofm_"+s+" and resi 183")
    cmd.select("G_7ofm_"+s, "7ofm_"+s+" and resi 186")
    cmd.align("L_5vwv_clean", "L_7ofm_"+s)
    cmd.zoom("all")
    cmd.ray(1400, 1400)
    cmd.png("image_bak_poss_L_"+s+".png", 0, 0, dpi = 600)
    cmd.save("bak_poss_L_"+s+".cif", "all")
    cmd.align("G_5vwv_clean", "G_7ofm_"+s)
    cmd.zoom("all")
    cmd.ray(1400,1400)
    cmd.png("image_bak_poss_G_"+s+".png", 0, 0, dpi = 600)
    cmd.save("bak_poss_G_"+s+".cif", "all")
    cmd.delete("7ofm_"+s)
    cmd.delete("L_7ofm_"+s)
    cmd.delete("G_7ofm_"+s)
    