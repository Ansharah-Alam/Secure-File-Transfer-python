import hashlib

def generate_hash(data):
    hash_object = hashlib.sha256(data)
    return hash_object.hexdigest()
