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
        return string
    elif len(string) >= 3 and string[-3:] == 'ing':
        string = string + 'ly'
        return string
    else:
        return string


quest5 = input('Add ing in given string >> ')
print()
print(addString(quest5))

# 6) Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


def substitute(string):
    indexNot = string.find('not')
    indexPoor = string.find('poor')
    if indexPoor > indexNot and indexNot > 0 and indexPoor > 0:
        string = string.replace(string[indexNot:indexPoor+4], 'good')
        return string
    else:
        return string


quest6 = input('Change everthing followed by not to good >> ')
print()
print(substitute(quest6))


# 7)  Write a Python function that takes a list of words and returns the length of the longest one.

def countLength(array):
    array = array.split(',')
    count = 0
    if isinstance(array, list):
        for i in range(1, len(array)):
            if len(array[count]) > len(array[i]):
                count = count
            else:
                count = i
        return array[count]


quest7 = input(
    'Calculate the longest length of word in list, seperate word by comma >> ')
print()
print(countLength(quest7))


# 8) Write a Python program to remove the nth index character from a nonempty string.

def removeChar(string, index):
    if len(string) > 0:
        return string[:index] + string[index+1:]


quest8 = input(
    'Remove the nth index of the character from nonempty string >> ')
index = int(input('Enter the index >> '))
print()
print(removeChar(quest8, index))

# 9) Write a Python program to change a given string to a new string where the first and last chars have been exchanged.


def exchangeChar(string):
    return string[-1:]+string[1:-1]+string[:1]


quest9 = input('Exchange the strings first and last chars >> ')
print()
print(exchangeChar(quest9))

# 10) Write a Python program to remove the characters which have odd index values of a given string.


def removeOdd(string):
    count = 0
    val = ''
    for _ in range(len(string)-1):
        if count % 2 == 0:
            val += string[count]
            count += 1
        else:
            count += 1
    return val


quest10 = input('return the even value from the string >> ')
print()
print(removeOdd(quest10))
