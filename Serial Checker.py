import os
import subprocess
import sys
from colorama import Fore, Style
from pystyle import Write, Colors

# Function to check if a package is installed
def is_package_installed(package_name):
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', package_name])
        return True
    except subprocess.CalledProcessError:
        return False

# Install or upgrade required packages
def install_required_packages(packages):
    for package in packages:
        if not is_package_installed(package):
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        else:
            print(f"{package} is already installed. Checking for updates...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

# Function to execute a command and print output
def run_command_and_print_output(command, description):
    Write.Print(f"{Fore.MAGENTA}[+] {description}:{Style.RESET_ALL}\n", Colors.purple_to_blue, interval=0.001)
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing command: {e}")

# Main function
def main():
    required_packages = ['fade', 'colorama', 'pystyle']
    install_required_packages(required_packages)

    gui = """
    ╔══════════════════════════════════╗ ╔════════════════════════╗
    ║  ______ __         ____          ║ ║                        ║
    ║ |   __ \  |.-----.|_   | .--.--. ║ ║ [discord.gg/plo1xmodz] ║
    ║ |    __/  ||  _  | _|  |_|_   _| ║ ║                        ║
    ║ |___|  |__||_____||______|__.__| ║ ║         [Plo1x]        ║
    ║                                  ║ ║                        ║
    ╚══════════════════════════════════╝ ╚════════════════════════╝
    ╔═════════════════════════════════════════════════════════════╗
    ║                    [Plo1x Serial Checker]                   ║
    ║            [!] https://discord.gg/plo1xmodz [!]             ║
    ╚═════════════════════════════════════════════════════════════╝
    ╔═════════════════════════════════════════════════════════════╗
    ║                  [All credits to @jddrizdog]                ║
    ╚═════════════════════════════════════════════════════════════╝
    """
    
    os.system("mode con: cols=90 lines=56")
    os.system("title Plo1x Modz Serial Checker ^| Press any key to refresh")

    while True:
        os.system("cls")
        Write.Print(f"\n{gui}\n", Colors.purple_to_blue, interval=0.001)
        
        Write.Print("[</>] Baseboard\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic baseboard get serialnumber")
        
        Write.Print("[</>] Mac\n", Colors.red_to_purple, interval=0.001)
        os.system("""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""")
        
        Write.Print("[</>] CPU\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic cpu get processorid")
        
        Write.Print("[</>] GPU\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic PATH Win32_VideoController GET Description,PNPDeviceID")
        
        Write.Print("[</>] DISK DRIVE\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic diskdrive get serialnumber")
        
        Write.Print("[</>] MotherBoard\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic baseboard get serialnumber")
        
        Write.Print("[</>] RAM\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic memorychip get serialnumber")
        
        Write.Print("[</>] Bios\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic bios get serialnumber")
        
        Write.Print("[</>] smBios\n", Colors.red_to_purple, interval=0.001)
        os.system("wmic csproduct get uuid")


        os.system("pause >nul")

if __name__ == "__main__":
    main()
