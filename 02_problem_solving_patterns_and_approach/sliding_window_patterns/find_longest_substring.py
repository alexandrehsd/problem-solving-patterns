"""
Write a function called find_longest_substring, which accepts a string and
returns the length of the longest substring with all distinct characters.
"""


def find_longest_substring(input: str) -> int:
    
    longest = 0
    seen = {}
    start = 0

    for i in range(len(input)):
        char = input[i]
        if char in seen:
            start = max(start, seen[char])
        # index - beginning of substring + 1 (to include current in count)
        longest = max(longest, i - start + 1)
        # store the index of the next char so as to not double count
        seen[char] = i + 1

    return longest


if __name__ == "__main__":
    print(find_longest_substring(''))  # 0
    print(find_longest_substring('rithmschool'))  # 7
    print(find_longest_substring('thisisawesome'))  # 6
    print(find_longest_substring('thecatinthehat'))  # 7
    print(find_longest_substring('bbbbbb'))  # 1
    print(find_longest_substring('longestsubstring'))  # 8
    print(find_longest_substring('thisishowwedoit'))  # 6
    print(find_longest_substring("abcabcbb"))  # 3
