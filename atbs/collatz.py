# collatz

def collatz(number):
    if number % 2 == 0:
        print(number // 2 )
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    number = int(input("enter an integer: "))
    result = collatz(number)
    print(f"the result is {result}")
    if result == 1:
        break
