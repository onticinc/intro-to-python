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