import socket 
import sys              # Import socket module

s = socket.socket()         # Create a socket object
host = str(sys.argv[1])                #socket.gethostname()
port = int(sys.argv[2])         # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024))                                       


while True:

    cmd = input("Please Enter an Equation:")        #store user equation in a variable

    
    s.send(str(cmd).encode())                           #sends cmd (equation) to server


    


    ans = s.recv(1024).decode()                         #receives the computed equation
    print (ans)



s.close()
