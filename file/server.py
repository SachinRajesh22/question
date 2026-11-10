import socket
import os

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('localhost',12345))
print("udp server waiting...")

while True:
  
  data, addr = server.recvfrom(1024)
  filename = data.decode()
  
  pid=os.fork()
  
  if pid==0:
    child_pid=os.getpid()
    
    try:
      with open(filename,'r') as fp:
        content=fp.read()
      
      result="handled by server pid" + str(child_pid) +"\n\n"
      result+=content
      
    except FileNotFoundError:
      result = "Handled by Server PID : " + str(child_pid)
      result += "\n\nRequested File Not Found."
    
    server.sendto(result.encode(), addr)

    print("Request for", filename, "served by PID", child_pid)

    os._exit(0)