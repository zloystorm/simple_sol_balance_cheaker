import requests
from fake_useragent import UserAgent

headers = {
        'authority': 'api.solscan.io',
        'origin': 'https://solscan.io/',
        'referer': 'https://solscan.io/',
        'user-agent': UserAgent().random
}

f = open('asd.txt', 'a')


with open(input('Drop file with wallet adresses '), 'r') as file:
        for i in range(2500):
                jopech = file.readline()
                asd = jopech.split("\n")[0]
                payload = {'address' : asd}
                r = requests.get('https://api.solscan.io/account/v2/tokens?', params=payload, headers=headers)
                print(r.text)
                f.write(f'{r.text}\n')

