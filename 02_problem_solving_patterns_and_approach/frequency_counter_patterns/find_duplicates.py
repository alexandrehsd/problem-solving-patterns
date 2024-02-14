"""
Implement a function called, are_there_duplicates which accepts a variable
number of arguments, and checks whether there are any duplicates among
the arguments passed in.
You can solve this using the frequency counter pattern OR the multiple 
pointers pattern.
"""


def are_there_duplicates_naive(*args) -> bool:
    # o(n^2) complexity
    arguments = []
    for arg in args:
        if arg in arguments:
            return True
        else:
            arguments.append(arg)
    return False


def are_there_duplicates_refactored(*args) -> bool:
    # O(n)
    arguments = {}
    for arg in args:
        arguments[arg] = 0 if arg not in arguments else arguments[arg] + 1
    
    for key in arguments:
        if arguments[key] > 0:
            return True
    
    return False


def are_there_duplicates_oneliner(*args) -> bool:
    return len(set(args)) != len(args)


if __name__ == "__main__":
    print(are_there_duplicates_naive(1, 2, 3))
    print(are_there_duplicates_naive(1, 2, 2))
    print(are_there_duplicates_naive("a", "b", "c", "b"))
    
    print(are_there_duplicates_refactored(1, 2, 3))
    print(are_there_duplicates_refactored(1, 2, 2))
    print(are_there_duplicates_refactored("a", "b", "c", "b"))
    
    print(are_there_duplicates_oneliner(1, 2, 3))
    print(are_there_duplicates_oneliner(1, 2, 2))
    print(are_there_duplicates_oneliner("a", "b", "c", "b"))
    