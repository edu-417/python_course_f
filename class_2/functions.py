# Ejemplo: cliente HTTP simplificado
def make_request(url, metodo, timeout, reintentos, verbose):
    if verbose:
        print(f"[{metodo}] {url}  timeout={timeout}s  reintentos={reintentos}")

    print(f"method: {metodo}")
    
    return {"status": 200, "url": url}






# def enviar_notificacion(mensaje, destinatario):
#     # print(f"Canal: {canal}")
#     print(f"Mensaje: '{mensaje}'")
#     print(f"Enviado a {destinatario} destinatario")
#     # for dest in destinatarios:
#         # print(f"  → {dest}")

def enviar_notificacion(mensaje, destinatario1, destinatario2):
    # print(f"Canal: {canal}")
    print(f"Mensaje: '{mensaje}'")
    print(f"Enviado a {destinatario1} destinatario1")
    print(f"Enviado a {destinatario2} destinatario2")


# def enviar_notificacion(mensaje, destinatario_list):
#     # print(f"Canal: {canal}")
#     print(f"Mensaje: '{mensaje}'")
#     for destinatario in destinatario_list:
#         print(f"Enviado a {destinatario} destinatario")

def enviar_notificacion(mensaje, *destinatarios, canales):
    print(f"Canal: {canal}")
    print(f"Mensaje: '{mensaje}'")
    print(f"Enviando a {len(destinatarios)} destinatario(s):")
    for dest in destinatarios:
        print(f"  → {dest}")



def generar_reporte(datos, titulo, **opciones):
    separador = opciones.get("separador", "-") * opciones.get("ancho", 40)
    formato   = opciones.get("formato", "tabla")
    pie       = opciones.get("pie", "")

    print(opciones)
 
    print(separador)
    print(f"  REPORTE: {titulo.upper()}")
    print(separador)
    print(f"  Formato: {formato} | Registros: {len(datos)}")
    if pie:
        print(f"  Nota: {pie}")
    print(separador)