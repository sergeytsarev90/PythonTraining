import random
import string

# class Strings:
#     def __init__(self):
#         pass
#
def random_string(prefix,maxlen,type):
    if type is "allstring":
        symbols = string.ascii_letters+string.digits+string.punctuation+" "*5
        return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    elif type is "digits":
        symbols = string.digits
        return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    elif type is "letters":
        symbols = string.ascii_letters
        return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])