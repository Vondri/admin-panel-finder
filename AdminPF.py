__AUTHOR__ = "Vondri"
__VERSION__ = "1.0.0"
__GITHUB__ = "https://github.com/Vondri"

import argparse
import os
import sys
import requests
import random 

parser = argparse.ArgumentParser(description='Python Admin Panel Finder.')
parser.add_argument('-u', '--url', help='Type URL of website to scan.', required=True)
parser.add_argument('-af','--AdminFile', help='Path to text file that constains urls to admin panel.', required=True)
parser.add_argument('-p', '--proxy', help="Path to file with proxies", required=False)
args = parser.parse_args()
target = args.url
adminPath = args.AdminFile
proxyPath = args.proxy


if sys.platform.startswith == "win":
    os.system('cls')
else: 
    os.system('clear')

if sys.version_info[0] > 3:
    print("Script run on Python 3.x! Update python {0}.{1} -> 3.x".format(sys.version_info[0], sys.version_info[1]))

print(f'''
\033[1m\033[38;5;21m █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗    ██████╗  █████╗ ███╗   ██╗███████╗██╗         ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ \033[0m
\033[1m\033[38;5;27m██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║    ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║         ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗\033[0m
\033[1m\033[38;5;33m███████║██║  ██║██╔████╔██║██║██╔██╗ ██║    ██████╔╝███████║██╔██╗ ██║█████╗  ██║         █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝\033[0m
\033[1m\033[38;5;39m██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║    ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║         ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗\033[0m
\033[1m\033[38;5;45m██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║    ██║     ██║  ██║██║ ╚████║███████╗███████╗    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║\033[0m
\033[1m\033[38;5;51m╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝\033[0m
\t\t    \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mAuthor:{__AUTHOR__} \033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mVersion: {__VERSION__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m] \033[4m\033[38;5;164mGithub: {__GITHUB__}\033[0m \033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m

\033[38;5;245mAdmin list path: \033[0m{adminPath}''')

if 'http://' and 'https://' not in target:
    target = 'http://'+target

if len(target) <= 8: 
    print('\033[1m\033[38;5;9mThe url is too short!')
    sys.exit(0)

proxies = []

if proxyPath:
    try:
        pl = open(proxyPath, 'r')
    except FileNotFoundError:
        print('\033[1m\033[38;5;9mProxy file was not found!\033[0m')
    proxyList = pl.readlines()    
    for proxy in proxyList:
        proxy = proxy.strip().split()
        if proxy[0].lower() == 'http' and 'https':
            proxies.append(f'http://{proxy[1]}:{proxy[2]}')
        if proxy[0].lower() == 'socks4':
            proxies.append(f'socks4://{proxy[1]}:{proxy[2]}')
        if proxy[0].lower() == 'socks5':
            proxies.append(f'socks5://{proxy[1]}:{proxy[2]}')

print(f'\033[38;5;245mTARGET:\033[0m {target} [ ]', end='\r')
try:
    req = 0
    proxy = random.choice(proxies)
    if proxyPath:
        req = requests.get(target, proxies={'http': proxy, 'https': proxy})
    else:
         rep = requests.get(target)
    if(req.status_code == 200):
        print(f'\033[38;5;245mTARGET:\033[0m {target} [\033[38;5;10m+\033[0m]')
        print(f'\033[38;5;245mPROXY: \033[0m{proxy}')        
except Exception as e:
    print(f'\033[38;5;245mTARGET:\033[0m {target} [\033[38;5;9m-\033[0m]')
    print('\033[1m\033[38;5;9mThe link could not be opened!\033[0m')
    print(e)
    sys.exit(0)

try:
    file = open(adminPath, 'r')
    urls = file.readlines()
    i = 0
    print('\033[38;5;245m====================================\033[0m')
    for url in urls:
        url = target+'/'+url.strip()
        print(f'{i}/{len(urls)} {url} [ ]', ' '*20, end='\r')
        try:
            req = requests.get(url)
            if(req.status_code == 200):
                print(f'\033[38;5;245m{i}/{len(urls)}\033[0m {url} [\033[38;5;10m+\033[0m]', ' '*20)
            else:
                print(f'\033[38;5;245m{i}/{len(urls)}\033[0m {url} [\033[38;5;9m-\033[0m]', ' '*20, end='\r')
        except requests.exceptions.ConnectionError:
            print(f'\033[38;5;245m{i}/{len(urls)}\033[0m {url} [\033[38;5;9m-\033[0m]', ' '*20, end='\r')
        i += 1
    print('\033[38;5;245m====================================\033[0m', ' '*50)
except FileNotFoundError:
    print("\033[1m\033[38;5;9mAdmin pages file was not found!\033[0m")
    sys.exit(0)
except KeyboardInterrupt:
    sys.exit(0)