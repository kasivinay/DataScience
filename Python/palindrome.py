# # Program to check if string is palindrome or not:

# A string is said to be palindrome if the reverse of the string is the same as string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.


s = input("enter a string: ")
x = s[::-1]
if x == s:
    print("{} is a palindrome".format(s))
else:
    print("{} is not a palindrome".format(s))
