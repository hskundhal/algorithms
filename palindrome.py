def ispalindrome(str):
    if str == str[::-1]:
        return True
    return False

print(ispalindrome("car"))
print(ispalindrome("radar"))