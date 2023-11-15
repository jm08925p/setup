import socket

def start_scada_server(port):
    host = ''  # Bind to all interfaces
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("SCADA system waiting for data...")
    conn, addr = s.accept()
    print(f"Connected to PLC at {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        # Simulate data integrity attack
        if is_attack_scenario():
            data = alter_data(data)

        print(f"Received data from PLC: {data}")

    conn.close()

def is_attack_scenario():
    # Define your logic to simulate an attack scenario
    return False  # Change to `True` to simulate an attack

def alter_data(data):
    # Alter the data to simulate an attack
    return f"Altered Data: {data}"

if __name__ == "__main__":
    scada_port = 12345
    start_scada_server(scada_port)
