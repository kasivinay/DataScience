# Python Program to Count the Number of Vowels in a String

h = input("enter a string:")
vowels = 0
for i in h:
    if (i == 'a'or i == 'e'or i == 'i'or i =='o'or i == 'u'or i == 'A'or i == 'E'or i =='I'or i == 'O'or i =='U'):
        vowels = vowels+1
print(vowels)

