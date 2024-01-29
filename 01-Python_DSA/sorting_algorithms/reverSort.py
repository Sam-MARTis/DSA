from numpy import argmin
from ArrayBaseModel import ArrayModel
# import logging


class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
     
    # @staticmethod
    # def reverse(a, index_low:int, index_high:int) -> list:
    #     if index_high >= len(a)  or  index_low <0: 
    #         logging.warning(IndexError(" Index out of bounds. Careful..."))
    #     print(f"a[:index_low]: {a[:index_low+1]}")
    #     print(f"a[index_high-1 : index_low: -1]: {a[index_high-1 : index_low: -1]}")
    #     print(f" a[index_high:]: { a[index_high:]}")
    #     return [a[0]*(index_low==0)] + a[:index_low+1] + a[index_high-1 : index_low: -1] + a[index_high:]
    @staticmethod
    def reverse(a:list, index_low:int, index_high:int) -> list:
        arr = []
        for i in range(index_low):
            arr.append(a[i])
        for i in range( 1+ index_high-index_low):
            arr.append(a[index_high-i])
        for i in range((len(a)-1)-index_high):
            arr.append(a[1+index_high +i])
        return arr
    
            
    
    def reverSort(self):
        # pass
        
        for i in range(round(len(self.vals)-1)):
            self.setValues(self.reverse(self.vals, i, i+argmin(self.vals[i:])))
            
            # print(f"self.vals: {self.vals} \ni = {i}\nArr[i:]: {self.vals[i :]}\ni+argmin(Arr[i:]): {i+argmin(self.vals[i :])}\nreversed values: {self.}\n\n\n")
    
            # self.setValues(k)
            # Arr = k.copy()
            
        return self.getValues()
            






arr = Array([0,23,2,3,96,95, 95,93,92,4,5,6,7,44,20,10])
# """Testing
# arrmine = [0, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(arr.reverse(arrmine, index_low=1, index_high=10))
# should give [0,11,2,3,7,6,5,4,8,9,10] for 4, 7
print(arr.reverSort())

# """