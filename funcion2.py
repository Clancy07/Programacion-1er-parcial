def reemplazarCaracteres(cadena: str, caracter_viejo: str, caracter_nuevo: str)->int:
    """Recibe una cadena de caracteres y dos caracteres por parametros y reemplaza todas las ocurrencias del segundo caracter por el tercero en la cadena original

    Args:
        cadena (_type_): cadena de caracteres a modificar
        caracter_viejo (_type_): caracter que sera reemplazado
        caracter_nuevo (_type_): caracter que sustituira al anterior 

    Returns:
        _type_: _description_
    """

    cantidad_de_reemplazos = cadena.count(caracter_viejo)
    cadena_modificada = cadena.replace(caracter_viejo, caracter_nuevo)

    return cantidad_de_reemplazos
