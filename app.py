    # Comment
    # Todo build this function
    

# name = "Johnny"
# print(name)

# nothing = None
# is_working = True
# car_off = False

# if is_working:
#     print('this is true')
# else:
#     print('this is not true')


# print(15 / 6)
# print(15 // 6)

# statement = "my code rulez" [3:7]
# print(statement)

# date = "today"
# food = "oatmeal"
# meals = "breakfast"

# mymessage = f"{date} i ate {food} for {meals}."

# print(mymessage)






from unittest import result


def say_hello(friend="Tim"):
  print("Hello, {}!".format(friend))

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Charlie")

say_hello('mike')

def car(name, type='honda'):
    msg ="{} is a {} "
    msg = msg.format(name, type)
    print(msg)

car('civic')

students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    }
]


def get_cities(students):
    '''Return a [list] of all cities'''

    result = []

    for s in students:
        if s.get('city'):
            result.append(s.get('city'))
    return result

print('cities list:', get_cities(students))


def get_names(students):
    
    result = []

    for n in students:
        if n.get('name'):
            result.append(n.get('name'))
    return result

print('name list:', get_names(students))