"""Tests two clients."""
import pytest
from unittest.mock import patch, MagicMock
from src.client import Client
from src.protocol import ChatProto

class ChatProtoException(Exception):
    pass

TIMEOUT = 2

def test_client_sends_register(server):
    with patch("json.dumps") as mock_json_dumps, \
        patch("selectors.DefaultSelector.register", side_effect=MagicMock) as mock_register, \
        patch("socket.socket.send", side_effect=MagicMock) as mock_send_msg, \
        patch("fcntl.fcntl") as mock_fcntl:
        
        mock_json_dumps.return_value = '{"command": "register", "user": "Bar"}'
        c = Client("Bar")
        c.connect()
        
        assert mock_json_dumps.call_count >= 1
        mock_json_dumps.assert_called_with({"command": "register", "user": "Bar"})

        assert mock_send_msg.call_count == 1
        mock_send_msg.assert_called_once_with(b'\x00&{"command": "register", "user": "Bar"}')