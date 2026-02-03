def mensaje_edad(edad):
    if not isinstance(edad, int):
        return 'Edad no válida'
    
    if edad < 0: 
        return 'No existes'
    elif edad < 13:
        return 'Eres un niño'
    elif edad < 18:
        return 'Eres un adolescente'
    elif edad < 65:
        return 'Eres un adulto'
    elif edad < 120:
        return 'Eres un adulto mayor'
    else:
        return 'Eres Mumm-Ra'