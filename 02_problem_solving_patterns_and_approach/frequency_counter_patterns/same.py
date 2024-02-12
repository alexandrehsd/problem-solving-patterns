"""
the function should return true if every value in the array
has its corresponding value squared in the second array,
the frequency of values must be the same.
"""
from typing import List


def same_naive(arr1: List, arr2: List) -> bool:
    
    if len(arr1) != len(arr2):
        return False
    
    freq_arr1 = {}
    
    for x in arr1:
        {x: freq_arr1.get(x, 0) + 1 for x in arr1}
        if x in freq_arr1:
            freq_arr1[x] += 1
        else:
            freq_arr1[x] = 1
            
    freq_arr2 = {key**2: value for key, value in freq_arr1.items()}
    
    for y in arr2:
        if y in freq_arr2:
            freq_arr2[y] -= 1
        else:
            return False
    
    return all(value == 0 for value in freq_arr2.values())


def same_refactored(arr1: List, arr2: List) -> bool:
    
    if len(arr1) != len(arr2):
        return False
    
    freq_arr1 = {}
    freq_arr2 = {}
    
    for x in arr1:
        freq_arr1[x] = 1 if x not in freq_arr1 else freq_arr1[x] + 1
    
    for x in arr2:
        freq_arr2[x] = 1 if x not in freq_arr2 else freq_arr2[x] + 1

    for key in freq_arr1:
        if (key ** 2) not in freq_arr2:
            return False
        if freq_arr2[key ** 2] != freq_arr1[key]:
            return False
    
    return True


if __name__ == "__main__":
    print(same_naive([1, 2, 3], [4, 1, 9]))
    print(same_naive([1, 2, 3], [1, 9]))
    print(same_naive([1, 2, 1], [4, 4, 1]))
    
    print(same_refactored([1, 2, 3], [4, 1, 9]))
    print(same_refactored([1, 2, 3], [1, 9]))
    print(same_refactored([1, 2, 1], [4, 4, 1]))
    