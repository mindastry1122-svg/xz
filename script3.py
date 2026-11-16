import random
import string

x = string.ascii_letters

y = string.digits

u = string.punctuation

all_chars = x + y + u
random_char = random.choice(all_chars)
password = "".join([random.choice(all_chars)for _ in range(10)])
print(password)