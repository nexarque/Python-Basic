num = int(input("enter a positive number : "))
factorial = 1 
counter = num
while counter > 0 :
    factorial *= counter
    counter -= 1
    print(f"factorial of {num} is {factorial}")