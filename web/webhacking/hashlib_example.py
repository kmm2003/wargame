import hashlib
string = 'admin'
encoded_string = string.encode()
print(encoded_string)
hexdigest = hashlib.sha512(encoded_string).hexdigest()
print('a:',hexdigest)