
# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

# initializing string
API_login_password = "Kielo2ph"

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(API_login_password.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())

