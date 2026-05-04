# MiServidorRAG - Servidor MCP

Este proyecto implementa un servidor utilizando el **Model Context Protocol (MCP)** a través de la librería `FastMCP`. Está diseñado para exponer herramientas y recursos que pueden ser consumidos por agentes de IA (como Claude o Gemini).

## Estructura del Proyecto

- `main.py`: Punto de entrada principal del servidor donde se registran las herramientas y recursos.
- `tools/math_tools.py`: Módulo que contiene la lógica de negocio para las operaciones matemáticas.

## Requisitos

- Python 3.10 o superior.
- `fastmcp` instalado en el entorno virtual.

## Instalación

1. Asegúrate de tener el entorno virtual activo:
   ```bash
   .\venv\Scripts\activate
   ```
2. Instala las dependencias necesarias (si no lo has hecho):
   ```bash
   pip install fastmcp
   ```

## Funcionalidades Exposed

### Herramientas (Tools)

Las herramientas son funciones que la IA puede ejecutar para realizar acciones o cálculos.

- **`sumar(a: int, b: int)`**: 
  - **Descripción**: Suma dos números enteros. Utilizado para cálculos básicos.
  - **Retorno**: Un entero con el resultado de la suma.

### Recursos (Resources)

Los recursos son datos estáticos o dinámicos que la IA puede leer para obtener contexto.

- **`config://app-settings`**: 
  - **Descripción**: Devuelve la configuración base del sistema en formato JSON.
  - **Contenido**: Configuración de tema y versión.

## Ejecución

Para iniciar el servidor en modo de transporte estándar (stdio), simplemente ejecuta el archivo principal:

```bash
python main.py
```

---
*Documentación generada para el proyecto FastMCP.*