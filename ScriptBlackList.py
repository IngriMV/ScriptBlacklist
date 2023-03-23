import requests
import threading
import sys

API_KEY = 'TU_PROPIA_API_KEY'

def get_ip_score(ip):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90'
    headers = {'Key': API_KEY, 'Accept': 'application/json'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        score = data['data']['abuseConfidenceScore']
        return score
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener la puntuación de {ip}: {e}')
        return None

def worker(ip, scores):
    score = get_ip_score(ip)
    if score is not None and score > 50:
        scores[ip] = score

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
    with open('IPs_maliciosas.csv', 'w') as f:
        f.write('IP Address\n')
        for ip, score in scores.items():
            f.write(f'{ip}\n')
    print(f'Coincidencias guardadas en el archivo IPs_maliciosas.csv')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python abuseipdb.py FILENAME')
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
