import sys
sys.path.append('01-Python_DSA/algorithms')

from numpy import argmin
from ArrayBaseModel import ArrayModel


class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
        
    def selection_sort(self):
        arr = self.vals[:]
        for i in range(len(arr)):
            minIndex = arr.index(min(arr[i:]))
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr
          
        
arr = Array([0,0,23,2,3,96,95,95,93,92,4,5,6,7,44,20,10])

print(f'Unsorted values: {arr.get_values()}\n')
arr.set_values(arr.selection_sort())
print(f"Sorted values: {arr.get_values()}")        
