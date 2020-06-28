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

# 11) Write a Python program to count the occurrences of each word in a given sentence.


def countWord(string):
    numString = {}
    string = string.split(' ')

    for i in string:
        keys = numString.keys()
        if i not in keys:
            numString[i] = 1
        else:
            numString[i] += 1
    return numString


quest11 = input('Count the occurrences of each word in given sentence >> ')
print()
print(countWord(quest11))

# 12) Write a Python script that takes input from the user and displays that input back in upper and lower cases.


def stringCasing(string):
    return (string.upper(), string.lower())


quest12 = input('Enter the string >> ')
print()
print('The string you have enter into upper case >> '+stringCasing(quest12)[0])
print('The string you have enter into lower case >> '+stringCasing(quest12)[1])


# 13) Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

def alphaSort(string):
    string = string.split(',')
    string.sort()
    return string


quest13 = input(
    'Sequnce of word as input seprated by comma, to print sorted from alphanumerically >> ')
print()
print(alphaSort(quest13))

# 14) Write a Python function to create the HTML string with tags around the word(s).


def add_tags(tag, string):
    return '<'+tag+'>'+string+'</'+tag+'>'


quest14 = input('Warp you text in html tag >> ')
tag = input('tag you wanna warp on >>')
print()
print(add_tags(tag, quest14))

# 15) Write a Python function to insert a string in the middle of a string.


def insert_sting_middle(string, text):
    countString = len(string)
    half_of_string = int(countString / 2)
    return string[:half_of_string]+text+string[half_of_string:]


quest15 = input('Wrap you string inside string >> ')
text = input('String you wanna warp with >> ')
print()
print(insert_sting_middle(text, quest15))

# 16) Write a Python program to sum all the items in a list.


def sumList(numbers):
    try:
        numbers = numbers.split(' ')
        sum_value = sum([int(num) for num in numbers])
        return sum_value
    except:
        return 'The value must be number and seprated by space'


quest16 = input('Enter list of numbers, sperate with space >> ')
print()
print(sumList(quest16))

# 17) Write a Python program to multiplies all the items in a list.


def multiply(numbers):
    try:
        numbers = numbers.split(' ')
        values = [int(num) for num in numbers]
        mun = 1
        for i in values:
            mun *= i
        return mun
    except:
        return 'The value must be number and seprated by space'


quest17 = input('Enter list of numbers, sperate with space >> ')
print()
print(multiply(quest17))

# 18) Write a Python program to get the largest number from a list.


def Largest(numbers):
    numbers = numbers.split(' ')
    numbers = [int(num) for num in numbers]
    numbers.sort()
    return numbers[len(numbers)-1]


quest18 = input('Enter list of numbers, sperate with space >> ')
print()
print(Largest(quest18))

# 19) Write a Python program to get the smallest number from a list.


def Smallest(numbers):
    numbers = numbers.split(' ')
    numbers = [int(num) for num in numbers]
    numbers.sort()
    return numbers[0]


quest19 = input('Enter list of numbers, sperate with space >> ')
print()
print(Smallest(quest19))

# 20) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.


def conditionCount(string):
    count = 0
    string = string.split(',')
    for i in string:
        if len(i) > 2 and i[:1] == i[-1:]:
            count += 1
    return count


quest20 = input('Enter list of word sperate them by comma >> ')
print()
print(conditionCount(quest20))

# 21) Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


def sortTuple(unsorted):
    unsorted = unsorted.split(',')
    sorting = [tuple(sort) for sort in unsorted]
    sorting.sort()
    return sorting


quest21 = input('Enter tuples sperated by commas >> ')
print()
print(sortTuple(quest21))

# 22) Write a Python program to remove duplicates from a list.


def removeDuplicate(sList):
    sList = sList.split(' ')
    usList = []
    for i in sList:
        if i not in usList:
            usList.append(i)
    return usList


quest22 = input('Enter list of word sperated by space >> ')
print()
print(removeDuplicate(quest22))

# 23) Write a Python program to check a list is empty or not.


def checkList(sList):
    sList = sList.split()
    if len(sList) <= 0:
        return 'The list is empty'
    else:
        return 'The list is not empty'


quest23 = input('Enter item in list sperated by space >> ')
print()
print(checkList(quest23))

# 24) Write a Python program to clone or copy a list.


def copyList(sList):
    new_list = sList()
    return new_list


print()
print('This is copyed list' + copyList([1, 2, 3, 4, 5]))

# 25) Write a Python program to check whether all dictionaries in a list are empty or not.


def inside_list(objList):
    for i in objList:
        if len(i) > 0:
            return True
        else:
            return False


print()
print(inside_list([{}, {}, {}]))
print(inside_list([{1, 2}, {}, {}]))


# 26. Write a Python program to insert a given string at the beginning of all items in a list.

