from array import array
import numpy as np

v = array('i',[1,4,78,29])
m1 = np.matrix([['a','b'],['c','d']])
m2 = np.array([(1,2,3),(4,5,6)])

print(v[0])
print(m1[0,1])
print(m2[1,0])

v[0] = 2019
m1[0,1] = 'F'
m2[1,1] = 2020

del v[1]

v.append(2022)

print(len(v))
print(m1.shape)
print(m2.shape)