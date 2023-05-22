def ordenarCaracteres(cadena: str) -> str:
    """Ordena los caracteres de manera ascendente.

    Args:
        cadena (str): Cadena de caracteres.

    Returns:
        str: Cadena con los caracteres ordenados de manera ascendente.
    """
    caracteres_ordenados = sorted(cadena)
    cadena_ordenada = ''.join(caracteres_ordenados)
    
    return cadena_ordenada