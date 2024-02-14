"""
Write a function that takes in two strings and checks
whether the characters in the first string form a subsequence
of the characters in the second string.
In other words, the function should check whether the characters
in the first string appear somewhere in the second string,
without their order changing.
"""


def is_sub_sequence(str1: str, str2: str) -> bool:
    
    if len(str2) == 0:
        return False
    
    i = 0
    for j in range(len(str2)):
        reference = str1[i]
        
        if str2[j] == reference:
            i += 1
            
        if i == len(str1):
            return True
    
    return False
    
    
if __name__ == "__main__":
    print(is_sub_sequence("", "ahbgdc"))
    print(is_sub_sequence('hello', 'hello world'))
    print(is_sub_sequence('sing', 'sting'))
    print(is_sub_sequence('abc', 'abracadabra'))
    print(is_sub_sequence('abc', 'acb'))
    