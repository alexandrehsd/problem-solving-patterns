"""
Write a function called average_pair.
Given a sorted array of integers and a target average,
determine if there is a pair of values in the array where
the average of the pair equals the target average.
There may be more than one pair that matches the average target.
"""
from typing import List


def average_pair(arr: List, target: float) -> bool:
    
    if len(arr) == 0:
        return False
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        curr_avg = (arr[left] + arr[right]) / 2
        
        if curr_avg == target:
            return True
        elif curr_avg < target:
            left += 1
        else:
            right -= 1
            
    return False


if __name__ == "__main__":
    print(average_pair([1, 2, 3], 3))
    print(average_pair([1, 2, 3], 2.5))
    print(average_pair([1,3,3,5,6,7,10,12,19], 9))
    print(average_pair([-1,0,3,4,5,6], 4.1))
    print(average_pair([], 4))
    
    