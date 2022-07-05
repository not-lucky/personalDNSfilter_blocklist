import requests as req

res = req.get('https://hosts.oisd.nl/')
with open('oisd_hosts_full.txt', 'w') as fl:
    print(res.content.decode().replace('0.0.0.0', '127.0.0.1'), file=fl)
