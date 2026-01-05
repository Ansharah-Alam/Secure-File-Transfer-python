import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def receive_data(conn):
    length_bytes = conn.recv(4)
    data_length = int.from_bytes(length_bytes, "big")

    data = b""
    while len(data) < data_length:
        packet = conn.recv(data_length - len(data))
        if not packet:
            break
        data += packet

    return data


#### SERVER SETUP ####

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server listening on port 5000...")

conn, addr = server.accept()
print("Connected with", addr)

#### RECEIVE DATA ####

encrypted_data = receive_data(conn)
print("Encrypted file received")

key = receive_data(conn)
print("AES key received")

iv = receive_data(conn)
print("IV received")

file_hash = receive_data(conn).decode()
print("File hash received")

#### DECRYPTION ####

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

print("Decryption successful")
print("Decrypted file size:", len(decrypted_data), "bytes")


###### HASH VERIFICATION #######

hash_obj = hashlib.sha256()
hash_obj.update(decrypted_data)
server_hash = hash_obj.hexdigest()


#### SAVING FILE #######

if server_hash==file_hash:                               #checking for file integrity
    print("Hash verified: File integrity confirmed")

    with open("received_file", "wb") as f:
        f.write(decrypted_data)

    print("File saved successfully")
else:
    print("Hash mismatch: File corrupted or tampered")
    print("File Not Saved")



conn.close()
server.close()
print("CONNECTION CLOSED")


