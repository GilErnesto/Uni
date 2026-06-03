import pytest
from unittest.mock import patch
from mock import MagicMock

from src.server import Server


class ChatProtoException(Exception):
    pass


def test_server():
    """Test that the server used ChatProto methods."""

    def fail(s):
        raise ChatProtoException()

    with patch("socket.socket") as mock_socket, patch(
        "selectors.DefaultSelector.select", side_effect=ChatProtoException
    ) as mock_selector, patch("selectors.DefaultSelector.register", side_effect=MagicMock) as mock_register:
        s = Server()

        with pytest.raises(ChatProtoException):
            s.loop()

        assert mock_socket.call_count == 1
        assert mock_selector.call_count == 1
        assert mock_register.call_count == 1
