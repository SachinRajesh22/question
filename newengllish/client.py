import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sentence=input("enter sentence: ")

client.sendto(sentence.encode(),('localhost',12345))
result,addr=client.recvfrom(1024)
print(result.decode())
client.close()