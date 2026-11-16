import random
import string

x = "".join(random.choices(string.ascii_lowercase,k=3))
y = "".join(random.choices(string.digits,k=3))
u =(random.choice(string.punctuation))

xyu= x+y+u
print(xyu)