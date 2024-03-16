import sys
sys.path.append('/home/samanth/Code/DSA/01-Python_DSA/algorithms')

from ArrayBaseModel import ArrayModel


class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
    
    
    def insertion_sort(self):
        """
        Insertion Sort is O(n^2) time complex and O(1) space complex
        It works by iterating over the array and for every element, it checks if the previous elements are sorted.
        If not, it keeps swapping the elements until the previous elements are sorted.
        """
        vals = self.vals[:]
        for i in range(1, len(vals)):
            j = i
            
            while vals[j]<vals[j-1]:
                vals[j-1], vals[j] = vals[j], vals[j-1]
                j-=1
                if j==0:
                    break
        return vals
    








#Testing. Uncomment/comment to see/hide examples
arr = Array([0,0,23,2,3,96,95,95,93,92,4,5,6,7,44,20,10])

print(f'Unsorted values: {arr.get_values()}\n')
arr.set_values(arr.insertion_sort())
print(f"Sorted values: {arr.get_values()}")
# """