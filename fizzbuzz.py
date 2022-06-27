for i in range(1, 100):
    if i%3==0 and i%5==0: #test for 3 and 5 first
        print("FizzBuzz")
    elif i%3==0: # test for 3
        print("Fizz")
    elif i%5==0: # test for 5
        print("Buzz")
    else: # just print
        print(i)

print( ['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i for i in range(1,100)] )