import string


def skyline(message):
    skyline_message = ""
    for x in list(message):
        if x not in string.ascii_lowercase:
            skyline_message += x
        elif message.index(x) % 2 == 0:
            skyline_message += x
        else:
            skyline_message += x.upper()
    return skyline_message


# class Uppercase:
#     def __init__(self, message):
#         self.message = str(message)
#         self.uppercase_message = self.message.upper()
#
#
# class Lowercase:
#     def __init__(self, message):
#         self.message = str(message)
#         self.lowercase_message = self.message.lower()
