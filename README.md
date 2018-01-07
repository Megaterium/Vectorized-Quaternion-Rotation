# Vectorized-Quaternion-Rotation

Fast implementation of a vectorized function to rotate vectors using quaternions in python

The function takes as input an array of vectors that you want to rotate, an array of axis and the angles for each rotation. 

The functio will discard the real part and return the vector part of the quaternions in a numpy array. 

You need to install the [Quaternion](https://github.com/moble/quaternion) library, which is implemented in numpy so the function is really fast. 

Test:

Here we create a random numpy array of pairs of vectors (100 samples with 2 pairs each). I used this example just because it make sense for my original application, the last dimension in my vector correspond to x,y,z possitions. 
We also create a random array of rotation axis and a random array of rotation angles. 

Then we call the function v_prim = rotate_vect(angles,v_,axis)

```python
import numpy as np
import quaternion as quat

v_ = np.random.randint(0,high=100,size=[100,2,3])
axis = np.random.randint(0,high=100,size=[100,2,3])
angles = np.random.randint(-180, high=180,size=[1])
v_primes = rotate_vect(angles,v_,axis)

```
Finally we can plot some of our 3D vectors to check the results. 

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = [v_[:1,:1,0],axis[:1,:1,0],v_primes[:1,:1,0]]
ys = [v_[:1,:1,1],axis[:1,:1,1],v_primes[:1,:1,1]]
zs = [v_[:1,:1,2],axis[:1,:1,2],v_primes[:1,:1,2]]

ax.scatter(xs,ys,zs,s=[150,10,150])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

fig
```
Also you can check that the vector was rotated successfully with the following test:

```python
a = v_[:1,:1,:].reshape(3)
b = axis[:1,:1,:].reshape(3)
c = v_primes[:1,:1,:].reshape(3)

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print(np.degrees(angle),angles[0])

```

