# 1
idx = 'abcde'
print(idx[-2])
print(idx * 2)

# 2
num = 33
isEven = num % 2 == 0
print(isEven)
isNotEven = num % 2 == 1
print(isNotEven)

# 3
str1 = 'marker'
num = 'whiteboard'
print(len(str1) - len(num))

str2 = 'bootcamp'
print(str2.upper())
print(str2.lower())

#4
sentence = 'welcome to bootcamp prep'
lastChar = sentence[len(sentence[-1])]
print(lastChar)
print(sentence.index(lastChar))


# 5
age = 29 
if age > 30:
    print('older than 30')
else:
    print('younger than 30')

#6
str = 'pizza'
if len(str) > 10:
    print('long string')
else: 
    print('short string')
if (len(str[0]) == 'p'):
    print('starts with p')

#7
num = 15
if num % 3 == 0:
    print('divisible by 3')
elif num % 5 == 0: 
    print('divisible by 5')

#8

if num % 3 == 0:
    print('divisible by 3')
if num % 5 == 0:
    print('divisible by 5')

#9
str = 'General Assembly'
if str[0] == str[0].upper():
    print('starts with a capital')
if len(str[-1]) == len(str[-1]):
    print('ends with a capital')

#10
num = -44
if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print(0)
if num % 2 == 0:
    print('even')
else:
    print('odd')

#11
num = 11
if num > 5:
    print('less than "if"')

if num > 5:
    print('if')
else:
    print('else')

#Task 5 
#12
def sayHello(name):
    msg = 'Hello, ' + name + '. How are you?'
    return msg
print(sayHello('mike'))

#13
def checkNumber(num):
    if num > 10:
        return 'positive'
    elif (num < 0):
        return 'negative'
    else:
        return 'zero'
    
print(checkNumber(5))

#14
def fizz_buzz(max):
    for i in range(max):
        if i % 3 == 0 and i % 5 != 0:
            print(i, 'fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print(i, 'buzz')
        elif i % 5 == 0 and i % 3 == 0:
            print(i, 'fizzbuzz')
 
fizz_buzz(30)
