"""Tests for the chat protocol."""
import pytest
from src.protocol import (
    ChatProto,
    TextMessage,
    JoinMessage,
    RegisterMessage,
    ChatProtoBadFormat,
)

from freezegun import freeze_time


@freeze_time("Mar 16th, 2021")
def test_protocol():
    p = ChatProto()

    assert str(p.register("student")) == '{"command": "register", "user": "student"}'

    assert str(p.join("#cd")) == '{"command": "join", "channel": "#cd"}'

    assert (
        str(p.message("Hello World"))
        == '{"command": "message", "message": "Hello World", "ts": 1615852800}'
    )


class mock_socket:
    def __init__(self, content):
        self.g = self.gen_stream(content)

    def gen_stream(self, content):
        yield len(content).to_bytes(2, "big")
        yield content

    def recv(self, n):
        return next(self.g)


def test_recv():

    assert isinstance(
        ChatProto.recv_msg(mock_socket(b'{"command": "register", "user": "student"}')),
        RegisterMessage,
    )

    assert isinstance(
        ChatProto.recv_msg(mock_socket(b'{"command": "join", "channel": "#cd"}')),
        JoinMessage,
    )
    assert isinstance(
        ChatProto.recv_msg(
            mock_socket(
                b'{"command": "message", "message": "Hello World", "ts": 1615852800}'
            )
        ),
        TextMessage,
    )

    with pytest.raises(ChatProtoBadFormat):
        ChatProto.recv_msg(mock_socket(b"Hello World"))
