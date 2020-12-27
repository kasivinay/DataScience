# Input Two Strings and Display the Larger String
# without Using Built-in Functions:


# this is using built in functions


a = input("enter a string:")
v = input("enter a string:")
c = len(a)
d = len(v)
if c>d:
    print("{} is Larger String".format(a))
elif d>c:
    print("{} is Larger String".format(v))
else:
    print("{} both strings are equal".format(a,v))
