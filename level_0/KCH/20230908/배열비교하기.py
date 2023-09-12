# 예상 시간복잡도: O(N)
from functools import total_ordering

@total_ordering
class ARR:
    def __init__(self, arr):
        self.arr = arr
    
    def __eq__(self, other):
        return len(self.arr) == len(other.arr) and sum(self.arr) == sum(other.arr)

    def __le__(self, other):
        return len(self.arr) < len(other.arr) or (len(self.arr)==len(other.arr) and sum(self.arr) < sum(other.arr))
    
    def __gt__(self, other):
        return len(self.arr) > len(other.arr) or (len(self.arr)==len(other.arr) and sum(self.arr) > sum(other.arr))

def solution(arr1, arr2):
    arr1 = ARR(arr1)
    arr2 = ARR(arr2)
    return -1 if arr1 < arr2 else( 1 if arr1 > arr2 else 0 )

# cf) 훨 간단..... O(N)
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
