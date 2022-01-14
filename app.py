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






# from unittest import result


# def say_hello(friend="Tim"):
#   print("Hello, {}!".format(friend))

# def move(name, city="Seattle", state="Washington"):
#   msg = "{} is moving to {}, {}"
#   msg = msg.format(name, city, state)
#   print(msg)

# move("Charlie")

# say_hello('mike')

# def car(name, type='honda'):
#     msg ="{} is a {} "
#     msg = msg.format(name, type)
#     print(msg)

# car('civic')

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
    },
     { 
        "name": "John",
        "city": "Atlanta"
    },
    { 
        "name": "Jane",
        "city": "New York"
    },
    { 
        "name": "Rob",
        "city": "Los Angeles"
    },
     { 
        "name": "Harper",
        "city": "Washington"
    },
    { 
        "name": "Mike",
        "city": "Seattle"
    },
    { 
        "name": "Set",
        "city": "San Francisco"
    },
]


# def get_cities(students):
#     '''Return a [list] of all cities'''

#     result = []

#     for s in students:
#         if s.get('city'):
#             result.append(s.get('city'))
#     return result

# print('cities list:', get_cities(students))


# def get_names(students):
    
#     result = []

#     for n in students:
#         if n.get('name'):
#             result.append(n.get('name'))
#     return result

# print('name list:', get_names(students))


# def par_by_cities(students):
#     '''
#     Return Dict that has a key for each city and 
#     a list of students for each city
#     '''

def parse_by_cities(students):
    #TODO make a empty dict
    #TODO Iterate through the list of students and perform logic
        # check if city is in dict if not
            # add the city add set tp empty list
        # logic => if city is in the dictionary
            # append student name to list
    #TODO return the dict

    result = {}

    for student in students:
        print('printing INSIDE', student)
        if student.get('city'):
            if not result.get(student.get('city')):
                print('Does Not Exist')
                result[student.get('city')] = []
                city_list = result[student.get('city')]
                city_list.append(student.get('name'))
            else:
                print('Does Exist')
                city_list = result[student.get('city')]
                city_list.append(student.get('name'))
    
    print('---------------------')
    return result
print('printing OUTSIDE', parse_by_cities(students))


