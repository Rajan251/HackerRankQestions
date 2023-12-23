if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Create a tuple from the input integers
    my_tuple = tuple(integer_list)

    # Print the hash value of the tuple
    print(hash(my_tuple))

# Task
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
    