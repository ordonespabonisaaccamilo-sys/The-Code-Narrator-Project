def check_number(num):
    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return result

number = int(input("Enter a number: "))
answer = check_number(number)
print(answer)