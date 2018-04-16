import hashlib

def generate_password(original_password, salt):
    first_hash_password = hashlib.md5(original_password).hexdigest()
    password = hashlib.md5(first_hash_password + salt).hexdigest()
    return password