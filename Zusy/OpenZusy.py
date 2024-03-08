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
    process = run(nmap_command, shell=True)
    print(process.stdout.decode())
    input("\nPress Enter to go back...")
    main_menu()

def open_metasploit():
    clear_screen()
    process = run("msfconsole -q", shell=True)

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
    print("[1] Nmap Scan\n[2] Open Metasploit\n[3] Social Engineering\n[99] Exit\n")
    choice = input("Zusy ~# ")

    if choice == "1":
        nmap_scan()
    elif choice == "2":
        open_metasploit()
    elif choice == "3":
        social_engineering()
    elif choice == "99":
        print("\nThanks For Using!!!")
    else:
        print("\nError: Please Try Again", color="red")
        main_menu()

main_menu()
