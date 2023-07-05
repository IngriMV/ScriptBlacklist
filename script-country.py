import requests
import threading
import sys
import json
import csv
import pycountry

API_KEY = 'e78fd35fe75c68e59410bb87330246dc30d475a2875dd27650a042e16f1b7b0d8be50e9de977c404'

def get_ip_info(ip):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90'
    headers = {'Key': API_KEY, 'Accept': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['data']
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener información de {ip}: {e}')
        return None

def get_country_name(country_code):
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        return country.name
    except Exception as e:
        print(f"Error: {e}")
        return None

def worker(ip, scores):
    ip_info = get_ip_info(ip)
    if ip_info is not None:
        score = ip_info.get('abuseConfidenceScore')
        if score is not None and score > 50:
            country_code = ip_info.get('countryCode')
            country_name = get_country_name(country_code)
            if country_name is not None:
                scores[ip] = {'score': score, 'country': country_name}
            else:
                scores[ip] = {'score': score, 'country': 'País no encontrado'}

def main(filename):
    with open(filename, 'r') as f:
        ips = f.read().splitlines()
    scores = {}
    threads = []
    for ip in ips:
        t = threading.Thread(target=worker, args=(ip, scores))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    with open('IPS_maliciosas.csv', 'w') as f:
        f.write('IP Address, Score, Country\n')
        for ip, data in scores.items():
            f.write(f'{ip}, {data["score"]}, {data["country"]}\n')

    print(f'Coincidencias guardadas en el archivo IPS_maliciosas.csv')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python Script.py FILENAME')
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
