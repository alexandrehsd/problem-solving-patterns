"""
given two strings, write a function to determine if the second string
is an anagram of the first. an anagram is a word, phrase, or name formed
by rearranging the letters of another, such as cinema, formed from iceman
"""


def anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2): 
        return False
    
    freq_counter1 = {}
    freq_counter2 = {}
    
    for l in str1:
        freq_counter1[l] = 1 if l not in freq_counter1 else freq_counter1[l] + 1
    
    for l in str2:
        freq_counter2[l] = 1 if l not in freq_counter2 else freq_counter2[l] + 1
        
    for l in str1:
        if l not in freq_counter2:
            return False
        if freq_counter2[l] != freq_counter1[l]:
            return False
        
    return True


if __name__ == "__main__":
    print(anagram("", ""))
    print(anagram("aaz", "zaa"))
    print(anagram("hello", "world"))
    print(anagram("hi", "there"))
    