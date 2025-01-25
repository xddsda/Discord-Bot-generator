import webbrowser
import os
import time
from colorama import init, Fore, Style

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = r"""
 _____     __     ______     ______     ______     ______     _____    
/\  __-.  /\ \   /\  ___\   /\  ___\   /\  __ \   /\  == \   /\  __-.  
\ \ \ /\ \ \ \ \  \ \___  \  \ \ \____  \ \ \/\ \  \ \  __<   \ \ \ /\ \ 
 \ \____-  \ \_\  \/\_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \____- 
  \/____/   \/_/   \/_____/   \/_____/   \/_____/   \/_/ /_/   \/____/ 
                                                    
"""
    print(Fore.BLUE + logo + Style.RESET_ALL)

def main():
    clear_screen()
    print_logo()

    time.sleep(2)

    discord_link = "https://discord.gg/KeXw4VTy9d"
    webbrowser.open(discord_link)


    thanks_message = """
THANKS FOR JOINING OUR DISCORD !
GRACIAS POR UNIRTE A NUESTRO DISCORD!
"""
    print(Fore.GREEN + thanks_message + Style.RESET_ALL)

if __name__ == "__main__":
    main()
