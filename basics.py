import numpy as np

array = np.array( [[1,5,8] ,[5,2,7]])
array1 = np.array([[4,8,2,7],[5,8,93,5],[8,8,1,7]])
print (array,"   ",array.ndim)
print(array1 , "    ",array.ndim)
print(array.shape,"  ",array.size)

#array creatd using list
arr= np.array([4,5,2])
print (arr)

#array created using tuple
ar = np.array ((1,8,2,5))
print (ar)

#*************numpy functions to create array
c=np.zeros((5,8))
print(c)

full= np.full((2,4),4,dtype='float')
print(full)

random=np.random.random((4,2))
print(random)

ones=np.ones((4,3))
print(ones)

#empty=np.empty((3,6))
#print(empty)

#**************reshaping of an array
array3=np.array([[1,5,7,5],[5,8,6,7],[8,6,9,12]])
newarray=array3.reshape(12,1)
print(newarray)
flatten_array=array3.flatten()
print(flatten_array)  ####flattens the array

#**********unary operators
print("manimum element in the array ",array3.min())
print("maximum element in the array ",array3.max())
print("maximum rowwise element in the array ",array3.max(axis=1))
print("maximum cloumnwise element in the array ",array3.max(axis=0))
print("sum of all the element in the array ",array3.sum())
print("The transpose of array",'\n',array3.T)

#*********binary opretions
mat1=np.array([[4,5,8,6],[7,9,6,1]])
mat2=np.array([[2,5],[8,7],[4,8],[56,9]])
print("matrix multiplication", '\n',mat1.dot(mat2))

#*********slicing an array
a=np.array([[12,5,87,6],
           [45,36,2,5],
           [65,89,27,3],
           [47,9,36,55]])
sliced_arr=a[2:3,2::3]
print("sliced array",'\n',sliced_arr)

#**********index in an array
index_array=a[[2,1,3,0],[3,2,1,0]]
print(index_array)
####**********creating numpy array using fromiter
iterable =(a**a for a in range (1,10))
array_fromiter=np.fromiter(iterable,int)
print("Fromiter array",array_fromiter)

#**********creating empty array
array_empty=np.empty([4,5],dtype=float,order='c')
print(array_empty)