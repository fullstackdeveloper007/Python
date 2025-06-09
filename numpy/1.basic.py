import numpy as np
import sys
import time
# Numpy is a library for numerical computing in Python
# below is the basic example of numpy array
arr=np.array([1,2,3,4,])
print(arr)

#Simplar we have python list 
l=[1,2,3,4,5]
print(l) #Python list takes more memory than numpy array        

#Size comparison of python list and numpy array
python_list = list(range(100))
print(sys.getsizeof(python_list[0])*len(python_list))  # Size of the Python list in bytes

numpy_array = np.arange(100)
print(numpy_array.nbytes)  # Size of the NumPy array in bytes


# Numpy array is more efficient than python list in terms of memory and performance
#Lets you want to add  arrays values
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[x+y for x,y in zip(l1,l2)]
print(l3)  # Output: [7, 9, 11, 13, 15]

#Through numpy array we can do the same thing in more efficient way
arr1=np.array([1,2,3,4,5])  
arr2=np.array([6,7,8,9,10])
arr3=arr1+arr2
print(f"array3",arr3)  # Output: [ 7  9 11 13 15]

#Check performence of python list and numpy array
SIZE = 1000000  # Size of the array
l1=list(range(SIZE))
l2=list(range(SIZE))
start_time = time.time()
l3=[x+y for x,y in zip(l1,l2)]
end_time = time.time()
print("Time taken for python list: ", end_time - start_time)  # Time taken for python list

#Same operation with numpy array
n1=np.arange(SIZE)
n2=np.arange(SIZE)  
nStart_time = time.time()
n3=n1+n2
nEndTime = time.time()
print("Time taken for numpy array: ", nEndTime - nStart_time)  # Time taken for numpy array

 