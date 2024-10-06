import subprocess

# Configuration for static IP
interface = "wlan0"  # Change this to your active interface
static_ip = "192.168.1.100"  # Your desired static IP
netmask = "255.255.255.0"  # Subnet mask
gateway = "192.168.1.1"  # Your gateway (usually your router's IP)
dns1 = "8.8.8.8"  # Primary DNS
dns2 = "8.8.4.4"  # Secondary DNS (optional)

# Commands to set static IP
commands = [
    f"ip addr add {static_ip}/{netmask} dev {interface}",
    f"ip link set {interface} up",
    f"ip route add default via {gateway}",
    f"echo 'nameserver {dns1}' > /etc/resolv.conf",
    f"echo 'nameserver {dns2}' >> /etc/resolv.conf"
]

# Execute each command
for command in commands:
    subprocess.run(command, shell=True, check=True)

print("Static IP configured successfully.")
