# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# importing library
import matplotlib.pyplot as plt
import numpy as np
import math


# Matrix to plot ladder
matrix = np.matrix([[1,1,3,3,1,3,1,3,1,3,1,3,1,3,1,3],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                   [11,25,11,25,13,13,15,15,17,17,19,19,21,21,23,23]
                     ])

# splitting x and y coordinates. 
x = np.array(matrix[0])[0]
z = np.array(matrix[2])[0]

#plotting a ladder
length = len(x)
for i in range(0,length,2):
    plt.plot(x[i:i+2], z[i:i+2],'k',linewidth=5)

plt.xlim([-1, 5])
plt.ylim([9, 27])
plt.xlabel("X axis")
plt.ylabel("Z axis")
plt.title("X and Z coordinates of the ladder")
    
#plt.savefig('ladder.png')
plt.show()
plt.close()

#Converting (X,Y) matrix to homogenous coordinate (X, Y,Z, 1)

add_w = np.ones(16)
matrix_new = np.vstack([matrix,add_w])

#projection/prospective transformation
f = -5
pro = np.matrix([[1,    0,      0,      0],
                 [0,    1,      0,      0],
                 [0,    0,      0,      0],
                 [0,    0,      1/f,    1]])

matrix_pro = pro * matrix_new 

pro = matrix_pro/matrix_pro[3]

x = np.array(pro[0])[0]
y = np.array(pro[1])[0]

length = len(x)
for i in range(0,length,2):
    plt.plot(x[i:i+2], y[i:i+2],'k',linewidth=5)    

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Prospective Transformation of the ladder")
plt.show()
plt.close()

#Rotating image along z axis by 45 degree (pi/4)
ang = (math.pi)/4
sin = math.sin(ang)
cos = math.cos(ang)

Rx = np.matrix([[1,     0,      0,      0],
                [0,     cos,    -sin,   0],
                [0,     sin,    cos,    0],
                [0,     0,      0,      1]])

Ry = np.matrix([[cos, 0, sin, 0],
                [0, 1, 0, 0],
                [-sin,0, cos,0],
                [0,0,0,1]]) 

Rz = np.matrix([[cos,   sin,   0,      0],
                [-sin,   cos,    0,      0],
                [0,     0,      1,      0],
                [0,     0,      0,      1]]) 


rot = Rz*pro

x = np.array(rot[0])[0]
y = np.array(rot[1])[0]

length = len(x)
for i in range(0,length,2):
    plt.plot(x[i:i+2], y[i:i+2],'k',linewidth=5)    

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Prospective Transformation of  ladder rotated by 45 degree")
plt.show()
plt.close()

#Translate x and y by 2.

Tr = np.matrix([[1, 0,  0,  2],
                [0, 1,  0,  2],
                [0, 0,  1,  2],
                [0, 0,  0,  1]])



tra = Tr*pro

x = np.array(tra[0])[0]
y = np.array(tra[1])[0]

length = len(x)
for i in range(0,length,2):
    plt.plot(x[i:i+2], y[i:i+2],'k',linewidth=5)    

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Prospective Transformation of  ladder translated by 2")

plt.show()
plt.close()

#Reflection around y 
Re = np.matrix([[1,     0,      0,      0],
                [0,     -1,     0,      0],
                [0,     0,      1,      0],
                [0,     0,      0,      1]])

ref = Re * pro

x = np.array(ref[0])[0]
y = np.array(ref[1])[0]

length = len(x)
for i in range(0,length,2):
    plt.plot(x[i:i+2], y[i:i+2],'k',linewidth=5)    


plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Prospective Transformation of  reflected ladder")

plt.show()
plt.close()

    


