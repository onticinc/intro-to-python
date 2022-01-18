numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result = map(double_number, numbers)
print(list(result))


result2 = map(lambda x: x + x, numbers)
print('Result Two =>', list(result2))

result3 = map(lambda y: y * y, numbers)
print('result three', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
print('Result 4',list(result4))


# a list containing both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]



