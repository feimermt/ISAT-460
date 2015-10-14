

import socket 
import sys              # Import socket module

                                 



while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         

    host = str(sys.argv[1])                #socket.gethostname()
    port = int(sys.argv[2])         # Reserve a port for your service.

    server = (host,port)
    print (server)

    cmd = input("Please Enter an Equation:")            

    
    s.sendto(cmd.encode(),server)  


                                   


    ans, server = s.recvfrom(1024)
    ans = ans.decode()                         
    print (ans)



    s.close()
