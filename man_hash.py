mens = "Hello World"
hash_value1 = hash(mens)
hash_value2 = hash(mens)

print(hash_value1)
print(hash_value2+1)

import hashlib
hash_object = hashlib.md5(mens.encode())
print(hash_object.hexdigest())
