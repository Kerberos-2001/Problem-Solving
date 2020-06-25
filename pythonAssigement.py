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


ques = input("Count the number of characters frequency in a string >> ")
print()
print(countChar(ques))


# 2 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def redefineString(string):
    value = ''

    if len(string) < 2:
        return ''
    else:
        value += string[:2]
        value += string[-2:]
        return value


ques1 = input("Combine the string made of first 2 and last 2 chars >> ")
print()
print(redefineString(ques1))

# 3) Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.


def replaceText(string):
    count = 0
    secCount = 1
    var = ''
    for i in range(len(string)):
        if string[count] in string[secCount:]:
            var = string[secCount:].replace(string[count], '$')
            var = string[:secCount] + var
        else:
            count += 1
            secCount += 1
    return var


ques2 = input('Change the string where all occurrences of its first char >> ')
print()
print(replaceText(ques2))


# 4) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swapUp(string1, string2):
    var1 = string1[:2]
    var2 = string2[:2]
    return var2+string1[2:]+' '+var1+string2[2:]


quest3 = input("Give one string to swap the first 2 characters >> ")
quest4 = input("Give one string to swap the first 2 characters >> ")
print()
print(swapUp(quest3, quest4))


# 5) Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def addString(string):
    if len(string) >= 3 and string[-3:] != 'ing':
        string = string + 'ing'
    elif len(string) >= 3 and string[-3:] == 'ing':
        string = string + 'ly'
    else:
        return string


quest5 = input('Add ing in given string >> ')
print()
print(addString(quest5))

# 6) Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


def substitute(string):
    indexNot = string('not')
    indexPoor = string('poor')

    if indexPoor > indexNot:
        string = string.replace(string[indexNot:indexPoor+4], 'good')
        return string
    else:
        return string


quest6 = input('Change everthing followed by not to good >> ')
print(substitute(quest6))


# 7)
