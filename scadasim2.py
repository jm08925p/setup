import socket
import threading

def handle_client_connection(client_socket):
    """Handles the client connection in a separate thread."""
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"SCADA received data: {data}")
            # Additional processing logic can be added here
    finally:
        client_socket.close()

def start_scada_server(host, port):
    """Starts the SCADA server and listens for incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)  # Adjust the number of queued connections
    print(f"SCADA server listening on {host}:{port}")

    try:
        while True:
            client_sock, address = server.accept()
            print(f"Accepted connection from {address}")
            client_handler = threading.Thread(
                target=handle_client_connection,
                args=(client_sock,)
            )
            client_handler.start()
    finally:
        server.close()

# Configuration for SCADA server
scada_host = '0.0.0.0'  # Listen on all network interfaces
scada_port = 12345

# Start the SCADA server
start_scada_server(scada_host, scada_port)
