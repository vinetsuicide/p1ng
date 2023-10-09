import requests
import socket
import sys
from colorama import Fore, Style

def check_website(target):
    try:
        ip_address = socket.gethostbyname(target)
        response = requests.get(f"http://{ip_address}")
        if response.status_code == 200:
            print(f"{Fore.GREEN}[*]The website {target} with IP {ip_address} is UP!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[*]The website {target} with IP {ip_address} is DOWN with status code {response.status_code}.{Style.RESET_ALL}")
    except socket.gaierror:
        print(f"{Fore.YELLOW}[*]Could not resolve {target}. Please check the spelling and try again.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.YELLOW}[*]An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}[!]Usage: python3 ping.py <domain/ip>{Style.RESET_ALL}")
    else:
        target = sys.argv[1]
        check_website(target)

