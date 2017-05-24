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

#operations x+y, x*y etc on arrays are per elements
z = np.array([y, y**2])
z = z.T #transpose
z = z.astype('f') #z.dtype will return float32 instead of int64
#operations posible on an array: sum(), max(), min(), mean(), std(); indexes: argmax(), argmin()

s = np.arange(13)**2 #from 0 to 12^2
print(s[0], s[4], s[0:3])
print(s[1:5])
print(s[-4:]) #last 4 elements
print(s[-5::-2]) #counting back with step 2

r = np.arange(36) #from 0 to 35
r.resize(6,6)
print(r[3,3:6]) #3rd row columns 3-6
print(r[:4:2, :-1]) #every second row up to 4th (0, 2), all columns except for the last
print(r[-1, ::2]) #every second element from the last row

r[r>30] = 30 #assign 30 to all elements >30 in r
itemindex = np.where(r>30) #returns indexes of elements >30
r2 = r[:3,:3]
r2[:] = 0 #this assignment also changes elements in array r!
r_copy = r.copy() #makes copy of the array; changes in copy -> no changes in original one

test = np.random.randint(0, 10, (4,3))
for row in test:
	print(row)

for i in range(len(test)):
	print(i)

for i, row in enumerate(test):
	print('row', i, 'is', row)

test2 = test**2

for i, j in zip(test, test2):
	print(i,'+', j, '=', i+j)
