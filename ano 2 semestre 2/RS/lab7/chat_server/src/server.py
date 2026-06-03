import logging
import socket
import selectors

from src.protocol import (
    ChatProto,
    ChatProtoBadFormat,
    RegisterMessage,
    JoinMessage,
    TextMessage,
)

logging.basicConfig(filename="server.log", level=logging.DEBUG)


class Server:

    def __init__(self):
        self.selector = selectors.DefaultSelector()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("localhost", 8080))
        self.server_socket.listen()
        self.server_socket.setblocking(False)
        self.selector.register(self.server_socket, selectors.EVENT_READ, self.accept)

        self.clients = {}

    def accept(self, sock):
            conn, addr = sock.accept()
            conn.setblocking(False)

            self.clients[conn] = {
                "username": None,
                "channel": "main"
            }

            self.selector.register(conn, selectors.EVENT_READ, self.read)


