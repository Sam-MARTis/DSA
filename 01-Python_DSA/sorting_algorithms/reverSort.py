from numpy import argmin
from ArrayBaseModel import ArrayModel
import logging


class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
    
    @staticmethod
    def reverse(a: list, index_low:int, index_high:int) -> list:
        if index_high >= len(a)  or  index_low <0: 
            logging.warning(IndexError(" Index out of bounds. Careful..."))
            
        return a[0: index_low] + a[index_high-1 : index_low-1: -1] + a[index_high:]
        
    def reverSort(self):
        # pass
        Arr = self.vals[:]
        for i in range(len(Arr)):
            self.reverse(Arr, i, argmin(Arr[i+1 :]))
            
            






arr = [0,1,2,3,4,5,6,7,8,9,10]
# """Testing
print(reverse(a=arr, index_low=3, index_high=15))

# """