import sys
sys.path.append('/home/samanth/Code/DSA/01-Python_DSA/algorithms')

from ArrayBaseModel import ArrayModel

class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
    
    
    def merge_sort(self):
        '''
        Merge Sort is (in my case) an time O(nlogn) and a space O(nlogn) algorithm to sort an array
        
        It works by dividing the array into subarrays(by splitting the middle) recursively until each element is in a subarray of length 1.
        Then, it combines the subarrays recursively in pairs so that when combining the combined subarray is sorted.
        Since there will be logn (base2) ± 1 and the total length of elements to be iterated over is at n, resultant complexity is nlogn
        '''
        # pass
        Arr = self.vals[:]

        def merge_up(leftArr: list, rightArr: list):

            i = 0
            k = 0
            upArr=[]
            
            for _ in range(len(leftArr)+len(rightArr)+1):
                if(leftArr[i] <= rightArr[k]):
                    upArr.append(leftArr[i])
                    i+=1
                    if i>=len(leftArr): 
                        for v in rightArr[k:]:
                            upArr.append(v)

                        break
                    pass
                else:
                    upArr.append(rightArr[k])
                    
                    k+=1
                    if k>=len(rightArr): 
                        for v in leftArr[i:]:
                            upArr.append(v)
                        break
                    pass
            
            
            return upArr
            
        def sort(Arr):
            arrL = Arr[:len(Arr)//2]
            arrR = Arr[len(Arr)//2:]
            if len(arrL)!=1 and len(arrR)!=1:
                arrL = sort(arrL)
                arrR = sort(arrR)
            return merge_up(arrL, arrR)
            
        
        return sort(Arr)
    








#Testing. Uncomment/comment to see/hide examples
arr = Array([0,0,23,2,3,96,95,95,93,92,4,5,6,7,44,20,10])

print(f'Unsorted values: {arr.get_values()}\n')
arr.set_values(arr.merge_sort())
print(f"Sorted values: {arr.get_values()}")
# """