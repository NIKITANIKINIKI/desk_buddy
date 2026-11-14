from langchain.tools import tool


@tool
def add(a: float, b: float) -> float:
    """Складывает два числа."""
    return a + b
