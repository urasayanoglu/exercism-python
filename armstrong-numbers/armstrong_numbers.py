def is_armstrong_number(number):
    sum = 0
    for digit in str(number):
        sum += int(digit) ** len(str(number))
    if sum == number:
        return True
    else:
        return False

