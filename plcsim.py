import socket
import random
import time

def generate_sensor_data():
    # Simulate sensor data
    return random.uniform(0, 100)  # Random value between 0 and 100

def send_data_to_scada(sensor_data, scada_host, scada_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((scada_host, scada_port))
        s.sendall(str(sensor_data).encode())

def plc_simulator():
    scada_host = '10.0.0.2'  # IP of the SCADA system
    scada_port = 12345       # Port for SCADA communication

    while True:
        sensor_data = generate_sensor_data()
        print(f"Generated sensor data: {sensor_data}")
        send_data_to_scada(sensor_data, scada_host, scada_port)
        time.sleep(2)  # Adjust as needed

if __name__ == "__main__":
    plc_simulator()
