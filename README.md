# Verificador de Bloques Bitcoin

Este programa verifica la validez de bloques y transacciones de la red Bitcoin.

## Funcionalidades

- Verificación de bloques por hash o altura
- Verificación de transacciones por ID
- Validación de estructura y datos
- Identificación de problemas específicos

## Requisitos

- Python 3.7+
- requests
- datetime

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install requests
```

## Uso

Ejecutar el script:

```bash
python verificador.py
```

El programa mostrará un menú interactivo donde puedes:
1. Verificar un bloque (introduciendo hash o altura)
2. Verificar una transacción (introduciendo ID)
3. Salir del programa

## Validaciones

Para bloques:
- Estructura correcta
- Timestamp válido
- Tamaño y peso correctos
- Dificultad del bloque (prefijo 000000)
- Balance de transacciones

Para transacciones:
- Estructura correcta
- Entradas y salidas válidas
- Balance de valores
- Tamaño válido
