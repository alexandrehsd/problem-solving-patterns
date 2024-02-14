"""
Write a function called sameFrequency. Given two positive integers, 
find out if the two numbers have the same frequency of digits.
"""


def same_frequency_digit(a: int, b: int) -> bool:
    
    a = str(a)
    b = str(b)
    
    if len(a) != len(b):
        return False
    
    digits1_freq = {}
    digits2_freq = {}
    
    for digit in a:
        digits1_freq[digit] = 1 if digit not in digits1_freq else digits1_freq[digit] + 1
        
    for digit in b:
        digits2_freq[digit] = 1 if digit not in digits2_freq else digits2_freq[digit] + 1
    
    for digit in digits1_freq:
        if digit not in digits2_freq:
            return False
        if digits1_freq[digit] != digits2_freq[digit]:
            return False
        
    return True


if __name__ == "__main__":
    print(same_frequency_digit(182,281))
    print(same_frequency_digit(34,14))
    print(same_frequency_digit(3589578, 5879385))
    print(same_frequency_digit(22,222))