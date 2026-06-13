
# try:
# int("adsdas")
# print(0/0)
# except:
#     print("Division entre 0")

# edad = int(input("Ingrese su edad: "))

# if( edad < 0):
#     raise Exception(f"La edad ingresada no es valida")


# assert(edad < 18)
# assert(edad > 0)


# def windows_interaction():
#     import sys
#     if "windows" not in sys.platform:
#         raise RuntimeError("Function can only run on Windows systems.")
#     print("Doing Windows things.")


# try:
#     # print(0/0)
#     windows_interaction()
# except RuntimeError as runtime_error:
#     print(runtime_error)
# except ZeroDivisionError as zero_error:
#     print(zero_error)
# else:
#     print("Otras cosas de windows")

# except (RuntimeError, ZeroDivisionError) as e:
    # print(e)

# print("Sigue ejecutando")

try:
    file = open("../class_4/estudiantes.csv")
    file.read()
except FileNotFoundError as file_error:
    print(file_error)
finally:
    print("Cerrando archivo")
    file.close()


