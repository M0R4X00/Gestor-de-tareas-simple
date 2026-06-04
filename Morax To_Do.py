import json
import os 

Archivo = "Morax_To_Do.json"

# Esta función carga la tareas existentes o crea una lista vacía si no existe el archivo.

def cargar_tareas():
    if os.path.exists(Archivo): # Verifica si el archivo existe
        with open(Archivo, 'r', encoding='utf-8') as f: #Encoding con utf 8 es para poder hacer cualquier aracter en unicode sin esto las tildes o la ñ valdria pura V
            return json.load(f)  # Carga las tareas desde el archivo JSON 
    else:
        return []   # Si el archivo no existe, devuelve una lista vacía
    

#Guardar tarea en el archivo JSON
def guardar_tareas(tareas):
    with open(Archivo, 'w', encoding='utf-8') as f: # con el 'w' se abre el archivo en modo escritura, si no existe lo crea
        json.dump(tareas, f, indent=4) # Guarda las tareas en el archivo JSON con una indentación de 4 espacios

tareas = cargar_tareas() # Carga las tareas al inicio del programa

#funciones para un menu interacitivo

#funcion que imprime el menu de opciones
def menu():
    print("\n\033[91m====================== Morax To Do =====================\033[0m") # \033[91m y \033[0m son codigos de escape ANSI para cambiar el color del texto en la terminal
    print("1. Ver tareas")
    print("2. Agregar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("\033[91m==========================================================\033[0m")

#funciones para ver, agregar, completar y eliminar tareas

def ver_tareas():

    if not tareas:
        print("\nNo hay tareas disponibles.")
        return
    for i, tarea in enumerate(tareas): # enumerate te da el numero de la posicion del array y la tarea que esta en esa posicion y tarea es un diccionario
        estado = "Completa" if tarea["completada"] else "incompleta" # esto es un operador ternario, si la tarea esta completada se pone completa y si no incompleta
        print(f"{i + 1}. [{estado}]{tarea['descripcion']}") #i + 1 es para que el usuario vea las tareas desde el 1 y no desde el 0, ya que en python los arrays empiezan desde el 0


def guarda_tarea ():

    desc = input("Escriba el titulo de la tarea: ")
    tareas.append({"descripcion": desc, "completada": False})# append agrega un elemento al final de la lista, en este caso un diccionario con la descripcion y el estado de la tarea
    guardar_tareas(tareas) #guarda la tarea                 # descripcion: desc es la variable que guarda el input del usuario y completada: False es para que la tarea se marque como incompleta al inicio
    print("\nTarea añadida.")


def completar_tarea():
    ver_tareas()
    try:
        num = int(input("¿Que tarea completaste? ")) -1 # el -1 es para que el usuario vea las tareas desde el 1 y no desde el 0, ya que en python los arrays empiezan desde el 0
        if 0<= num < len(tareas): # si el numero esta dentro del rango de las tareas
            tareas[num]["completada"] = True # marca la tarea como completada
            guardar_tareas(tareas)  # guarda las tareas actualizadas
            print("\nTarea marcada como completa")
        else:
            print("\nTarea no existe")
    
    except: 
        print("\nOpcion invalida")

def eliminar_tarea(): 
    ver_tareas()
    try:
        num = int(input("Qué tarea desea borrar" )) -1
        if 0<= num <len(tareas):    # si el numero esta dentro del rango de las tareas
            eliminada = tareas.pop(num)# el pop lo que hace es eliminar el elemnto de la posicion de la variable 'num' y el -1 es para quitarlo del array creo
            guardar_tareas(tareas)
            print(f"\n{eliminada['descripcion']} eliminada con exito")
        else:
            print("\nNumero fuera de rango")
    except:
        print("\nOpcion invalida")


#el while lo que hace es mantener el menu hasta que este se marque en la opcion numero 5

while True:
    menu()
    opcion = input("\033[92m Elige una opcion \033[0m")
    if opcion == '1':
        ver_tareas()
    elif opcion == '2':
        guarda_tarea()
    elif opcion == '3':
        completar_tarea()
    elif opcion == '4':
        eliminar_tarea()
    elif opcion =='5':
        print("\nCerrando...\n\n\n")
        break   # este se usa para cortar la terminal y que este deje de hacer el while
    else:
        print("opcion invalida")
        