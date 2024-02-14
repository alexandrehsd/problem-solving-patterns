"""
Write a function called min_subarray which accepts two parameters
- an array of positive integers and a positive integer.
This function should return the minimal length of a contiguous subarray
of which the sum is greater than or equal to the integer passed to the
function. If there isn't one, return 0 instead.
"""
from typing import List


def min_subarray(arr: List[int], n: int) -> List[int]:
    
    if (n < 0):
        return 0
    
    if (len(arr) == 0):
        return 0
    
    min_length = float("inf")
    i, j = 0, 0
    
    current_sum = 0
    
    while j < len(arr):
        current_sum += arr[j]
        
        if current_sum == n:
            min_length = min(min_length, j - i + 1)
        elif current_sum > n:
            while (current_sum >= n) and i <= j:
                min_length = min(min_length, j - i + 1)
                current_sum -= arr[i]
                i += 1
        j += 1

    if current_sum >= n:
        min_length = min(min_length, j - i + 1)
    
    if min_length == float("inf"):
        return 0
    
    return min_length


if __name__ == "__main__":
    
    print(min_subarray([2,3,1,2,4,3], 7)) # 2 -> because [4,3] is the smallest subarray
    print(min_subarray([2,1,6,5,4], 9)) # 2 -> because [5,4] is the smallest subarray
    print(min_subarray([3,1,7,11,2,9,8,21,62,33,19], 52)) # 1 -> because [62] is greater than 52
    print(min_subarray([1,4,16,22,5,7,8,9,10],39)) # 3
    print(min_subarray([1,4,16,22,5,7,8,9,10],55)) # 5
    print(min_subarray([4, 3, 3, 8, 1, 2, 3], 11)) # 2
    print(min_subarray([1,4,16,22,5,7,8,9,10],95)) # 0
    