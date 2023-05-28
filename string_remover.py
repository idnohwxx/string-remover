import pymem
import pyuac
from colorama import init, Fore
import sys
import os
# Initialising Colorama
init()


def remove():
    try:
        string_to_removed = input(Fore.LIGHTYELLOW_EX + "[*] " + Fore.LIGHTWHITE_EX + "Enter Strings: ")
        address = int(string_to_removed.split()[0], 0)
        length = int(string_to_removed.split("(")[1].split(")")[0], 0)

        pymem.memory.write_string(pymem.process.open(process_id), address, bytes(length))
        print(Fore.GREEN + "[+] " + Fore.LIGHTWHITE_EX + "string removed..")
    except:
        print(Fore.RED + "[+] " + Fore.LIGHTWHITE_EX + "string error!")


class StringRemover:
    def __init__(self):
        if not pyuac.isUserAdmin():
            print(Fore.GREEN + "[+] " + Fore.LIGHTWHITE_EX + "launching as admin...")
            pyuac.runAsAdmin()


if __name__ == "__main__":
    remover = StringRemover()
    print(Fore.GREEN + "[+] " + Fore.LIGHTWHITE_EX + "made by idnohwxx")
    print("\n")
    print(Fore.GREEN + "[+] " + Fore.LIGHTWHITE_EX + "importing libraries...")
    print(Fore.LIGHTYELLOW_EX + "[*] " + Fore.LIGHTWHITE_EX + "1. " + Fore.LIGHTWHITE_EX + "remove string")
    print(Fore.LIGHTYELLOW_EX + "[*] " + Fore.LIGHTWHITE_EX + "2. " + Fore.LIGHTWHITE_EX + "exit")
    choice = input(Fore.GREEN + "[+] " + Fore.LIGHTWHITE_EX + "Enter your choice: ")
    if choice == "1":
        os.system('cls')
        print("\n")
        process_id = int(input(Fore.LIGHTYELLOW_EX + "[*] " + Fore.LIGHTWHITE_EX + "Enter PID: "), 0)
        remove()
    elif choice == "2":
        sys.exit(0)
    else:
        print(Fore.RED + "[+] " + Fore.LIGHTWHITE_EX + "invalid choose. try again.\n")
    while True:
        remove()
