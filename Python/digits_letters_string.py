# Count the number of digits & letter in a string:

s = 'My name is vinay i am learning Datascience and Machine Learning fromm dec 17'
count1 = 0
count2 = 0
for i in s:
    if (i.isdigit()):
        count1 = count1+1
    else:
        count2 = count2+1
print("no of digits in s are {}".format(count1))
print("no of letters in s are {}".format(count2))
print(len(s))
