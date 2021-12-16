import requests
import re


utl_list = input().strip()
res = requests.get(f'{utl_list}')

html_сod_utl_list = res.text

spis_url = re.findall(r"<a .*href=(\"|')(\w+://)*(\w.+?)[:!@#$%^&*()/\\'\"]+?", html_сod_utl_list)

new_spis = list(set([i[2] for i in spis_url]))

new_spis.sort()
for i in new_spis:
    print(i)
