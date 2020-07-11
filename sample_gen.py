import pandas as pd
import numpy as np 
from random import randint, choice
import inspect, re
import datetime
import string
import secrets
import time
 
#Generate Pass, count: number of generate passwords, maxlength: maximum password length
def generatePass(count, maxLength=15):
    arr = []
    alphabet = string.ascii_letters + string.digits
    for i in range(count):
        password = ''.join(secrets.choice(alphabet) for i in range(maxLength))
        arr.append(password)
    return arr


#printing variable name, not necessary actually
def varname(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)


#Generate Email, count: number of generated items,
def randomEmail(count):
    arr = []
    letters = string.ascii_lowercase
    mails = ["hotmail", "gmail", "protonmail","outlook"]
    for i in range(count):
        word = ''
        word = '{}@{}.com'.format(''.join(
            choice(letters) for j in range(randint(6, 15))), choice(mails))
        arr.append(word)
    return arr


#Generate elements from given array
"""
arr: Given array
N: number of items to generate
unique: True if generated elements are unique from each other
multiple: True if you want to generate an arrays of arrays
limit: If multiple is true, limit the number of array to generate of arrays
"""


def generateArr(
        arr, N, unique=False, multiple=False, limit=0
):  #Generate random elements from given array, Cant create unique array of arrays
    n = len(arr)
    tarr = arr.copy()
    newarr = []

    if (limit == 0):
        limit = n
    assert not (
        n < N and unique == True
    ), "WHEN UNIQUE NUMBER GENERATING, POSSIBLE VALUES MUST LOWER OR EQUAL THEN ELEMENT COUNT "

    for i in range(0, N):

        if (multiple):
            newarr.append(generateArr(arr, randint(1, limit), unique=True))
        else:
            if (unique):
                index = randint(0, n - i - 1)
                newarr.append(tarr[index])
                tarr.remove(tarr[index])
            else:
                index = randint(0, n - 1)
                newarr.append(tarr[index])
    return newarr


#Generate random integer in integer or string format
"""
count: number of generated items,
n: number of digits of item
unique: True if generated elements are unique from each other
asStrEqualUnique: True if unique request always returned as strings
intType: integer type to generate 
multiple: True if you want to generate an arrays of arrays
limit: If multiple is true, limit the number of array to generate of arrays
"""


def randomN(count,
            n,
            unique=True,
            asStrEqualUnique=True,
            asStr=False,
            intType="int64",
            multiple=False,
            limit=2):  #Generate n digit number
    if (multiple):
        return generateArr(
            randomN(
                count,
                n,
                unique,
                asStrEqualUnique,
                asStr,
                intType,
                multiple=False).tolist(),
            count,
            multiple=True,
            limit=limit,
            unique=False)
    if (asStrEqualUnique):
        asStr = unique
    if (asStr):
        arr = np.zeros(count, dtype=object)
        for i in range(0, count):
            string = ""
            while (unique and (string in arr or string == "")):
                string = ""
                for j in range(0, n):
                    string = string + str(randint(0, 9))
            arr[i] = string

    else:
        assert not (
            pow(10, n) < count and unique == True
        ), "WHEN UNIQUE NUMBER GENERATING, 10^N MUST BE BIGGER THAN COUNT "

        arr = np.empty(count, dtype=intType)
        for i in range(0, count):
            range_start = 10**(n - 1)
            range_end = (10**n) - 1
            val = randint(range_start, range_end)
            while (unique and val in arr):
                val = randint(range_start, range_end)
            arr[i] = val

    return arr


#Generate random Date
"""
start_date: date to start generate from
range_in_days: range to generate
N: number of elements to generate
"""


def random_date_generator(start_date, range_in_days, N):  #Generate random date
    arr = []
    for i in range(0, N):
        days_to_add = np.arange(0, range_in_days)
        arr.append(np.datetime64(start_date) + np.random.choice(days_to_add))
    return arr


#Convert and map 0 and 1s to another key
"""
case1: element to change from 1 
case2: element to change from 2 
N: length of elements  
"""


def randomTF(case1, case2, N):  #Generate random True False
    arr = np.random.randint(2, size=N)
    mapFunc = lambda x: case1 if x == 1 else case2
    mapFunc = np.vectorize(mapFunc)
    return mapFunc(arr)

 


#print for dataframes
def prinit(caption, x):
    print("\t\t" + caption[:-1].upper() + "\n")
    print(x.head(3))
    print("\n\n{}".format(x.dtypes))
    split()


#Generate 0 and 1 array
"""
count: number of elements to generate
n: number of digits of item
allZero: True if you want to generate every element is zero
"""


def generateBit(count, n, allZero=False):
    arr = np.empty(count, dtype=object)
    bits = ["0", "1"]
    if (allZero):
        bits = ["0"]
    for i in range(0, count):
        arr[i] = "".join(generateArr(bits, n))
    return arr


#Change non-list types's given index to given value
def strIndex(s, index, value):
    s = list(s)
    s[index] = value
    s = ''.join(s)
    return s


#Generate TimeStamp
def generateTs(count, unique=True, onlyHour=True):
    arr = []
    hour = 8
    assert count < 24, "24 SAAT DERS OLAMAZ "
    for i in range(count):
        hour = hour + 1
        if (onlyHour):
            stringg = hour
        else:
            stringg = ("{:0=2d}:00:00".format(hour))
        arr.append(stringg)
    return arr
