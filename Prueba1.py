from datetime import datetime  # Importamos la librería para manejar fechas y horas

class Turno:
    def __init__(self, nombre, horario_inicio, horario_fin):
        """
        Clase que representa un turno de trabajo.
        :param nombre: Nombre del turno (Ejemplo: "Lunes a Jueves").
        :param horario_inicio: Hora de inicio del turno en formato 12 horas (Ejemplo: "6:40 AM").
        :param horario_fin: Hora de fin del turno en formato 12 horas (Ejemplo: "5:16 PM").
        """
        self.nombre = nombre
        self.horario_inicio = horario_inicio
        self.horario_fin = horario_fin

    def calcular_horas_trabajadas(self):
        """
        Calcula las horas trabajadas basándose en la diferencia entre la hora de inicio y la hora de fin.
        :return: Número de horas trabajadas en formato decimal.
        """
        formato = "%I:%M %p"  # Formato de hora (12 horas con AM/PM)
        inicio = datetime.strptime(self.horario_inicio, formato)  
        fin = datetime.strptime(self.horario_fin, formato)
        diferencia = fin - inicio
        return diferencia.total_seconds() / 3600  

    def mostrar_turno(self):
        """
        Muestra el nombre del turno y los horarios de inicio y fin.
        """
        print(f"\nTurno: {self.nombre}")
        print(f"Horario: {self.horario_inicio} - {self.horario_fin}")

class Operador:
    def __init__(self, nombre, id_operador, puesto, turno):  # Corregido __init__
        """
        Representa a un operador de la fábrica.
        :param nombre: Nombre del operador.
        :param id_operador: Identificación única del operador.
        :param puesto: Puesto o cargo del operador.
        :param turno: Turno asignado al operador (instancia de la clase Turno).
        """
        self.nombre = nombre
        self.id_operador = id_operador
        self.puesto = puesto
        self.turno = turno
        self.horas_trabajadas = 0  

    def registrar_horas_trabajadas(self, dias_trabajados):
        """
        Registra las horas trabajadas en función de los días que el operador ha trabajado.
        :param dias_trabajados: Lista con los días en los que el operador trabajó.
        """
        for dia in dias_trabajados:
            if dia.lower() in ["lunes", "martes", "miércoles", "jueves"]:
                horas = self.turno.calcular_horas_trabajadas()
            elif dia.lower() == "viernes":
                horas = Turno("Viernes", "6:40 AM", "2:46 PM").calcular_horas_trabajadas()
            else:
                horas = 0  
            self.horas_trabajadas += horas  

    def mostrar_informacion(self):
        """
        Muestra toda la información del operador.
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
            operador.nombre = input("Nuevo nombre: ")
            operador.puesto = input("Nuevo puesto: ")
            print("\nOperador actualizado exitosamente.")
            return
    print(f"\nNo se encontró un operador con ID {id_operador}.")

def main():
    """
    Función principal que maneja el menú interactivo del programa.
    """
    operadores = []  

    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Registrar un nuevo operador")
        print("2. Editar un operador")
        print("3. Eliminar un operador")
        print("4. Ver todos los operadores")
        print("5. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del operador: ")
            try:
                id_operador = int(input("ID del operador: "))  
            except ValueError:
                print("\nID no válido. Debe ser un número entero.")
                continue

            puesto = input("Puesto del operador: ")
            turno_largo = Turno("Lunes a Jueves", "6:40 AM", "5:16 PM")  
            operador = Operador(nombre, id_operador, puesto, turno_largo)

            dias_trabajados = input("\nDías trabajados (separados por coma): ").split(",")
            operador.registrar_horas_trabajadas([dia.strip().lower() for dia in dias_trabajados])
            operadores.append(operador)

        elif opcion == "2":
            try:
                id_operador = int(input("\nIntroduce el ID del operador a editar: "))
            except ValueError:
                print("\nID no válido. Debe ser un número entero.")
                continue
            editar_operador(operadores, id_operador)

        elif opcion == "3":
            try:
                id_operador = int(input("\nIntroduce el ID del operador a eliminar: "))
            except ValueError:
                print("\nID no válido. Debe ser un número entero.")
                continue
            eliminar_operador(operadores, id_operador)

        elif opcion == "4":
            if operadores:
                print("\nOperadores registrados:")
                for operador in operadores:
                    operador.mostrar_informacion()
            else:
                print("\nNo hay operadores registrados.")

        elif opcion == "5":
            print("\n¡Hasta luego!")
            break

        else:
            print("\nOpción no válida, por favor elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
