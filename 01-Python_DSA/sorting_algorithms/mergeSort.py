from ArrayBaseModel import ArrayModel


class Array(ArrayModel):
    def __init__(self, a: list = []) -> None:
        super().__init__(a)
    
    
    def mergeSort(self):
        # pass
        Arr = self.vals[:]

        def mergeUp(leftArr: list, rightArr: list):

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
            return mergeUp(arrL, arrR)
            
        
        return sort(Arr)
    








# """Testing

a = Array([12,22,3,44,56, 16,37,28,99,])
a.setValues(a.mergeSort())
print(a.getValues())

# """