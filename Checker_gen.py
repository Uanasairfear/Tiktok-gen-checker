from os import system
import os
import asyncio
from typing import List
import aiohttp
import requests
import time
import random
checked = []
webhook = 'webhook here'

username_list = []
proxy_list = []

def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')

def sendwebhook(u):
    embed = {
        "avatar_url": "https://cdn.discordapp.com/attachments/967527324893450250/970271084693819392/image0.jpg",
        "username": "name of webhook",
        "content":u,
        "embeds": [{
            "title": "Name Available:",
            "description": f"[{u}](https://www.tiktok.com/@{u}) is available!",
            "color": 0x000000
        }]
    }
    requests.post(webhook, json=embed)

def usernamegenerator(amount):
        for i in range(amount):
            randomAlphaNum = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz1234567890')) for x in range(26))
            user = ''.join((random.choice(str(randomAlphaNum))) for x in range(4))
            username_list.append(user)
            print(f"[GENNED] {user}")

def proxyscraper():
    r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
    for proxy in r.text.split("\n"):
        proxy = proxy.strip()
        if proxy:
            print(f"[SCRAPED] {proxy}")
            proxy_list.append(proxy)


class Checker:
    def __init__(self, usernames: List[str]):
        self.to_check = usernames

    async def _check(self, session: aiohttp.ClientSession, username: str) -> None:
        
        async with session.head(f'https://www.tiktok.com/@{username}') as response:

            if response.status == 200 and len(username) > 2:
                print('%s[UNAVAILABLE] https://www.tiktok.com/@%s%s' % ('\u001b[31;1m', username, '\u001b[0m'))

            else:
                try:
                    time.sleep(0)
                    headers = {
                        'authority':
                        'www.tiktok.com',
                        'cache-control':
                        'max-age=0',
                        'sec-ch-ua':
                        '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                        'sec-ch-ua-mobile':
                        '?0',
                        'sec-ch-ua-platform':
                        '"Windows"',
                        'upgrade-insecure-requests':
                        '1',
                        'user-agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        'accept':
                        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site':
                        'none',
                        'sec-fetch-mode':
                        'navigate',
                        'sec-fetch-user':
                        '?1',
                        'sec-fetch-dest':
                        'document',
                        'accept-language':
                        'en-US,en;q=0.9',
                        'cookie':
                        'passport_csrf_token_default=41256012c3ba6c4a5f6eff8ffcbf5349; passport_csrf_token=41256012c3ba6c4a5f6eff8ffcbf5349; MONITOR_DEVICE_ID=f0ce74a5-885e-4d02-88c7-2c43798ad27d; MONITOR_WEB_ID=d69eae08-8320-45c7-a34b-4c3e34aa49e3; _gcl_au=1.1.1440710902.1639700638; _ga=GA1.2.328516192.1639700638; _tea_utm_cache_1988={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22ios%22%2C%22utm_campaign%22:%22client_share%22}; tt_csrf_token=rM7oYX6vWhwFFPCKf1dTM_zv; s_v_web_id=verify_kx989i45_IhLTyzHx_3FzG_4dlf_9W49_7LuRS29INVar; d_ticket=0ecf71bd0956a1e552c6f9d00e93da3b02dbd; sid_guard=bd3195b36f7dbe9036998237f66bee14%7C1640366713%7C5184000%7CTue%2C+22-Feb-2022+17%3A25%3A13+GMT; uid_tt=7c7743a01ddbf9ca0b8dac8fc6664e0957a5308710a1e174f2f4ff8e69d27ab5; uid_tt_ss=7c7743a01ddbf9ca0b8dac8fc6664e0957a5308710a1e174f2f4ff8e69d27ab5; sid_tt=bd3195b36f7dbe9036998237f66bee14; sessionid=bd3195b36f7dbe9036998237f66bee14; sessionid_ss=bd3195b36f7dbe9036998237f66bee14; sid_ucp_v1=1.0.0-KDEzN2IxZGI3NWFlNTNkYzM2YTk4ODhkZWZmNTkxZmMxODE4M2RmMWQKIAiFiNLQwJLesGAQ-YSYjgYYswsgDDDn8YWDBjgBQOsHEAMaBm1hbGl2YSIgYmQzMTk1YjM2ZjdkYmU5MDM2OTk4MjM3ZjY2YmVlMTQ; ssid_ucp_v1=1.0.0-KDEzN2IxZGI3NWFlNTNkYzM2YTk4ODhkZWZmNTkxZmMxODE4M2RmMWQKIAiFiNLQwJLesGAQ-YSYjgYYswsgDDDn8YWDBjgBQOsHEAMaBm1hbGl2YSIgYmQzMTk1YjM2ZjdkYmU5MDM2OTk4MjM3ZjY2YmVlMTQ; store-idc=maliva; store-country-code=us; passport_fe_beating_status=true; odin_tt=24c0e42d5ef7bc175cb89b6b4b40bc5486023cc033b66d33c3214e4085ec9fa300e292c7aa7be81a9e39a07d16c493185deb89e18106de19f33abd8f5eca10c5ab9945928f0d9f741fec5dbb06e6b42e; cmpl_token=AgQQAPNSF-RMpbBfljOCJl08-9rsJwcXP4fZYMKyNQ; msToken=xA5dzvoJU1UcSa6kHkJVYXHrQ6Ev5PC_uM_R75A5IhPsNmhAZMCfIeZ96ElaTVXegwcEaRmSwY76kSydqukfbpXDGgpj5AxU4lhkRdO98w_2ICOke42rdZrzRFTnEqgbHGOy2WmXVA==; ttwid=1%7CJgN4OHw957YPRZgxry1GVExeBGYrh_C8ojoMbtiuYpo%7C1640371288%7C782c4960e7f3266e4bfa0df0a7f4ad046e536f394f56fe487ff1a1317e102041; msToken=0gxpqPQyPctVePFZGemyKTg7a6rJrktVMtMivOJXPJYR0DUYX5499YClEBN4AmrMdYnNhTyUhdd8-ZLBIxHxRIj3u1fqNq8n293JLaWQYpYJX14OTzRkfNLEBWZUAKal_eZPld8=; _abck=5068439CECD4980C81ED0CA6AC0EFFCC~-1~YAAQzHAsz1HxaN19AQAAWlTt7gflKN904Aaw8RbDZ03gMiyjcBgEvMz3X3WwCaf9EsRHrWsxz7aurAgQKsefrdBQnh3YTFeSX7OI4+u3pHXC7bY7t3PSHYYui3Ky/iQbCeSD4ME+MDoeSoCfMsFC50tqViuFan/P2oXeqFYpI8czPwtGuOlIkJ9x4xc1Jb9aFeluvMyLZGjMwf6AsHctSyxRhMnqM4wWLC5q+TxdinWM1dQVMWHA1yxdU1xk657b2VZ+xjrBBs6erDcBEOV2dmiaMD7GoRuyQ8rbkkTTGW+qLPIef9R5TWay+B3Lioy/Dp8ZNDI8s+3AUckubgo3YEzxG59cd w8FwOInXt2Zg7K88/Q+S1XrLbtqasOTWaOHXSVw7zAFmRPtZpZw==~-1~-1~-1; ak_bmsc=3A28AE88455C6A72DEA5D1255FE5C410~000000000000000000000000000000~YAAQzHAsz1LxaN19AQAAWlTt7g4meAUk67EpAUqvDZgOqtr9yezmOIwNNPtMs9mLXvsBq14LRRThAY4NlosEmPtbyyBmRbd6CN0mqQglZzQ/FJq5SfFtQAGzeun6TQ6sR+JZx5MycoD9x/zpHgnV2aahaVkZBVDa1qO85F0+J9+mJFkzbnpXhByZkdBJIRRDZE9utqbPdvbskEgxGhzoaAOZzMj4pRE3z1oA++nr8mBN9P/sS/TwSpyIdNhCjRZoDkarPkhu7gF+OqB29T7DFEzGhEwgQ5ZaEMyzjDhhAttCPE24BHO0/xKuPOF+egvQ5L5/TxWm+VRFesCoCCkMubAX926SjdWVvfHyCcKY9K1L39U9/IfOFI9xFGKNXLgTW8KdOyzXPZc+fw==; bm_sz=30FF1370A2D18F7732A4AD01AB2957A2~YAAQzHAsz1PxaN19AQAAWlTt7g6DicMWnJNG2t/yZl2wR38IHiDhanzpViA2hstd98K8lXanryGIuriXdrfVFSb2rchexn5YrxCd1dhVBJIFBU4bdnL/kiNvsRPQAt1wUIK47OzZWcJI8n7/1wsPzH2dv7SymNCirq4e1RKD8z2Mi1Ap5mA0h+pXxVWf4XT6nCL6k/OrnKs84wBzpPlJ/u3IONaBZ1TtK/QBXMVlM+CpF4PYieYymwQniyc8B6SntIt+nM0Kd+oF3A9xykkgmRAf1brA9KfqifassC7nYb3moI8=~4342086~4404034; bm_sv=D8BF9F07F758C53011047F2D0A2858D2~0iwvqsRpX04ex2AcMEJo2f9ngFyAD+XKJOpgp1de4Xt3CIs4+qMfhA+eNqkrc34vChZ2z7Ty4G+MqhN+cug1M8aWmHJu3dhbbcvW9SCL4iD7wGh3xQGu/pKg6JHGfd58BYkakeQuRX0nWYk1Lv28dOwnhPXgy+IQ7dQStHkt+/o=',
                    }

                    url = f'https://www.tiktok.com/api/user/detail/?aid=1988&app_name=tiktok_web&device_platform=web_pc&uniqueId={username}'

                    params = (
                        ('aid', '1988'),
                        ('app_name', 'tiktok_web'),
                        ('device_platform', 'web_pc'),
                        ('uniqueId', f'{username}'),  # 
                    )

                    proxyDict = {
                        "http": 'http://' + random.choice(proxy_list)
                    }

                    r = requests.get(url, headers=headers, data=params, proxies=proxyDict)

                    if "10221" in r.text:
                        print('%s[BANNED] https://www.tiktok.com/@%s%s' % ('\u001b[31;1m', username, '\u001b[0m'))

                    elif "10202" in r.text:
                        print('%s[AVAILABLE] https://www.tiktok.com/@%s%s' % ('\u001b[32;1m', username, '\u001b[0m'))
                        f = open('hits.txt', 'a', encoding='UTF-8')
                        time.sleep(3)
                        sendwebhook(username)
                        f.write(f'{username}\n')
                except:
                    exit()
    async def start(self):
        system('cls||clear')
        print(""" __________ ____ ___  _________ _________.___   _____                                            
\______   \    |   \/   _____//   _____/|   | /  _  \                                           
 |       _/    |   /\_____  \ \_____  \ |   |/  /_\  \                                          
 |    |   \    |  / /        \/        \|   /    |    \                                         
 |____|_  /______/ /_______  /_______  /|___\____|__  /                                         
        \/                 \/        \/             \/                                          
  ___ ___ ________      _____   ________ __________  ___ ___ ________ __________.____________   
 /   |   \\_____  \    /     \  \_____  \\______   \/   |   \\_____  \\______   \   \_   ___ \  
/    ~    \/   |   \  /  \ /  \  /   |   \|     ___/    ~    \/   |   \|    |  _/   /    \  \/  
\    Y    /    |    \/    Y    \/    |    \    |   \    Y    /    |    \    |   \   \     \____ 
 \___|_  /\_______  /\____|__  /\_______  /____|    \___|_  /\_______  /______  /___|\______  / 
       \/         \/         \/         \/                \/         \/       \/            \/  
                                                                                                
                                                      https://discord.gg/G5hmTHJyXt                                          
                                                                                                

              
        """)
        async with aiohttp.ClientSession() as sess:
            return await asyncio.gather(
                *[self._check(sess, u) for u in self.to_check])
if __name__ == '__main__':
    while True:
        username_list.clear()
        proxy_list.clear()
        proxyscraper()
        usernamegenerator(10000)
        checker = Checker(username_list)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(checker.start())
