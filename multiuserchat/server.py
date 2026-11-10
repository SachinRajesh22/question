import socket
import select

PORT = 9000
MAX_CLIENTS = 10

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('0.0.0.0', PORT))
server.listen(MAX_CLIENTS)

clients = {}

print("=====================================")
print(" Multi User Chat Server Started")
print(" Port:", PORT)
print("=====================================")

while True:
    sockets = [server] + list(clients.keys())

    readable, _, _ = select.select(sockets, [], [])

    for sock in readable:

        # New client connection
        if sock == server:
            conn, addr = server.accept()

            name = conn.recv(1024).decode().strip()

            clients[conn] = name
            print(name, "Connected")

        # Existing client sends message
        else:
            data = sock.recv(1024)

            if not data:
                print(clients[sock], "Disconnected")
                del clients[sock]
                sock.close()

            else:
                message = clients[sock] + " : " + data.decode()

                print(message, end="")

                # Broadcast to all other clients
                for client in clients:
                    if client != sock:
                        client.send(message.encode())