import socket

def start_scada_server(host, port):
    """Starts the SCADA server to listen for incoming data."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    return conn, addr

def process_plc_data(data):
    """Processes data received from the PLC."""
    print(f"SCADA received data: {data}")
    if "Valve OPEN" in data:
        print("Alert: Valve opened due to low pressure")

# Configuration for SCADA server
scada_host = ''  # Empty string means listening on all interfaces
scada_port = 12345

# Start the SCADA server
conn, addr = start_scada_server(scada_host, scada_port)
print(f"SCADA server started, connected to {addr}")

# Main loop
try:
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        process_plc_data(data)
finally:
    conn.close()
