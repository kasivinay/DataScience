for i in range(1,100):
    if i%3 == 0 and i%5 ==0:
        print("FizzBuzz")
        continue
    elif i%3 ==0:
        print("Fizz")
        continue
    elif i%5 ==0:
        print("Buzz")
        continue
    elif i%i != 0:
        print("prime")
        continue
    print(i)
        
        
