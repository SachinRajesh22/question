import socket
import threading

PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', PORT))

name = input("Enter your name: ")
client.send(name.encode())

print("\nConnected to Chat Server")
print("Start chatting...\n")


# Function to receive messages
def receive():
    while True:
        try:
            data = client.recv(1024)

            if not data:
                print("Disconnected from Server")
                break

            print(data.decode())

        except:
            break


# Run receiver in a separate thread
threading.Thread(target=receive, daemon=True).start()

# Send messages
while True:
    message = input()

    if message.lower() == "exit":
        break

    client.send(message.encode())

client.close()