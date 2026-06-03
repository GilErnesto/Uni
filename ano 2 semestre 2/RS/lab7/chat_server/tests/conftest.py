"""Server."""
import pytest
import time
import threading

from src.server import Server

@pytest.fixture(scope="session")
def server():
    """Fixture to start the server in a separate thread."""   

    def _server():
        print("Starting server...")
        s = Server()
        s.loop()

    server_thread = threading.Thread(target=_server, daemon=True)
    server_thread.start()
    
    time.sleep(1)  # Give the server some time to start
    yield 