import requests

sites = ['https://sch16.edu.vn.ua/']
N = 100

for site in sites:
    for i in range(N):
        response = requests.get(site)
        print(i, site, response.status_code)