# chat_server

Skeleton repository for the TCP Chat Server project — Redes e Serviços.

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Remember to activate the environment every time you open a new terminal session.

## Running

Open three terminals (all with the virtual environment activated):

```bash
# Terminal 1 — server
$ python3 server.py

# Terminal 2 — first client
$ python3 foo.py

# Terminal 3 — second client
$ python3 bar.py
```

## Testing

```bash
$ pytest
```
