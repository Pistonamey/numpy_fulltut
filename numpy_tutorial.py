import numpy as np

#a=[1,2,3,4,5]
#print(a[1])
#print(a[1:4])

a=np.array([1,2,3,4,5])
print(a)
print(a[1])
print(a[1:])
print(a[:-2])

a[2]=10

print(a)

a_mul=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a_mul)
print(a_mul[0,1])
print(a_mul.shape)

a_mul=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,5],[7,5,5],[9,2,9]]])
print(a_mul.shape)
print(a_mul.ndim)
print(a_mul.size)
print(a_mul.dtype)


print("-----Filling------")
a=np.full((2,3,4),9)
print(a)

a=np.zeros((10,5,2))
#print(a)
a=np.empty((5,5,5))
#print(a)

x_values=np.arange(0,1005,5)
print(x_values)

x_values=np.linspace(0,1000,2)
print(x_values)

print("------NaN and INF----")
print(np.nan)
print(np.inf)

print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.inf))

print("----- Mathematical operations ------")

l1=[1,2,3,4,5]
l2=[6,7,8,9,0]

a1=np.array(l1)
a2=np.array(l2)

print(a1*5)

#vector addition
print(a1+5)

print(a1/2)

print(np.log10(a1))

print("-----Array Functions ----")

a = np.array([1,2,3])
a=np.append(a,[2,3,6])
print(a)

a=np.insert(a,4, [4,5,6])
print(a)

a=np.array([[1,2,3],[4,5,6]])
print(np.delete(a,1))
print(np.delete(a,1,0))

print("-----Structuring ----")
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])

print(a.shape)
print(a.reshape((5,4)))

#return a copy
print(a.flatten())

#return a view
print(a.ravel())

a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(a.T)
print(a.swapaxes(0,1))

print("----- Concatenating, Splitting, Stacking----")
a1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
a2=np.array([[11,12,13,14,15],[16,17,18,19,20]])

a=np.concatenate((a1,a2),axis=0)
print(a)
a=np.concatenate((a1,a2), axis=1)
print(a)

a=np.stack((a1,a2))
print(a)

a=np.vstack((a1,a2))
print(a)


print("-------- statistics----")
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(np.split(a,2, axis=0))
#print(np.split(a,3,axis=1))
print(a.min())
print(a.max())
print(a.mean())
print(a.std())
print(a.sum())
print(np.median(a))


print("----random=-------")
number=np.random.randint(100)
print(number)

a=np.random.randint(90,100,size=(2,3,4))
print(a)

a=np.random.binomial(10,p=0.5,size=(5,10))
print(a)

print("----- Export and Import ----- ")
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
np.save("muarray.txt", a)
np.savetxt("arrrr.csv",a,delimiter=",")
a=np.loadtxt("arrrr.csv", delimiter=",")
print(a)
