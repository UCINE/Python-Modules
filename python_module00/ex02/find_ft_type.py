"""well for this exercise you can impliment it with if else statments if you wanna acheive the same output
as the subject but its the same shit lool because The point of this exercise is to practice and
understanding OOP concept like objects and their types, and learning how to handle different type
de data structure where functions can accept any type of object as an argument lool and thats why we love python :),
"""
#so simply you can do it like this 

def all_thing_is_obj(obj):
    if isinstance(obj, str) or hasattr(obj, '__iter__'):
        print(f'type of the object is: {type(obj).__name__}')
    else:
        print("Type not found!")
    return (42)

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")

print(all_thing_is_obj(10))

#but if you wanna if else it, here you go

"""
def all_thing_is_obj(obj):
    if isinstance(obj, list):
        print(f'List : {type(obj)}')
    elif isinstance(obj, tuple):
        print(f'Tuple : {type(obj)}')
    elif isinstance(obj, set):
        print(f'Set : {type(obj)}')
    elif isinstance(obj, dict):
        etc ...

"""