import socket, threading


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[ip] = 'Listening'
    except:
        output[ip] = ''

def scan_ports(host_ip, port, delay=0.1):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes
    result = []

    # Spawning threads to scan ports
    for i in range(255):
        t = threading.Thread(target=TCP_connect, args=(host_ip+str(i), port, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(255):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(255):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(255):
        if output[host_ip+str(i)] == 'Listening':
            result.append(host_ip+str(i))
    return result
