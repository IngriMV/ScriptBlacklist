import sys
import requests
import csv

# Leer el nombre de archivo txt desde la línea de comandos
try:
    file_name = sys.argv[1]
except IndexError:
    print("Debe proporcionar el nombre del archivo .txt como argumento.")
    sys.exit(1)

# Leer las direcciones IP desde el archivo txt
try:
    with open(file_name, 'r') as f:
        txt_ips = set()
        for line in f:
            line = line.strip()
            if line:
                txt_ips.add(line)
except FileNotFoundError:
    print(f"El archivo {file_name} no se encuentra.")
    sys.exit(1)
except Exception as e:
    print(f"Ocurrió un error inesperado al leer el archivo txt: {e}")
    sys.exit(1)

# Definir la URL de la API y los encabezados
url = 'https://api.abuseipdb.com/api/v2/check'
headers = {
    'Accept': 'application/json',
    'Key': 'API Key'
}

# Definir una lista para almacenar las direcciones IP que coinciden
matched_ips = []

# Hacer una solicitud GET a la API para cada dirección IP de texto y verificar si está en la lista negra
for ip in txt_ips:
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90',
        'limit':'500000'
    }
    try:
        response = requests.get(url=url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        if data['data']['isWhitelisted'] == False and data['data']['abuseConfidenceScore'] >= 90:
            matched_ips.append(ip)
    except requests.exceptions.HTTPError as e:
        print(f"Error al hacer la solicitud a la API: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error al procesar la respuesta de la API: {e}")

# Si se encontraron coincidencias, generar un archivo CSV con las direcciones IP coincidentes
if matched_ips:
    try:
        with open('IPs_maliciosas.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Direccion IP'])
            for ip in matched_ips:
                writer.writerow([ip])
        print(f"Se encontraron {len(matched_ips)} direcciones IP coincidentes. Se ha generado el archivo 'matched_ips.csv'.")
    except Exception as e:
        print(f"Error al escribir el archivo CSV: {e}")
else:
    print("No se encontraron direcciones IP coincidentes.")
