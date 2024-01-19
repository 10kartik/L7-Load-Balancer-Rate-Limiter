from flask import Flask, redirect
from itertools import cycle
from threading import Lock, Thread
import requests
import time

app = Flask(__name__)

# List of backend servers
backend_servers = ["http://127.0.0.1:5000", "http://127.0.0.1:5001", "http://127.0.0.1:5002"]

# Lock for thread safety
lock = Lock()

# List to store the healthy servers
healthy_servers = backend_servers.copy()

# Cycle through the list of healthy servers in a round-robin fashion
server_cycle = cycle(healthy_servers)

# Function to perform health checks in the background
def health_check():
    global healthy_servers
    while True:
        time.sleep(3)  # Health check every 3 seconds
        with lock:
            new_healthy_servers = []
            print('====================')
            for server in backend_servers:
                try:
                    print('Checking health of server {}'.format(server))
                    response = requests.get(server + '/health', timeout=2)
                    if response.status_code == 200:
                        new_healthy_servers.append(server)
                except requests.RequestException:
                    print('Server {} is unhealthy'.format(server))
                    pass  # Server is considered unhealthy if there's an exception
            healthy_servers = new_healthy_servers
            print('healthy servers: {}'.format(healthy_servers))
            print('====================')

# Start the health check thread as a daemon
health_check_thread = Thread(target=health_check, daemon=True)
health_check_thread.start()

@app.route('/')
def load_balancer():
    with lock:
        if not healthy_servers:
            return "No healthy servers available", 503
        next_server = next((s for s in server_cycle if s in healthy_servers), None)
    return redirect(next_server)

if __name__ == '__main__':
    print('Running load balancer on port 8000')
    print('Supporting servers: {}'.format(backend_servers))
    app.run(port=8000)
