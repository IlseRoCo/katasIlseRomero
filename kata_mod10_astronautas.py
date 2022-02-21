#def uso_agua(astronautas, agua, dias):
#    uso_diario = astronautas * 11
#    uso_total = uso_diario * dias
#    total_agua = agua - uso_total
#    return f"Agua total restante despues de {dias} días: {total_agua} litros."

#if __name__ == '__main__':
#    uso_agua(5,100,2)

# Modificación 2
#def uso_agua(astronautas, agua, dias):
#    uso_diario = astronautas * 11
#    uso_total = uso_diario * dias
#    total_agua = agua - uso_total

#    if total_agua < 0:
#        raise RuntimeError(f"¡No hay suficiente agua para {astronautas} astronautas después de {dias} días!")
#    return f"Agua total restante despues de {dias} días: {total_agua} litros."

#if __name__ == '__main__':
#    uso_agua(5,100,2)

# Modificación 3
def uso_agua(astronautas, agua, dias):
    for item in [astronautas, agua, dias]:
        try:
            # Si el argumento es entero, la siguient operación funcionará
            item / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben ser de tipo entero, recibimos '{item}'.")
    uso_diario = astronautas * 11
    uso_total = uso_diario * dias
    total_agua = agua - uso_total

    if total_agua < 0:
        raise RuntimeError(f"¡No hay suficiente agua para {astronautas} astronautas después de {dias} días!")
    return f"Agua total restante despues de {dias} días: {total_agua} litros."

if __name__ == '__main__':
    uso_agua("3","200",None)    