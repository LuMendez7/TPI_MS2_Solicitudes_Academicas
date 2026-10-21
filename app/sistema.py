
solicitudes = []
contador = 1


def procesar(opcion, titulo="", tipo="", prioridad="", responsable="", numero=0, estado=""):
    global contador

    if opcion == 1:
        if titulo != "":
            if tipo != "":
                if prioridad != "":
                    if prioridad == "ALTA" or prioridad == "MEDIA" or prioridad == "BAJA":
                        solicitud = {
                            "id": contador,
                            "titulo": titulo,
                            "tipo": tipo,
                            "prioridad": prioridad,
                            "responsable": responsable,
                            "estado": "PENDIENTE"
                        }
                        solicitudes.append(solicitud)
                        contador += 1
                        return "Solicitud registrada"
                    else:
                        return "Prioridad invalida"
                else:
                    return "Prioridad obligatoria"
            else:
                return "Tipo obligatorio"
        else:
            return "Titulo obligatorio"

    elif opcion == 2:
        for s in solicitudes:
            if s["id"] == numero:
                s["responsable"] = responsable
                return "Responsable asignado"
        return "Solicitud no encontrada"

    elif opcion == 3:
        for s in solicitudes:
            if s["id"] == numero:
                if estado == "PENDIENTE" or estado == "EN_PROCESO" or estado == "RESUELTA":
                    s["estado"] = estado
                    return "Estado actualizado"
                else:
                    return "Estado invalido"
        return "Solicitud no encontrada"

    elif opcion == 4:
        for s in solicitudes:
            if s["id"] == numero:
                return str(s)
        return "Solicitud no encontrada"

    elif opcion == 5:
        pendientes = 0
        en_proceso = 0
        resueltas = 0

        for s in solicitudes:
            if s["estado"] == "PENDIENTE":
                pendientes += 1
            elif s["estado"] == "EN_PROCESO":
                en_proceso += 1
            elif s["estado"] == "RESUELTA":
                resueltas += 1

        return (
            "Pendientes: " + str(pendientes)
            + " | En proceso: " + str(en_proceso)
            + " | Resueltas: " + str(resueltas)
        )

    elif opcion == 6:
        return str(solicitudes)

    else:
        return "Opcion invalida"


def main():
    while True:
        print("\nSISTEMA DE SOLICITUDES ACADEMICAS")
        print("1. Registrar solicitud")
        print("2. Asignar responsable")
        print("3. Cambiar estado")
        print("4. Consultar solicitud")
        print("5. Generar reporte")
        print("6. Listar solicitudes")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            print("Programa finalizado")
            break

        if opcion == "1":
            titulo = input("Titulo: ")
            tipo = input("Tipo: ")
            prioridad = input("Prioridad (ALTA/MEDIA/BAJA): ")
            responsable = input("Responsable: ")
            print(procesar(1, titulo, tipo, prioridad, responsable))

        elif opcion == "2":
            numero = int(input("ID de solicitud: "))
            responsable = input("Responsable: ")
            print(procesar(2, responsable=responsable, numero=numero))

        elif opcion == "3":
            numero = int(input("ID de solicitud: "))
            estado = input("Estado (PENDIENTE/EN_PROCESO/RESUELTA): ")
            print(procesar(3, numero=numero, estado=estado))

        elif opcion == "4":
            numero = int(input("ID de solicitud: "))
            print(procesar(4, numero=numero))

        elif opcion == "5":
            print(procesar(5))

        elif opcion == "6":
            print(procesar(6))

        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()
