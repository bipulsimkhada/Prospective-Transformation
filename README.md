# Prospective Transformation
## Description
In this project, the ladder was projected using 3D coordinated X, Y, and Z were projected onto a walkway. The length of the ladder is in the Z direction, the width is in the X direction and the thickness of the ladder is in the Y direction. The 3D ladder is transformed into a perspective transformation using a Homogenous coordinate system. 3 further transformation was carried out in the perspective-transformed ladder.
1.	Rotated 45 degrees along the Z axis.
2.	 Translated by a factor of 2.
3.	Reflected around the y-axis. 

## Libraries 
* numpy
* math
* matplotlib

## Tool
* Python IDE

## Method
The ladder was created in 3D space using X, Y, and Z coordinates. Image below represents Length as Z axis and Width as X axis. 

<img src="https://github.com/bipulsimkhada/Image/blob/main/CV%20images/ladder%20x-z.png">

#### 1. Prospective Transformation
The 3D coordinates systems (X, Y, Z) were converted into homogeneous coordinates systems (X, Y, Z, 1). The projective matrix is set up below where f is equal to focal length of the lens. 

```python
# Prospective matrix
pro = np.matrix([[1,    0,      0,      0],
                 [0,    1,      0,      0],
                 [0,    0,      0,      0],
                 [0,    0,      1/f,    1]])
```

The prospective matrix is multiplied with ladder matrix to achive prospective transformation of the ladder. The visualization of the prospective transformed ladder is:

<img src="https://github.com/bipulsimkhada/Image/blob/main/CV%20images/prospective%20transformation.png">

#### 1. Rotation
The rotation matrix multiplied with prospective transformed image results in rotated 2D image. 

```python
# Anti-clockwise Rotation along X axis by angle θ
Rx = np.matrix([[1,     0,          0,         0],
                [0,     cos(θ),    sin(θ),     0],
                [0,     -sin(θ),    cos(θ),    0],
                [0,     0,          0,         1]])
                
# Anti-clockwise Rotation along Y axis by angle θ
Ry = np.matrix([[cos(θ),     0,    sin(θ),    0],
                [0,          1,     0,        0],
                [-sin(θ),    0,    cos(θ),    0],
                [0,          0,    0,         1]]) 
                
# Anti-clockwise Rotation along Z axis by angle θ
Rz = np.matrix([[cos(θ),   sin(θ),   0,      0],
                [-sin(θ),   cos(θ),    0,      0],
                [0,        0,         1,      0],
                [0,        0,         0,      1]])                 
```
In this project, rotation matrix along Z axis is multiplied with Prospective transformed ladder with rotation angle of 45 degree. 


<img src="https://github.com/bipulsimkhada/Image/blob/main/CV%20images/Rotation%20Z.png">


