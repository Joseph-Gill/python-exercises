# Create a function that returns true when passed a string as a parameter

def is_string(string):
    return type(string) is str


# print(is_string('hello'))  # True
# print(is_string(['hello']))  # False
# print(is_string('this is a long sentence'))  # True
# print(is_string({'a': 2}))  # False


# Create a function based off is_string that checks if the argument contains spaces or digits

def is_only_string(test_string):
    if is_string(test_string):
        for index in test_string:
            if index in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]:
                return False
        return True
    return False


# print(is_only_string("11"))  # False
# print(is_only_string("hello"))  # True
# print(is_only_string("this is a long sentence"))  # False
# print(is_only_string({"a": 2}))  # False


# Create a function that returns true if all characters in the string are alphanumeric and is not empty
import re


def is_alphanumeric(test_string):
    if is_string(test_string):
        if re.search('[^a-zA-Z0-9_]', test_string):
            return False
        return True
    return False


# print(is_alphanumeric("11"))  # True
# print(is_alphanumeric(["Hello"]))  # False
# print(is_alphanumeric("This is a long sentence"))  # False
# print(is_alphanumeric({"a": 2}))  # False
# print(is_alphanumeric("this is a string.....!!!"))  # False


# Create a function that returns true when arguments passed are a list or tuple

def is_list_or_tuple(test_list):
    return type(test_list) == list or type(test_list) == tuple


# print(is_list_or_tuple("Hello"))  # False
# print(is_list_or_tuple(["Hello"]))  # True
# print(is_list_or_tuple([2, {}, 2]))  # True
# print(is_list_or_tuple({"a": 2}))  # False
# print(is_list_or_tuple((1, 2)))  # True
# print(is_list_or_tuple(set()))  # False


# Create a function that checks all elements of a list are the same data type

def same_type(test_data):
    data_type = None
    for index in test_data:
        if not data_type:
            data_type = type(index)
        if not type(index) == data_type:
            return False
    return True


# print(same_type(["hello", "world", "long sentence"]))  # True
# print(same_type([1, 2, 9, 10]))  # True
# print(same_type([["hello"], "hello", ["bye"]]))  # False
# print(same_type([["hello"], [1, 2, 3], [{"a": 2}]]))  # True
# print(same_type([["hello"], set("hello")]))  # False
