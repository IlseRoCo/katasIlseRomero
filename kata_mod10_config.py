def main():
    try:
# Ejercicio 1
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("¡No se puede encontrar el archivo config.txt!")

# Ejercicio 2
#   except Exception:
#        print("¡No se puede encontrar el archivo config.txt!")
# Agregué una excepción de permisos ya que a mi me muestra un error de permisos y no uno de directorio
#    except PermissionError: 
#        print("¡Hubo un error de permisos!")    

# Ejercicio 3     
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("¡No se puede encontrar el archivo config.txt!")
        elif err.errno == 13:
            print("¡No se puede encontrar el archivo config.txt!")

if __name__ == '__main__':
    main()

    