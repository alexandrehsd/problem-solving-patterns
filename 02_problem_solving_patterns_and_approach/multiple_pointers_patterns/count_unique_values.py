"""
implement a function called count_unique which accepts a sorted array, and counts
the unique values in the array. there can be negative numbers in the array,
but it will always be sorted.
"""
from typing import List


def count_unique_naive(arr: List) -> int:
    if len(arr) == 0:
        return 0
    
    unique = 0
    i = 0
    
    while i < len(arr):
        current_value = arr[i]
        unique += 1
        
        j = i+1
        
        if j == len(arr):
            break
        
        next_value = arr[j]
        while current_value == next_value:
            j += 1
            
            if j == len(arr):
                break
            
            next_value = arr[j]
            
        i = j
        
    return unique


def count_unique_refactored(arr: List) -> List:
    if len(arr) == 0:
        return 0
    
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1
    

if __name__ == "__main__":
    print(count_unique_naive([1, 1, 1, 1, 2]))
    print(count_unique_naive([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 14]))
    print(count_unique_naive([]))
    
    print(count_unique_refactored([1, 1, 1, 1, 2]))
    print(count_unique_refactored([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 14]))    
    print(count_unique_refactored([]))
    