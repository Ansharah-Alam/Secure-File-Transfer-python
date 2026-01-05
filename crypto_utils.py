from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_file(file_data):
    # Generate a 32-byte key for AES-256
    key = get_random_bytes(32)

    # Generate a random 16-byte IV
    iv = get_random_bytes(16)

    # Create AES cipher (CBC mode)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the file data (with padding)
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))

    return encrypted_data, key, iv
