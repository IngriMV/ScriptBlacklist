# ScriptBlacklist
Este es un Script para comparar IP's de un archivo (.TXT) si estas se encuentran en listas negras, si coincide con alguna de las IP's, genera un archivo con extensión (.csv) con estas IP's.

> Los datos de comparación se extraen de **AbuseIp**.


El siguiente paso a paso contiene la implementación de la API que incluye la herramienta **AbuseIP**, que tiene como objetivo el verificar las IP’s reportadas en listas negras (Funcionalidad de revisión masiva o individual).

## Paso 1. Registro

Se debe ingresar a la pagina web de AbuseIPDB y dar clic en la opción **Login** una vez allí, dar clic en el botón de **Register**; se debe diligenciar los campos correspondientes para poder obtener una cuenta oficial dentro de la aplicación.
 
 
## Paso 2. API key
Una vez verificada la cuenta se debe [crear la API](https://www.abuseipdb.com/account/api) dar clic en la opción **API → Create Key**; solicitará el asignar un nombre, para este ejemplo se denominará **PrimerApi**, automáticamente genera la API para su correspondiente uso.
 
## Paso 3. Script
Una vez se genera la API Key, se procede a ir a la documentación de los Scripts de la herramienta AbuseIP dando [clic Aquí](https://docs.abuseipdb.com/#plaintext-blacklist) ; se selecciona la Opción **REPORTS ENDPOINT** y dar clic en la opción **Python**

## Ejecución del Script

Sistema operativo Linux:
```
Python3 ScriptBlackList.py IPs.txt
```

Sistema operativo Windows:

Ir a la URL [get-pip.py](https://bootstrap.pypa.io/get-pip.py) ejecutar el archivo, para poder instalar pip en Windows.

```
python c:\users\ScriptBlackList.py ips.txt
```

## REFERENCIAS

[AbuseIP Blacklist](https://docs.abuseipdb.com/#plaintext-blacklist)
[PIP Windows](https://bootstrap.pypa.io/get-pip.py)


