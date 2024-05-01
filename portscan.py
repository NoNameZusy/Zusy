import socket

def port_scan(target_host):
    print("[*] Starting port scan on", target_host)
    for port in range(1, 65536):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((target_host, port))
            if result == 0:
                print("[+] Port {} is open".format(port))
            s.close()
        except KeyboardInterrupt:
            print("\n[*] Exiting due to user interrupt")
            exit()
        except socket.gaierror:
            print("[!] Hostname could not be resolved")
            exit()
        except socket.error:
            print("[!] Couldn't connect to server")
            exit()

def main():
    target_host = input("Enter target IP address: ")
    port_scan(target_host)

if __name__ == "__main__":
    main()
