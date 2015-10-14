import socket               # Import socket module
import sys

if len(sys.argv) !=5: 
   print ("Enter in Arguments ip port " )
  
else: 
   print("Error too many arguments")
   exit()	
host = str(sys.argv[1])
port = int(sys.argv[2])
err = "DivBy0"
Error = "Error"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send('Thank you for connecting'.encode())  
   break

while True:
 
   result=c.recv(1024).decode()                          
   result = result.replace('^','**')
   result = result.replace('-1','((-)(1))')
   print (result)

   try:
       result = str(eval(result))
       c.send(str(eval(result)).encode()) 
       break 
   except ZeroDivisionError:
       print(err)
       c.send(str(err).encode()) 
   except NameError:
       print(Error)
       c.send(str(Error).encode()) 
   except SyntaxError:
       print(Error)
       c.send(str(Error).encode())
   
                  
  


 
