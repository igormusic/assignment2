
max_value = int(input("Please input a maximum value for the range of numbers you would like to check the primes of:\n"))
for number in range(2,max_value+1):
    i = 0
    while i <= 2:
        for factor in range(1,number+1):
            if number % factor == 0:
              i += 1
        if i == 2:
            print(number)