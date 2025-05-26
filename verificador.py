import requests
from datetime import datetime
from config import API_URL

class BlockVerifier:
    """
    Clase para verificar la validez de bloques y transacciones de Bitcoin.
    
    Métodos:
        validate_block(hash_or_height): Verifica la validez de un bloque
        validate_transaction(tx_id): Verifica la validez de una transacción
    """
    
    def __init__(self):
        """Inicializa el verificador con la URL de la API y headers"""
        self.api_url = API_URL
        self.headers = {'User-Agent': 'Bitcoin Block Verifier'}

    def validate_block(self, hash_or_height):
        """
        Valida un bloque de Bitcoin.
        
        Args:
            hash_or_height: Hash del bloque o altura numérica
        
        Returns:
            None - Imprime resultados directamente
        """
        try:
            # Determinar si es altura o hash
            url = f"{self.api_url}/block-height/{hash_or_height}" if isinstance(hash_or_height, int) \
                 else f"{self.api_url}/block/{hash_or_height}"

            # Obtener datos del bloque
            r = requests.get(url, headers=self.headers)
            r.raise_for_status()
            block = r.json()

            # Inicializar validación
            valid = True
            issues = []

            # Validaciones
            try:
                timestamp = datetime.fromtimestamp(block['timestamp'])
            except (ValueError, TypeError):
                valid = False
                issues.append("Timestamp inválido")

            # Validar tamaño y peso
            if block['size'] <= 0:
                valid = False
                issues.append(f"Tamaño inválido: {block['size']} bytes")

            if block['weight'] <= 0:
                valid = False
                issues.append(f"Peso inválido: {block['weight']}")

            # Validar dificultad (hash)
            if block['id'][:6] != '000000':
                valid = False
                issues.append("Hash no cumple con la dificultad (prefijo 000000)")

            # Validar transacciones
            tx_count = block['tx_count']
            if tx_count <= 0:
                valid = False
                issues.append(f"Número de transacciones inválido: {tx_count}")

            # Mostrar resultados
            print("\n=== Resultado de Verificación ===")
            print(f"Bloque: {block['id']}")
            print(f"Altura: {block['height']}")
            print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')} (UTC)")
            print(f"Tamaño: {block['size']} bytes")
            print(f"Peso: {block['weight']}")
            print(f"Transacciones: {tx_count}")
            print(f"Bits: {block['bits']}")
            print(f"Nonce: {block['nonce']}")

            if valid:
                print("\n✅ Bloque válido")
            else:
                print("\n❌ Bloque inválido")
                print("\nProblemas encontrados:")
                for issue in issues:
                    print(f"- {issue}")

        except requests.exceptions.RequestException as e:
            print(f"\n❌ Error al obtener el bloque: {e}")
        except KeyError as e:
            print(f"\n❌ Error en la estructura del bloque: {e}")

    def validate_transaction(self, tx_id):
        """
        Valida una transacción de Bitcoin.
        
        Args:
            tx_id: ID de la transacción
        
        Returns:
            None - Imprime resultados directamente
        """
        try:
            # Obtener datos de la transacción
            url = f"{self.api_url}/tx/{tx_id}"
            r = requests.get(url, headers=self.headers)
            r.raise_for_status()
            tx = r.json()

            # Inicializar validación
            valid = True
            issues = []

            # Validar entradas y salidas
            if len(tx['vin']) == 0:
                valid = False
                issues.append("Transacción sin entradas")

            if len(tx['vout']) == 0:
                valid = False
                issues.append("Transacción sin salidas")

            # Validar valor total
            total_input = sum(input['value'] for input in tx['vin'] if 'value' in input)
            total_output = sum(output['value'] for output in tx['vout'])

            if total_output > total_input:
                valid = False
                issues.append(f"Salida excede entrada (Entrada: {total_input}, Salida: {total_output})")

            # Validar tamaño
            if tx['size'] <= 0:
                valid = False
                issues.append(f"Tamaño inválido: {tx['size']} bytes")

            # Mostrar resultados
            print("\n=== Resultado de Verificación ===")
            print(f"Transacción: {tx['txid']}")
            print(f"Tamaño: {tx['size']} bytes")
            print(f"Peso: {tx['weight']}")
            print(f"Entradas: {len(tx['vin'])}")
            print(f"Salidas: {len(tx['vout'])}")
            print(f"Valor total: {total_output} satoshis")

            if valid:
                print("\n✅ Transacción válida")
            else:
                print("\n❌ Transacción inválida")
                print("\nProblemas encontrados:")
                for issue in issues:
                    print(f"- {issue}")

        except requests.exceptions.RequestException as e:
            print(f"\n❌ Error al obtener la transacción: {e}")
        except KeyError as e:
            print(f"\n❌ Error en la estructura de la transacción: {e}")

def main():
    """Función principal que maneja la interfaz de usuario"""
    print("""
=== Verificador de Bloques Bitcoin ===

Este programa verifica la validez de bloques y transacciones de Bitcoin.
Las validaciones incluyen:
- Estructura correcta
- Timestamp válido
- Tamaño y peso correctos
- Dificultad del bloque
- Balance de transacciones
    """)

    verifier = BlockVerifier()
    
    while True:
        print("\n=== Menú Principal ===")
        print("1. Verificar bloque")
        print("2. Verificar transacción")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ").strip()
        
        if opcion == '1':
            while True:
                hash_or_height = input("\nIntroduce el hash o altura del bloque (o 'q' para volver): ").strip()
                if hash_or_height.lower() == 'q':
                    break
                    
                try:
                    height = int(hash_or_height)
                    verifier.validate_block(height)
                    break
                except ValueError:
                    if hash_or_height:  # Solo validar si no está vacío
                        verifier.validate_block(hash_or_height)
                        break
                    print("Por favor, introduce un hash válido o una altura numérica")
        
        elif opcion == '2':
            while True:
                tx_id = input("\nIntroduce el ID de la transacción (o 'q' para volver): ").strip()
                if tx_id.lower() == 'q':
                    break
                if tx_id:  # Solo validar si no está vacío
                    verifier.validate_transaction(tx_id)
                    break
                print("Por favor, introduce un ID de transacción válido")
        
        elif opcion == '3':
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 3.")

if __name__ == "__main__":
    main()
