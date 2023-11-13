import os
import time
import socket

SLEEP_SECONDS = int(os.getenv('SLEEP_SECONDS', 5))
RUN_SECONDS = int(os.getenv('RUN_SECONDS', 300)) 
RUN_FOR_EVER = os.getenv('RUN_FOR_EVER', 'no')  

def print_time_hostname_ip():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(f"I am Alive Amigo - {current_time}, Host: {host_name}, IP: {ip_address}")

if RUN_FOR_EVER.lower() == "yes":
    while True:
        print_time_hostname_ip()
        time.sleep(SECONDS_TO_SLEEP)
else:
    SEC = 0
    while SEC < RUN_SECONDS:
        print_time_hostname_ip()
        time.sleep(SLEEP_SECONDS)
        SEC = SEC + 5

