# Secure-File-Transfer-python
This project is a secure client–server file transfer system built using Python sockets.

## Overview
The client encrypts a file using AES encryption and generates a SHA-256 hash for integrity.  
The encrypted file, along with the key, IV, and hash, is sent to the server.  
The server decrypts the file, verifies the hash, and saves the file securely.

## Features
 Client–server architecture using TCP sockets
 AES encryption for data confidentiality
 SHA-256 hashing for file integrity verification
 Secure file transmission over a network

## Technologies Used
 Python
 Socket Programming
 AES Encryption
 SHA-256 Hashing

## How to Run
1. Run server.py from the Server folder
2. Run client.py from the Client folder

## Testing
The project was tested by:
 Verifying successful client–server connection
 Ensuring encrypted file transmission
 Confirming correct decryption on the server side
 Validating file integrity using hash comparison
 Checking that the saved file matches the original file

## Contributors
Abiha Jamshed  
Ansharah Alam
