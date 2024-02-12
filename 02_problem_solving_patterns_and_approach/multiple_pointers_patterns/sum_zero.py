"""
write a function called sum_zero which accepts a sorted array
of integers. the function should find the first pair where
the sum is 0. Return an array that includes both values that
sum to zero or undefined if a pair does not exist.
"""
from typing import List


def sum_zero(arr: List) -> List:
    left = 0
    right = len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == 0:
            return [arr[left], arr[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1
    
    return []


if __name__ == "__main__":
    print(sum_zero([-4, -3, -1, 0, 1, 2, 5]))
    print(sum_zero([-4, -3, -1, 0]))
    print(sum_zero([-4, -3, -1, 0, 2, 5]))
    