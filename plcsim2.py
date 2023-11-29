import socket
import random
import time

def simulate_water_flow():
    """Simulates water flow rate."""
    return random.uniform(10, 100)  # Flow rate in liters per second

def simulate_water_pressure():
    """Simulates water pressure."""
    return random.uniform(1, 5)  # Pressure in bars

def valve_control_logic(flow, pressure):
    """Determines valve status based on flow and pressure."""
    if pressure < 2:
        return "Valve OPEN"
    else:
        return "Valve CLOSED"

def send_data_to_scada(data, host, port):
    """Sends data to the SCADA system."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data.encode())

# Configuration for SCADA server
scada_host = '10.0.0.2'  # Replace with the actual IP of the SCADA host
scada_port = 12345

# Main loop
while True:
    flow = simulate_water_flow()
    pressure = simulate_water_pressure()
    valve_status = valve_control_logic(flow, pressure)

    data = f"Flow: {flow:.2f} L/s, Pressure: {pressure:.2f} bar, Valve: {valve_status}"
    send_data_to_scada(data, scada_host, scada_port)
    time.sleep(2)
