import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import json

file1 = "bak_B3a_dist.dat"
file2 = "bak_B3a_dist2.dat"

data1 = np.loadtxt(file1)[:, 1]
data2 = np.loadtxt(file2)[:, 1]

###############################

min_data1 = min(data1)
max_data1 = max(data1)

min_data2 = min(data2)
max_data2 = max(data2)

print('Minimum of d1:', min_data1)
print('Maximum of d1:', max_data1)
print('Minimum of d2:', min_data2)
print('Maximum of d2:', max_data2)

n = 0.1
s = 1

d1 = np.arange(min_data1, max_data1+n, n)
d2 = np.arange(min_data2, max_data2+n, n)
pop = []
temp2 = []
for i in d1:
   for j in d2:
       i = round(i, s)
       j = round(j, s)
       temp = [i, j, 0]
       temp2 = pop.append(temp)

l_data = len(data1)
l_pop = print(len(pop))

###############################

m = 0

for i1 in range(l_data):
    i1=int(i1)
    temp_data1 = data1[i1]
    temp_data1 = round(temp_data1, 1)
    temp_data2 = data2[i1]
    temp_data2 = round(temp_data2, 2)
    m = m + 1
    
    for i2 in range(len(pop)):
        i2 = int(i2)
        if  pop[i2][0] == temp_data1 and pop[i2][1] == temp_data2:
            pop[i2][2] = pop[i2][2] + 1

###############################

f = open("pop_d1_d2_birNB.dat", "w")
lpop = len(pop)

for line in range(lpop):
        n = int(line)
        l = ""
        a = str(pop[n][0])
        b = str(pop[n][1])
        c = str(pop[n][2])

        l= a + " " + b + " " + c
        f.write(l + "\n")

f.close()

###############################
