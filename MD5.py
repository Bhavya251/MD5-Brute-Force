import hashlib

def calcmd5(str_normal):
    result = hashlib.md5(str_normal.encode())
    str_hash = result.hexdigest()
    return str_hash
