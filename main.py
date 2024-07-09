import os
import platform
import subprocess
import socket
import colorama

colorama.init()
clear_command = "cls" if os.name == "nt" else "clear"

def clear_screen():
    os.system(clear_command)

def print_info(title, info):
    print(colorama.Fore.GREEN + f"[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"{title}")
    print("")
    for key, value in info.items():
        if isinstance(value, list):
            print(colorama.Fore.YELLOW + f"{key}:")
            for item in value:
                print(colorama.Fore.LIGHTWHITE_EX + f"  {item}")
        else:
            print(colorama.Fore.YELLOW + f"{key}: " + colorama.Fore.LIGHTWHITE_EX + f"{value}")
    print("")

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

def ping_sweep(network):
    live_hosts = []
    print(colorama.Fore.GREEN + f"[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"Pinging hosts in network {network}.0/24...")
    for i in range(1, 255):
        ip = f"{network}.{i}"
        if ping_host(ip):
            live_hosts.append(ip)
            print(colorama.Fore.GREEN + f"[Network Scanner]: " + colorama.Fore.LIGHTWHITE_EX + f"{ip} is up")
        else:
            print(colorama.Fore.RED + f"[Network Scanner]: " + colorama.Fore.LIGHTWHITE_EX + f"{ip} is down")
    return {"Live Hosts": live_hosts}

def port_scan(ip, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    return {"Open Ports": open_ports}

def add_ports():
    global common_ports
    print(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter ports to add (type 'exit' to finish adding):")
    while True:
        new_port = input(colorama.Fore.MAGENTA + "Add Port: " + colorama.Fore.WHITE).strip()
        if new_port.lower() == 'exit':
            break
        elif new_port.isdigit():
            common_ports.append(int(new_port))
            print(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"Added port: {new_port}")
        else:
            print(colorama.Fore.RED + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Invalid port. Please enter a valid number.")
    print(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Port addition finished.")

common_ports = [
    21, 22, 23, 25, 53, 80, 110, 123, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080
]

def main():
    while True:
        clear_screen()
        print(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Choose an option (type 'exit' to quit):")
        print("")
        print(colorama.Fore.YELLOW + "1 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Run Ping Sweep")
        print(colorama.Fore.YELLOW + "2 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Run Port Scan")
        print(colorama.Fore.YELLOW + "3 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "List of Common Ports")
        print(colorama.Fore.YELLOW + "4 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Add Ports")
        print("")

        choice = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE).strip()

        if choice == '1':
            network = input(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the network (e.g., 192.168.1): " + colorama.Fore.WHITE).strip()
            info = ping_sweep(network)
            print_info("Ping Sweep Results", info)
        elif choice == '2':
            ip = input(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the IP address: " + colorama.Fore.WHITE).strip()
            info = port_scan(ip, common_ports)
            print_info("Port Scan Results", info)
        elif choice == '3':
            print_info("Common Ports", {"Common Ports": common_ports})
        elif choice == '4':
            add_ports()
        elif choice.lower() == 'exit':
            break
        else:
            print(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.RED + "Invalid choice, please try again.")
        
        input(colorama.Fore.GREEN + "[Network Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")

if __name__ == "__main__":
    main()
