# main.py
from fastmcp import FastMCP
from tools.math_tools import add_numbers

# 1. Inicializar el servidor MCP
mcp = FastMCP("MiServidorRAG")

# 2. Registrar herramientas usando el decorador
# Al igual que en FastAPI registras rutas, aquí registras herramientas


@mcp.tool()
def sumar(a: int, b: int) -> int:
    """Suma dos números enteros. Utilizado para cálculos básicos."""
    return add_numbers(a, b)

# Puedes registrar recursos (datos que la IA puede leer)


@mcp.resource("config://app-settings")
def get_settings() -> str:
    """Devuelve la configuración base del sistema."""
    return '{"tema": "oscuro", "version": "1.0.0"}'


# 3. Punto de entrada para ejecutar el servidor
if __name__ == "__main__":
    # Inicia el servidor usando el transporte estándar (stdio)
    mcp.run()
