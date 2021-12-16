import requests
import re


A = input().strip()
res = requests.get(f'{A}')

html_kod_A = res.text

spis_url = re.findall(r"<a .*href=(\"|')(\w+://)*(\w.+?)[:!@#$%^&*()/\\'\"]+?", html_kod_A)

new_spis = list(set([i[2] for i in spis_url]))

new_spis.sort()
for i in new_spis:
    print(i)
