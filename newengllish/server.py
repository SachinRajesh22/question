import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('localhost',12345))
print("udp waiting..")
data,addr=server.recvfrom(1024)
data=data.decode()

print("recieved sentence : ",data)

dict = {
   "tbh" : "to be honest",
   "tbf": "to be fair",
   "idk": "I don't know",
   "idc": "I don't care",
   "nvm": "never mind",
   "ig" : "i guess",
   "atm": "at the moment",
   "irl": "in real life",
   "lol": "laughing out loud",
   "asap": "as soon as possible",
   "omg": "oh my God",
   "ttyl": "talk to you later"
}



words=data.split()
result=[]
for word in words:
  result.append(dict.get(word.lower(),word))

translated=" ".join(result)

server.sendto(translated.encode(),addr)

server.close()