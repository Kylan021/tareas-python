"""
Un script en Python que permita:

Agregar tareas

Ver tareas

Marcar tareas como completadas

Guardar las tareas en un archivo .txt

🎯 Objetivo
Practicar:

git init, add, commit, status, log, diff, .gitignore, etc.

Estructurar versiones reales con Git
"""

class GestorTareas:

    def __init__(self):
        
        self.tareas = []

    
    def bienvenida(self):

        print("Bienvenido a tu lista de tareas")


    def guardar_tarea(self, tarea):

        if tarea not in self.tareas:

            if tarea.lower() == "salir":

                return "Saliendo del programa"

            self.tareas.append(tarea)
            return "Tarea agregada"


    def listar_tareas(self):

        if self.tareas:

            for index, tarea in enumerate(self.tareas, start=1):

                print(f"{index}. {tarea}")

        else:

            print("No hay tareas")


    def guardar_archivo(self):

        with open("tareas.txt", "w") as archivo:

            for index, tarea in enumerate(self.tareas, start=1):

                archivo.write(f"{index}. {tarea}\n")


    def eliminar_tarea(self, tarea):

        if tarea in self.tareas:

            self.tareas.remove(tarea)
            return f"Tarea {tarea} eliminada."
        
        return f"No se encuentra dentro de las tareas."


gestor = GestorTareas()

gestor.bienvenida()
print(gestor.guardar_tarea("Aprender git"))
print(gestor.guardar_tarea("Aprender gitHub"))
print(gestor.guardar_tarea("salir"))
gestor.listar_tareas()
gestor.guardar_archivo()
print(gestor.eliminar_tarea("Aprender gitHub"))
gestor.listar_tareas()
