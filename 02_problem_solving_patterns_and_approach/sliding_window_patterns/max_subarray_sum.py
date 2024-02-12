"""
write a function which accepts an array of integers and a number called n.
the function should calculate the maximum sum of n consecutive elements
in the array.
"""
from typing import List


def max_subarray_sum_naive(arr: List, n: int) -> int:
    if n > len(arr):
        return None
    
    maximum = float("-inf")
    for i in range(len(arr) - n):
        
        temp = 0
        for j in range(n):
            temp += arr[i + j]
            
        if temp > maximum:
            maximum = temp
            
    return maximum
   
    
def max_subarray_sum_refactored(arr: List, n: int) -> int:
    if n > len(arr):
        return None
    
    max_sum = sum(arr[:n])
    temp_sum = max_sum
    
    for i in range(n, len(arr)):
        temp_sum = temp_sum - arr[i - n] + arr[i]
        max_sum = max(max_sum, temp_sum)
            
    return max_sum


if __name__ == "__main__":
    print(max_subarray_sum_naive([1, 2, 5, 2, 8, 1, 5], 2))
    print(max_subarray_sum_naive([1, 2, 5, 2, 8, 1, 5], 4))
    print(max_subarray_sum_naive([1, 2, 5, 2, 8, 1, 5], 1))
    print(max_subarray_sum_naive([], 4))
    
    print(max_subarray_sum_refactored([1, 2, 5, 2, 8, 1, 5], 2))
    print(max_subarray_sum_refactored([1, 2, 5, 2, 8, 1, 5], 4))
    print(max_subarray_sum_refactored([1, 2, 5, 2, 8, 1, 5], 1))
    print(max_subarray_sum_refactored([], 4))
    