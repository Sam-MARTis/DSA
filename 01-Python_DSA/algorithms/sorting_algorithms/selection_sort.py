import sys
sys.path.append('/home/samanth/Code/DSA/01-Python_DSA/algorithms')

from ArrayBaseModel import ArrayModel


class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
        
    def selection_sort(self):
        """
        Selection Sort is O(n^2) time complex and O(1) space complex
        It compares the first element with all the elements in the array and swaps the first element with the smallest element.
        Then moves on and compares the second element with all alements AFTER it and swaps. 
        Every iteration, one element is sorted.
        
        """
        arr = self.vals[:]
        for i in range(len(arr)):
            minIndex = arr.index(min(arr[i:]))
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr
          
        
arr = Array([0,0,23,2,3,96,95,95,93,92,4,5,6,7,44,20,10])

print(f'Unsorted values: {arr.get_values()}\n')
arr.set_values(arr.selection_sort())
print(f"Sorted values: {arr.get_values()}")        
