import time
import socket

def simulate_network_activity():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('example.com', 80))  # Connect to an external server
        s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
        response = s.recv(1024)
        print(f"Received data: {response[:100]}...")  # Print the first 100 bytes

def main():
    print("Starting network activity")
    for _ in range(5):  # Perform 5 network requests
        simulate_network_activity()
        time.sleep(2)  # Wait 2 seconds between each request

    print("Network activity complete")
    time.sleep(10)  # Keep script running for 10 more seconds to allow profiling

if __name__ == "__main__":
    main()


import time
import socket
import ssl
import logging
from typing import Dict, Optional
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('network_activity.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)