# Count Number of Lowercase Characters in a String:


s = 'Hello WORld'
count1 = 0
for i in s:
    if (i.islower()):
        count1 = count1+1
print("no of lowercase characters in a string are {}".format(count1))
print(len(s))
