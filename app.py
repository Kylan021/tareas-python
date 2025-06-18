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


gestor = GestorTareas()

gestor.bienvenida()
print(gestor.guardar_tarea("Aprender git"))
print(gestor.guardar_tarea("salir"))