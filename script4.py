import random
import string


x = string.ascii_letters
y = string.digits
z = string.punctuation

xyz = x+y+z
xyz = "".join(random.choices(xyz , k=16))
print(xyz)