def insertString(slist, string):
    slist = slist.split()
    for i in range(len(string)-1):
        slist[i] = str(string+slist[i])
    return slist


quest26 = input('Enter input list of word seprated by space >> ')
text = input('enter string you wanna add >> ')
print()
print(insertString(quest26, text))

# 27) Write a Python program to replace the last element in a list with another list.


def replaceChar(fList, sList):
    return fList[:-1]+sList


print()
print(replaceChar([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))


def addKey(norDict):
    keys = list(norDict.keys())
    value = list(norDict.values())
    if (keys[-1:][0]+1) not in keys:
        norDict[keys[-1:][0]+1] = value[-1:][0]+10
        return norDict


print()
print(addKey({1: 10, 2: 20}))

# 29. Write a Python script to concatenate following dictionaries to create a new one.


def dict_concat():
    new_dic = {}
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    keys = list(dic1.keys()) + list(dic2.keys()) + list(dic3.keys())
    values = list(dic1.values()) + list(dic2.values()) + list(dic3.values())

    for i in range(len(keys)-1):
        new_dic[keys[i]] = values[i]
    return new_dic


print()
print(dict_concat())

# 30) Write a Python script to check whether a given key already exists in a dictionary.


def dict_check(string):
    dic = {'1': 'prayag', '2': 'piya'}
    if string in dic.keys():
        return True
    else:
        return False


quest30 = input('Enter key to check >> ')
print()
print(dict_check(quest30))

# 31) Write a Python program to iterate over dictionaries using for loops.


def iterate_dict(dic):
    key, value = dic.items()
    for i in key:
        print('Key '+i + ' Value' + dic[i])


print()
iterate_dict({1: 2, 3: 4, 5: 6, 7: 8})

# 32) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form


def createDic(n):
    dic = {}
    for i in range(1, n+1):
        dic[i] = i*i
    return dic


quest32 = input('enter a range >> ')
print()
print(createDic(int(quest32)))

# 33) Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys


def squareDic():
    dic = {}
    for i in range(1, 16):
        dic[i] = i**i
    print(dic)


print()
squareDic()

# 34) Write a Python script to merge two Python dictionaries.


def mergeDic(dic1, dic2):
    new_dic = dic1
    for key, value in dic2.items():
        new_dic[key] = value
    return new_dic


print()
print({1: 2, 2: 3}, {4: 5, 6: 7})

# 35) Write a Python program to iterate over dictionaries using for loops.

print()
iterate_dict({'prayag': 'piya', '1': 2, '5': 6})

# 36) Write a Python program to sum all the items in a dictionary.


def sumValue(dic):
    return sum(dic.values())


print()
print(1: 10, 3: 30, 2: 20, 4: 40)

# 37) Write a Python program to multiply all the items in a dictionary.


def multiplyValue(dic):
    value = dic.values()
    mun = 1
    for i in value:
        mun *= i
    return mun


print()
print(multiplyValue({1: 2, 3: 40, 5: 3, 6: 7}))

# 38) Write a Python program to remove a key from a dictionary.


def removeKey(dic, key):
    del dic[key]
    return dic


print({'1': 3, 'prayag': 'piya', '5': 20})
key = input('Enter key you wanna delate >> ')
print()
print(removeKey({'1': 3, 'prayag': 'piya', '5': 20}, key))


# 39. Write a Python program to unpack a tuple in several variables.

def unpackTuple(smallbracket):
    data1, data2, data3 = smallbracket
    print('unpacked tuple = ' + data1 + data2 + data3)


print()
unpackTuple(('prayag', 5, True))

# 40) Write a Python program to add an item in a tuple.


def addindex(tupl, index):
    tupl = tupl+(index,)
    return tupl


print()
print(addindex((1, 2, 3, 4, 5), 'prayag'))

# 41) Write a Python program to convert a tuple to a string.


def convertTuple(tup):
    string = ''.join(tup)
    return string


print()
print(convertTuple(('p', 'r', 'a', 'y', 'a', 'g'))

# 42) Write a Python program to convert a list to a tuple.

def tupleBack(sList):
    return tuple(sList)

print()
print(tupleBack([1, 2, 3, 4, 5, 6]))

# 43) Write a Python program to remove an item from a tuple.

def remveItem(tup, item):
    tup=list(tup)
    tup.remove(item)
    tup=tuple(tup)
    return tup

print((1, 2, 3, 4, 5, 6))
item=int(input('Item you wanna remove >> '))
print()
print(remveItem((1, 2, 3, 4, 5, 6), item))


# ---------
# FUNCTION
# ---------

def maxNumber(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3

num1=int(input('Enter a number >> '))
num2=int(input('Enter a number >> '))
num2=int(input('Enter a number >> '))
print()
print(maxNumber(num1, num2, num3))


sList=[1, 50, 6, 10, 2, 0]
sort=lambda a: a.sort()
sort(sList)
print(sList)
