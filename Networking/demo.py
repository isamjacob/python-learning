# Nttworking With Python

import socket 
import requests
import urllib.request

# Get your hostname

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"Local IP: {local_ip}")

# DNS lookup

google_ip = socket.gethostbyname("google.com")
print(f"Google IP: {google_ip}")

github_ip = socket.gethostbyname("github.com")
print(f"GitHub IP: {github_ip}")

# HTTP Request

print("\n HTTP Request")
response = requests.get("https://httpbin.org/get")
print(f"Status: {response.status_code}")
print(f"Headers: {dict(list(response.headers.items())[:3])}")

# Check if port is open
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex
    sock.close()
    return result == 0

print("\n Port Checker")
print(f"Google port 80: {check_port('google.com', 80)}")
print(f"Google port 443: {check_port('google.com', 443)}")
print(f"Local port 8000: {check_port('localhost', 8000)}")

# Simple HTTP server
print("\n Making HTTP request")
response = requests.get("https://api.github.com")
print(f"GitHub API status: {response.status_code}")
print(f"Rate limit remaining: {response.headers.get('X-RateLimit-Remaining')}")

# IP Information
try:
    response = requests.get("https://httpbin.org/ip", timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"\nYour public IP: {data['origin']}")
    else:
        print(f"Failed: {response.status_code}")
except Exception as e:
    print(f"Could not get IP: {e}")