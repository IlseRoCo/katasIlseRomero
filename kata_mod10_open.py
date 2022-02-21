def main():
    #open("/path/to/mars.jpg")
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError as err:
        print("Hubo un problema tratando de leer el archivo: ", err)
if __name__ == '__main__':
    main()