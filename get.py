import requests
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_proxies(api_urls, file_name):
    all_proxies = set()

    for url in api_urls:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                proxies = response.text.splitlines()
                all_proxies.update(proxies)
                print(f'[HenryNET-SCAN] Successfully Scanning !')
            else:
                print(f'[HenryNET-SCAN] Error from Scanning')
        except Exception as e:
            print(f'[HenryNET-SCAN] Error from Scanning')

    with open(file_name, 'w') as file:
        for proxy in sorted(all_proxies):
            file.write(proxy + '\n')

    print(f'Proxy saved to file [{file_name}]')

def main():
    clear_screen()
    print("""
               [!] SCANNING PROXY BY [HenryNET-2006]
               [#] API SPACE
    """)
    print("(1) [SCANNING PROXY VIETNAM]")
    print("(2) [SCANNING ALL COUNTRIES]")

    choice = input("Enter Choice: ")

    if choice == '1':
        api_urls = [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=30000&country=VN',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=30000&country=VN',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=30000&country=VN',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=30000&country=VN',
            'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=VN&city=all&port=all&type=all&anonymity=all&state=all&need=all',
            'https://api.openproxylist.xyz/v1/get?country=VN',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=VN&ssl=all&anonymity=anonymous'

        ]
        fetch_proxies(api_urls, 'vn.txt')
    elif choice == '2':
        api_urls = [
            'https://api.openproxylist.xyz/v1/get?country=VN',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
            'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=VN&city=all&port=all&type=all&anonymity=all&state=all&need=all',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=anonymous',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=1000&country=all',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=300&country=all',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=500&country=all',
            'https://api.proxyscrape.com/?request=displayproxies&proxytype=https',
            'http://worm.rip/http.txt',
            'http://alexa.lr2b.com/proxylist.txt',
            'https://api.openproxylist.xyz/http.txt',
        ]
        fetch_proxies(api_urls, 'all.txt')
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
