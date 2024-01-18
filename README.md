# L7 Load Balancer

A simple Layer 7 (Application Layer) load balancer implemented in Python using the Flask framework and multithreading.

## Project Overview

This project aims to build a basic load balancer that distributes HTTP requests across multiple backend servers efficiently. The load balancer is designed to ensure high availability and reliability by dynamically routing traffic to healthy servers. It provides flexibility in handling server additions and removals based on demand.

## Features

- **Round Robin Load Balancing:** Distributes incoming requests among multiple backend servers in a round-robin fashion.
- **Multithreading:** Utilizes Python's multithreading capabilities to handle concurrent connections efficiently.
- **Health Checks:** Periodically checks the health of backend servers using HTTP GET requests. Unhealthy servers are temporarily removed from the list.
- **Dynamic Server Management:** Allows adding or subtracting servers dynamically based on demand.

## Getting Started

- **Setup Virtual Environment:**
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```
   
- **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

  - **Run Backend Servers:**
  ```bash
  python app.py
  ```

  - **Run Load Balancer:**
  ```bash
  python load_balancer.py
  ```

  - **Test Load Balancer:**
  ```bash
   curl http://127.0.0.1:8000
  ```

### Testing
Unit Tests: Includes unit tests for load balancer functionality.
Load Tests: Use tools like Apache Benchmark (ab) to test load balancer performance under different scenarios.

### Contributing
Feel free to contribute by opening issues, suggesting improvements, or submitting pull requests. Your feedback is valuable!

### License
This project is licensed under the MIT License.
