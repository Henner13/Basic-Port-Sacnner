# Escáner de Puertos Básico
# El escaner se limitara entre el puerto 1 al 1024

import socket
import argparse

# Función para escanear puertos
def escanear_puertos(objetivo, puerto_inicio=1, puerto_fin=1024):
    print(f"Escaneando {objetivo} desde el puerto {puerto_inicio} hasta el {puerto_fin}...\n")
    puertos_abiertos = []

    for puerto in range(puerto_inicio, puerto_fin + 1):
        try:
            # Creamos el socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # Tiempo de espera
            resultado = s.connect_ex((objetivo, puerto))  # Intentamos conectar
            if resultado == 0:
                try:
                    servicio = socket.getservbyport(puerto)
                except:
                    servicio = "Desconocido"
                print(f"Puerto {puerto} abierto ({servicio})")
                puertos_abiertos.append((puerto, servicio))
            s.close()
        except KeyboardInterrupt:
            print("\nEscaneo cancelado por el usuario.")
            break
        except socket.gaierror:
            print("Nombre de host no válido.")
            break
        except socket.error:
            print("Error al conectar con el servidor.")
            break

    if not puertos_abiertos:
        print("No se encontraron puertos abiertos.")
    return puertos_abiertos

# Programa principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escáner de Puertos Básico")
    parser.add_argument("host", help="IP o dominio a escanear")
    parser.add_argument("--start", type=int, default=1, help="Puerto inicial (por defecto 1)")
    parser.add_argument("--end", type=int, default=1024, help="Puerto final (por defecto 1024)")

    args = parser.parse_args()
    escanear_puertos(args.host, args.start, args.end)

