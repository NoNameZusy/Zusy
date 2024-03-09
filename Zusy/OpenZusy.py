from subprocess import run, PIPE
import os

def clear_screen():
    os.system('clear')

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
    
def update_kali():
    clear_screen()
    process = run("sudo apt update && sudo apt upgrade", shell=True)    
    
def kali_undercover():
    clear_screen()
    process = run("kali-undercover", shell=True)    
    
def reboot_system():
    clear_screen()
    process = run("sudo reboot", shell=True)    

def social_engineering():
    clear_screen()
    process = run("setoolkit", shell=True)

def main_menu():
    clear_screen()
    logo = """
      ╔════╦╗─╔╦═══╦╗──╔╗
      ╚══╗═║║─║║╔═╗║╚╗╔╝║
      ──╔╝╔╣║─║║╚══╬╗╚╝╔╝
      ─╔╝╔╝║║─║╠══╗║╚╗╔╝─
      ╔╝═╚═╣╚═╝║╚═╝║─║║──
      ╚════╩═══╩═══╝─╚╝──
------{ By No_Name.exe }------
    """
    print(logo)
    print("[1] Nmap Scan\n[2] Open Metasploit\n[3] Social Engineering\n[4] SQL Injection\n[5] Commix\n[6] Restart System\n[7] Become Windows (on/off)\n[8] Upgrade System\n[99] Exit\n")
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
    elif choice == "99":
        print("\nThanks For Using!!!")
    else:
        print("\nError: Please Try Again")
        main_menu()

main_menu()
