import socket


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server = ('localhost', 12345)

# Input filename
filename = input("Enter File Name: ")

# Send filename
client.sendto(filename.encode(), server)

# Receive response
data, addr = client.recvfrom(1024)

# Display response
print("\n=====================================")
print("Response Received From Server")
print("=====================================\n")

print(data.decode())

client.close()