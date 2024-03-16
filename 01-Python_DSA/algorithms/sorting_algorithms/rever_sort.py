import sys
sys.path.append('/home/samanth/Code/DSA/01-Python_DSA/algorithms')

from ArrayBaseModel import ArrayModel


from numpy import argmin

class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
        
        
        
    @staticmethod
    def reverse(array_to_reverse:list, index_low:int, index_high:int) -> list:
        '''
        Returns a array that has terms of the input array between index_low to index_high (inclusive) reversed.
        
        :param array_to_reverse: list to reverse
        :param index_low: which element to reverse from (inclusive)
        :param index_high: till element to reverse to (inclusive)
        
        Note: doesn't mutate the input array.
        
        '''
        
        changed_array = []
        for i in range(index_low):
            changed_array.append(array_to_reverse[i])
            
        for i in range( 1+ (index_high - index_low) ):
            changed_array.append(array_to_reverse[index_high - i])
            
        for i in range((len(array_to_reverse) - 1) - index_high):
            changed_array.append(array_to_reverse[ 1 + index_high + i])
            
        return changed_array
    
            
    
    def rever_sort(self):
        '''
        Revere Sort is (in my case) an time O(n^2) and a space O(n^2) algorithm to sort an array
        
        It works by iterating i over elements from START to END.
        For every i, it checks if what the smallest element is from i to END.
        Next, it calls the reverse function of that subarray from i to minValue_i. ie, it flips the terms from i to minValue_i.
        This way minValue_i is now in its correct spot. 
        Doing this for all elements, the array is sorted, with each iteration sorting, at the very least, one element to its correct spot.
        ''' 
        sortedArr = self.vals[:]
        for i in range(round(len(sortedArr)-1)):
            sortedArr = (self.reverse(sortedArr, i, i+argmin(sortedArr[i:]))).copy()            
        return sortedArr
         
            





#Testing. Uncomment/comment to see/hide examples
arr = Array([0,0,23,2,3,96,95,95,93,92,4,5,6,7,44,20,10])

print(f'Unsorted values: {arr.get_values()}\n')
arr.set_values(arr.rever_sort())
print(f"Sorted values: {arr.get_values()}")

