import socket               # Import socket module
import sys

if len(sys.argv) !=5: 
   print (" The server is running! Enter The Equation on the Client side. " )
  
else: 
   print("Error too many arguments")
   exit()	
host = str(sys.argv[1])
port = int(sys.argv[2])
server = (host,port)
err = "Error"
divide ="DivBy0"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))      


while True:
 
   result,server = s.recvfrom(1024)
   client = server
   result = result.decode()
   
   result = result.replace('^','**')
   result = result.replace('-1','((-)(1))')                    
   print (result)
   
   try:
       result = str(eval(result))
       s.sendto((str(eval(result)).encode()),client) 
       
   except ZeroDivisionError:
       print(divide)
       s.sendto((str(divide).encode()),client)
        
   except NameError:
       print(err)
       s.sendto((str(err).encode()),client)
       
   except SyntaxError:
       print(err)
       s.sendto((str(err).encode()),client)
   

   print (result)
   
   s.sendto(result.encode(),client)                   

  


