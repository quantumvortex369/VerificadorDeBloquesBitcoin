import requests

def obtener_bloque_actual():
    url = "https://blockstream.info/api/blocks"
    r = requests.get(url)
    bloques = r.json()
    bloque = bloques[0]
    print(f"Altura: {bloque['height']}")
    print(f"Hash: {bloque['id']}")
    print(f"Timestamp: {bloque['timestamp']}")
    print(f"Cantidad de transacciones: {bloque['tx_count']}")
    print(f"Minería exitosa: {'000000' in bloque['id']}")

obtener_bloque_actual()