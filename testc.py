_author__ = 'kyle'

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(input("Please Enter a Port Number") )           # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024))                                        #receive thanks for connecting and prints



while True:

    cmd = input("Please Enter an Equation:")            #store user equation in a variable

    s.send(str(cmd).encode())                           #sends cmd (equation) to server


    break
while True:

    ans = s.recv(1024).decode()                         #receives the computed equation
    print (ans)


s.close()
