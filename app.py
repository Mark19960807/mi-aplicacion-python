from datetime import datetime

class Turno:
    def __init__(self, nombre, horario_inicio, horario_fin):
        """
        Esta clase representa un turno de trabajo. Le damos un nombre y los horarios de inicio y fin.
        
        :param nombre: El nombre del turno (por ejemplo, "Lunes a Jueves").
        :param horario_inicio: La hora de entrada del turno (en formato 12 horas con AM/PM).
        :param horario_fin: La hora de salida del turno (en formato 12 horas con AM/PM).
        """
        self.nombre = nombre  # Nombre del turno
        self.horario_inicio = horario_inicio  # Hora en la que comienza el turno
        self.horario_fin = horario_fin  # Hora en la que termina el turno

    def calcular_horas_trabajadas(self):
        """
        Este método calcula las horas trabajadas, basándose en la hora de inicio y de fin del turno.
        La diferencia entre estas dos horas nos da las horas trabajadas.
        """
        formato = "%I:%M %p"  # Usamos el formato de hora de 12 horas con AM/PM
        inicio = datetime.strptime(self.horario_inicio, formato)  # Convertimos la hora de entrada en un objeto datetime
        fin = datetime.strptime(self.horario_fin, formato)  # Convertimos la hora de salida en un objeto datetime
        diferencia = fin - inicio  # Calculamos la diferencia de tiempo
        horas_trabajadas = diferencia.total_seconds() / 3600  # Convertimos la diferencia de segundos a horas
        return horas_trabajadas  # Devolvemos el número de horas trabajadas

    def mostrar_turno(self):
        """
        Este método imprime el turno con su nombre y los horarios de inicio y fin.
        """
        print(f"\nTurno: {self.nombre}")
        print(f"Horario: {self.horario_inicio} - {self.horario_fin}")


class Operador:
    def __init__(self, nombre, id_operador, puesto, turno):
        """
        Esta clase representa a un operador de la fábrica. Cada operador tiene un nombre, un ID, un puesto,
        y el turno al que está asignado.
        
        :param nombre: El nombre del operador.
        :param id_operador: El ID único del operador.
        :param puesto: El puesto o cargo del operador en la fábrica.
        :param turno: El turno asignado al operador (es una instancia de la clase Turno).
        """
        self.nombre = nombre  # Nombre del operador
        self.id_operador = id_operador  # ID único del operador
        self.puesto = puesto  # Puesto del operador
        self.turno = turno  # El turno asignado al operador
        self.horas_trabajadas = 0  # Inicialmente, el operador no ha trabajado ninguna hora

    def registrar_horas_trabajadas(self, dias_trabajados):
        """
        Aquí registramos las horas trabajadas por el operador según los días que ha trabajado.
        Dependiendo del día, usamos diferentes horarios de trabajo.
        
        :param dias_trabajados: Lista con los días en los que el operador trabajó (Ejemplo: ["lunes", "martes", "viernes"])
        """
        for dia in dias_trabajados:
            if dia.lower() in ["lunes", "martes", "miércoles", "jueves"]:
                # Si el operador trabajó de lunes a jueves, usamos el turno largo
                horas = self.turno.calcular_horas_trabajadas()
            elif dia.lower() == "viernes":
                # Si es viernes, usamos el turno corto
                horas = Turno("Viernes", "6:40 AM", "2:46 PM").calcular_horas_trabajadas()
            else:
                horas = 0  # Si el día no es válido (no es un día de trabajo), no contamos horas
            self.horas_trabajadas += horas  # Sumamos las horas trabajadas ese día al total

    def mostrar_informacion(self):
        """
        Este método muestra toda la información relevante del operador.
        Incluye su ID, nombre, puesto, el turno al que está asignado y las horas trabajadas.
        """
        print(f"\nID Operador: {self.id_operador}")
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Turno: {self.turno.nombre}")
        print(f"Horas trabajadas: {self.horas_trabajadas}")


def eliminar_operador(operadores, id_operador):
    """
    Elimina un operador de la lista de operadores según su ID.
    """
    for operador in operadores:
        if operador.id_operador == id_operador:
            operadores.remove(operador)
            print(f"\nOperador con ID {id_operador} ha sido eliminado.")
            return
    print(f"\nNo se encontró un operador con ID {id_operador}.")


def editar_operador(operadores, id_operador):
    """
    Permite editar los detalles de un operador en la lista.
    """
    for operador in operadores:
        if operador.id_operador == id_operador:
            print(f"\nEditando operador {operador.nombre} (ID: {operador.id_operador}).")
            nombre = input("Nuevo nombre: ")
            puesto = input("Nuevo puesto: ")
            operador.nombre = nombre
            operador.puesto = puesto
            print("\nOperador actualizado exitosamente.")
            return
    print(f"\nNo se encontró un operador con ID {id_operador}.")


def main():
    operadores = []  # Lista donde guardaremos los operadores registrados

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Registrar un nuevo operador")
        print("2. Editar un operador")
        print("3. Eliminar un operador")
        print("4. Ver todos los operadores")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            # Registrar nuevo operador
            print("\n¡Bienvenido! Vamos a registrar los datos del operador.\n")
            nombre = input("¿Cómo se llama el operador? ")
            id_operador = int(input("¿Cuál es el ID del operador? "))
            puesto = input("¿Cuál es el puesto del operador? ")

            print("\nAhora vamos a definir el turno del operador.")
            print("El turno de lunes a jueves es de 6:40 AM a 5:16 PM.\n")

            # Creamos el turno de lunes a jueves (6:40 AM - 5:16 PM)
            turno_largo = Turno("Lunes a Jueves", "6:40 AM", "5:16 PM")
            
            # Creamos la instancia del operador con los datos proporcionados
            operador = Operador(nombre, id_operador, puesto, turno_largo)

            # Pedimos los días que trabajó el operador
            dias_trabajados_input = input("\n¿En qué días trabajó el operador? (Separados por coma, por ejemplo: lunes, martes, viernes) ")
            dias_trabajados = [dia.strip().lower() for dia in dias_trabajados_input.split(",")]

            # Registramos las horas trabajadas del operador
            operador.registrar_horas_trabajadas(dias_trabajados)

            # Agregamos el operador a la lista
            operadores.append(operador)

        elif opcion == "2":
            # Editar operador
            id_operador = int(input("\nIntroduce el ID del operador a editar: "))
            editar_operador(operadores, id_operador)

        elif opcion == "3":
            # Eliminar operador
            id_operador = int(input("\nIntroduce el ID del operador a eliminar: "))
            eliminar_operador(operadores, id_operador)

        elif opcion == "4":
            # Ver todos los operadores registrados
            if operadores:
                print("\nOperadores registrados:")
                for operador in operadores:
                    operador.mostrar_informacion()
            else:
                print("\nNo hay operadores registrados.")

        elif opcion == "5":
            # Salir
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida, por favor elige una opción entre 1 y 5.")


if __name__ == "__main__":
    main()

