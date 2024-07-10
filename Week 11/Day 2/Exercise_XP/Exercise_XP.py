import numpy as np

array = np.arange(0,10)
print(array)

array2 = [3.14, 2.17, 0, 1, 2] 
array2_np = np.array(array2).astype(int)
print (array2_np)

array3x3 = np.arange(1,10).reshape(3,3)
print (array3x3)

array4 = np.round(np.random.rand(4,5),2)
print(array4)

array5=np.arange(15,25).reshape(2,5)
print(array5[1])

array6=np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
reversed_array6=array6[::-1]
print(reversed_array6)

identity_matrix = np.eye(4)
print(identity_matrix)

array7=np.arange(20)
print(f'sum: {array7.sum()}, Average: {array7.mean()}')

array8=np.arange(1,21).reshape(4,5)
print(array8)

array9=np.arange(1,21)
array9_even=array9[array9%2!=0]
print(array9_even)
