import string
import random

x = "".join(random.choices(string.ascii_uppercase,k=2))
y = "".join(random.choices(string.digits,k=4))

xy = x+y


print(xy)