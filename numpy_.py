import numpy as np

mylist = [1, 2, 3]

x = np.array(mylist)
y = np.array([4, 5, 6])
m = np.array([[7, 8, 9], [10, 11, 12]])

n = np.arange(0, 30, 2) #similar to Matlab 0:2:28
n = n.reshape(3,5) #convert to 3x5 array
print(n)

o = np.linspace(0, 4, 9) #from 0 to 4: 9 values
o.resize(3,3) #resize changes array's shape; reshape only outputs temp array reshape
print(o)

a = np.array([1, 2, 3] * 3) #appends next array(s)
b = np.repeat([1, 2, 3], 3) #repeats every element
c = np.vstack([a,b]) #hstack can be used to append horizontically
print(c)

z = np.array([y, y**2])
z = z.T #transpose
z = z.astype('f') #z.dtype will return float32 instead of int64
#operations posible on an array: sum(), max(), min(), mean(), std(); indexes: argmax(), argmin()
