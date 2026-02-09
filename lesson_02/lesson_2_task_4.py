n = int(input("Введите число: "))

def fizz_buzz(n):
    for x in range(1, n):
        if x % 3 == 0:
            print(f"{x} Fizz")
        if x % 5 == 0:
            print(f"{x} Buzz")
        if x % 3 == 0 and n % 5 == 0:
            print(f"{x} FizzBuzz")
        else: print(x)

n = 17

fizz_buzz(n)