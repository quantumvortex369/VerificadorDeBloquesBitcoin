# Verificador de Bloques Bitcoin

Este programa verifica la validez de bloques y transacciones de la red Bitcoin de manera fácil y confiable.

## Características

- **Verificación de bloques** por hash o altura
- **Validación de transacciones** por ID
- **Comprobaciones exhaustivas** de integridad
- **Interfaz de línea de comandos** intuitiva
- **Validación en tiempo real** usando la red Bitcoin

## Requisitos

- Python 3.7 o superior
- Módulo `requests`
- Conexión a Internet

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/quantumvortex369/VerificadorDeBloquesBitcoin.git
cd VerificadorDeBloquesBitcoin
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Inicia el programa desde la línea de comandos:

```bash
python3 main.py
```

### Menú Principal

1. **Verificar bloque**
   - Ingresa el hash o altura del bloque
   - Ejemplo: `00000000000000000008a8a9b7a0a5b8d9c0d9e0f1a2b3c4d5e6f7a8b9c0d1e2f` o `700000`

2. **Verificar transacción**
   - Ingresa el ID de la transacción
   - Ejemplo: `a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d`

3. **Salir**
   - Cierra la aplicación

## Validaciones

### Para bloques:
- Estructura de datos correcta
- Timestamp válido
- Tamaño y peso dentro de límites
- Dificultad del bloque (prefijo 000000)
- Número válido de transacciones

### Para transacciones:
- Estructura de datos correcta
- Entradas y salidas válidas
- Balance correcto entre entradas y salidas
- Tamaño de transacción dentro de límites

## Estructura del Proyecto

```
VerificadorDeBloquesBitcoin/
├── main.py          # Punto de entrada
├── requirements.txt # Dependencias
├── src/             # Código fuente
│   ├── config.py    # Configuración
│   └── verificador.py # Lógica principal
└── tests/           # Pruebas unitarias
```

## Contribución

Las contribuciones son bienvenidas. Por favor, crea un issue o envía un pull request con tus mejoras.
