# 1) Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'


def countChar(string):
    numString = {}

    for i in string:
        keys = numString.keys()
        if i not in keys:
            numString[i] = 1
        else:
            numString[i] += 1
    return numString


print("Answering question number 1")
print(countChar('google.com'))


# 2 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def redefineString(string):
    value = ''

    if len(string) < 2:
        return ''
    else:
        value += string[:2]
        value += string[-2:]
        return value


print("Answering question number 2")
print(redefineString('python'))

# 3) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.


