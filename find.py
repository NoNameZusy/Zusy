import subprocess
import importlib.util
import netifaces
from scapy.all import ARP, Ether, srp

def install_package(package_name):
    try:
        subprocess.check_call(["apt", "install", "-y", package_name])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")

def check_dependencies():
    required_packages = ["nmap", "scapy"]
    installed_packages = []
    missing_packages = []
    for package in required_packages:
        spec = importlib.util.find_spec(package)
        if spec is None:
            missing_packages.append(package)
        else:
            installed_packages.append(package)
    return installed_packages, missing_packages

def install_dependencies():
    installed_packages, missing_packages = check_dependencies()
    if missing_packages:
        for package in missing_packages:
            print(f"{package} is not installed. Installing...")
            install_package(package)

def get_local_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        try:
            if interface != "lo":
                iface_details = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
                return iface_details['addr']
        except:
            pass
    return None

def scan_network(ip):
    arp_request = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp_request
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

def get_wifi_gateway():
    try:
        output = subprocess.check_output(["ip", "route"])
        output = output.decode("utf-8").split("\n")
        for line in output:
            if "default via" in line:
                return line.split()[2]
    except subprocess.CalledProcessError:
        pass
    return None

def display_menu(devices, local_ip, wifi_gateway):
    print("Devices in the network:")
    print("No.\tIP Address\t\tMAC Address\t\tHostname")
    print("-----------------------------------------------------------------")
    for idx, device in enumerate(devices, start=1):
        hostname = device.get('hostname', 'Unknown')
        print(f"{idx}.\t{device['ip']}\t{device['mac']}\t{hostname}")
    print("-----------------------------------------------------------------")

    if wifi_gateway:
        print("\nWi-Fi Gateway IP Address:")
        print(wifi_gateway)
    else:
        print("\nWi-Fi Gateway IP Address: Unknown")


def main():
    install_dependencies()

    local_ip = get_local_ip()
    if local_ip:
        print("Local IP Address:", local_ip)
        wifi_gateway = get_wifi_gateway()
        network_ip = local_ip.split('.')
        network_ip[-1] = '0/24'
        network_ip = '.'.join(network_ip)
        devices = scan_network(network_ip)
        display_menu(devices, local_ip, wifi_gateway)
    else:
        print("Failed to retrieve local IP address.")

if __name__ == "__main__":
    main()
