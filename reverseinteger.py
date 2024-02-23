def reverseinteger(number):
    reversed = 0
    while (number > 0):

        oneval = number%10
        reversed = reversed*10 + oneval
        number = number/10
    return reversed

print(reverseinteger(1234))