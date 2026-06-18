import socket
from datetime import datetime

target = input("Enter target IP or hostname: ")

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}

open_ports = []

print(f"\nScanning {target}...")
start = datetime.now()

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        open_ports.append((port, common_ports[port]))

    sock.close()

end = datetime.now()

print("\n===== Security Report =====")
print("Target:", target)

if open_ports:
    print("\nOpen Ports:")
    for port, service in open_ports:
        print(f"{port} - {service}")

        if service == "Telnet":
            print("  Warning: Telnet is insecure.")
        elif service == "FTP":
            print("  Warning: FTP transmits data unencrypted.")
else:
    print("No common open ports detected.")

print("\nScan Duration:", end - start)