
import sys
sys.path.append('01-Python_DSA/algorithms')

from ArrayBaseModel import ArrayModel

class Array(ArrayModel):
    def __init__(self, a: list = ...) -> None:
        super().__init__(a)
    def binary_search(self, key: int) -> int:
        lb = 0
        ub = len(self.vals) - 1
        while lb <= ub:
            m = (lb + ub) // 2
            if self.vals[m] == key:
                return m
            elif self.vals[m] > key:
                ub = m - 1
            else:
                lb = m + 1
        return -1

arr = Array([0,4 ,9, 12, 14, 15, 23, 37, 40, 50, 69])

print(f"Index of 5 is: {arr.binary_search(5)}")
print(f"Index of 15 is: {arr.binary_search(15)}")
# """