"""Protocol for chat server - Computação Distribuida Assignment 1."""
import json
from datetime import datetime
from socket import socket


class Message:
    """Message Type."""

    
class JoinMessage(Message):
    def __init__(self, channel):
        self.command= "join"
        self.channel= channel

    def __str__(self):
        return json.dumps({
            "command": self.command,
            "channel": self.channel
        })

class RegisterMessage(Message):
    def __init__(self, user):
        self.command= "register"
        self.user= user

    def __str__(self):
        return json.dumps({
            "command": self.command,
            "user": self.user
        })
    
class TextMessage(Message):
    def __init__(self, message, ts=None):
        self.command= "message"
        self.message= message
        self.ts= ts if ts is not None else int(datetime.now().timestamp())

    def __str__(self):
        return json.dumps({
            "command": self.command,
            "message": self.message,
            "ts": self.ts
        })

class ChatProto:

    @classmethod
    def register(cls, username: str) -> RegisterMessage:
        return RegisterMessage(username)

    @classmethod
    def join(cls, channel: str) -> JoinMessage:
        return JoinMessage(channel)

    @classmethod
    def message(cls, message: str, channel: str = None) -> TextMessage:
        return TextMessage(message)

    @classmethod
    def send_msg(cls, connection: socket, msg: Message):
        msg_bytes= str(msg).encode("utf-8")
        size= len(msg_bytes).to_bytes(2, byteorder="big")
        conn.sendall(size + msg_bytes)
        
    @classmethod
    def recv_msg(cls, connection: socket) -> Message:
        header= cls._recv_all(conn, 2)
        if not header:
            return None

        length= int.from_bytes(header, byteorder="big")
        data= cls._recv_all(conn, length)

        if data is None or len(data) != length:
            raise ChatProtoBadFormat(data)

        try:
            obj= json.loads(data.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise ChatProtoBadFormat(data)

        if "command" not in obj:
            raise ChatProtoBadFormat(data)

        command= obj["command"]

        if command== "register":
            if "user" not in obj:
                raise ChatProtoBadFormat(data)
            return RegisterMessage(obj["user"])

        elif command== "join":
            if "channel" not in obj:
                raise ChatProtoBadFormat(data)
            return JoinMessage(obj["channel"])

        elif command== "message":
            if "message" not in obj or "ts" not in obj:
                raise ChatProtoBadFormat(data)
            return TextMessage(obj["message"], obj["ts"])

        else:
            raise ChatProtoBadFormat(data)

class ChatProtoBadFormat(Exception):

    def __init__(self, original_msg: bytes=None) :
        self._original = original_msg

    @property
    def original_msg(self) -> str:
        return self._original.decode("utf-8")
