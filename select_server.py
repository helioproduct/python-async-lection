import socket
import select

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(("localhost", 16000))
server_sock.listen(5)

to_monitor = []


def accept_conn(server_sock):
    client_sock, addr = server_sock.accept()
    print("Connected", addr)
    to_monitor.append(client_sock)


def respond(client_sock):
    data = client_sock.recv(4096)
    if data:
        client_sock.send(data.decode().upper().encode())
    else:
        print("Client closed")
        client_sock.close()
        to_monitor.remove(client_sock)


def event_loop():
    while True:
        ready_to_read, _, _ = select.select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_sock:
                accept_conn(sock)
            else:
                respond(sock)


if __name__ == "__main__":
    to_monitor.append(server_sock)
    event_loop()
