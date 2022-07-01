import numpy as np

arr1 = np.array([1,2,3,4])
print(arr1)
print(arr1.shape)
print('\n-----\n')

arr2 = np.array([ [1,2,3,4] ])
print(arr2)
print(arr2.shape)
print('\n-----\n')

arr3 = np.array([ [1],[2],[3],[4] ])
print(arr3)
print(arr3.shape)
print('\n-----\n')


arr4 = np.array([ [1,2,3,4] ])
print(arr4.shape)
print(arr1+arr4)
print('-----')
print(arr2+arr4)
print('-----')
print(arr3+arr4)

arr4 = np.array([ [1,2,3,4] ])
print(arr3.shape)
print(arr4.shape)
print('-----')
print(arr3+arr4)
# set 은 - 로 교집합 뺼 수 있음.
print('-----')

arr5 = np.array([ [1,2,3], [1,2,3] ])
arr6 = np.array([ [10],[20] ])
arr6 = np.array([ [10],[20] ])
print(arr5+arr6)