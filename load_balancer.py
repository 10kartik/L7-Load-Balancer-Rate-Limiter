from flask import Flask, redirect
from itertools import cycle
from threading import Lock

app = Flask(__name__)

# List of backend servers
backend_servers = ["http://127.0.0.1:5000", "http://127.0.0.1:5001", "http://127.0.0.1:5002"]

# Cycle through the list of servers in a round-robin fashion
server_cycle = cycle(backend_servers)

# Lock for thread safety
lock = Lock()

@app.route('/')
def load_balancer():
    with lock:
        next_server = next(server_cycle)
    return redirect(next_server)

if __name__ == '__main__':
    print('Running load balancer on port 8000')
    print('Supporting servers: {}'.format(backend_servers))
    app.run(port=8000)
