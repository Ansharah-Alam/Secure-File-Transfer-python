import socket
from hash_utils import generate_hash
from crypto_utils import encrypt_file

#CREATE SOCKET
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONNECT TO SERVER 
client.connect(("127.0.0.1", 5000))

#READ FILE IN BINARY MODE
with open("test.txt", "rb") as file:
    file_data = file.read()
   
#GENERATE HASH OF FILE 
file_hash = generate_hash(file_data)

#ENCRYPT FILE
encrypted_data, key, iv = encrypt_file(file_data)

######## SENDING DATA #######
def send_data(sock, data):
    #Send length first (4 bytes)
    sock.send(len(data).to_bytes(4, "big"))
    #Send actual data
    sock.sendall(data)

#SEND ENCRYPTED FILE
send_data(client, encrypted_data)
print("Encrypted file sent")

#SEND KEY
send_data(client, key)
print("AES key sent")

#SEND IV
send_data(client, iv)
print("IV sent")

#SEND HASH (convert string to bytes)
send_data(client, file_hash.encode())
print("File hash sent")

#CLOSE CONNECTION
client.close()
print("CONNECTION CLOSED")


