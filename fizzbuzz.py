from sre_constants import RANGE


def fizz_buzz(max):
    for i in range(max):
        if i % 3 == 0 and i % 5 != 0:
            print(i, 'fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print(i, 'buzz')
        elif i % 5 == 0 and i % 3 == 0:
            print(i, 'fizzbuzz')
 
fizz_buzz(30)