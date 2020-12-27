# Program to reverse a given number:

v = int(input("Enter a value: "))
rev = 0
while v > 0:
    z = v%10
    rev = rev*10 + z
    v = v//10
print(rev)
