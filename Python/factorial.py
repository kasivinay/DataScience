# Python program to find the factorial of a number:

fact = 1
z = int(input("Enter a value: "))
if z<0:
    print("Factorial doesnot exist for negative number")
elif z == 0:
    print("Factorila of 0 is 1")
else:
    for i in range(1,z+1):
        fact = fact*i
    print(fact)
    
