def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)): 
        if string [i : i+len(sub_string)] == sub_string:
            count += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Constraints


# Each character in the string is an ascii character.

# Iteration 1 =0 python string[i : i+len(sub_string)] string[0 : 0+3] string[0:3] given: string = "abracadabra"

# sub_string ="abr"

# count +1 = 1