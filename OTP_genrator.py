import random
import string
lenth =6
characters = string.digits
otp = ''.join(random.choice(characters) for _ in range (lenth))
print(otp)