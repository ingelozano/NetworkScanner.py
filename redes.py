import socket
import ipaddress
import threading
import os

# Función para escanear puertos en un host
def scan_ports(target_ip, port_range):
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Puerto {port} Abierto")
        sock.close()

# Función para escanear una subred en busca de hosts activos
def scan_subnet(subnet):
    for ip in ipaddress.IPv4Network(subnet):
        response = os.system(f"ping -c 1 {ip}")
        if response == 0:
            print(f"Host {ip} Activo")
            scan_ports(str(ip), range(1, 1025))

if __name__ == "__main__":
    target_subnet = "coloca tu subred"  # Cambia a la subred que deseas escanear
    target_ports = range(1, 1025)      # Rango de puertos a escanear

    threads = []

    subnet_scanner = threading.Thread(target=scan_subnet, args=(target_subnet,))
    threads.append(subnet_scanner)
    subnet_scanner.start()

    for thread in threads:
        thread.join()

    print("Scaneo Completado")