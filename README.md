# Morax To Do

Aplicación de gestión de tareas desarrollada en Python para terminal. Permite crear, visualizar, completar y eliminar tareas, almacenando la información de forma persistente mediante un archivo JSON.

## Características

* Ver tareas pendientes y completadas.
* Agregar nuevas tareas.
* Marcar tareas como completadas.
* Eliminar tareas existentes.
* Almacenamiento persistente utilizando JSON.
* Interfaz simple en consola con colores ANSI.

## Tecnologías Utilizadas

* Python 3
* JSON
* OS (gestión de archivos)

## Estructura del Proyecto

```text
Morax_To_Do/
│
├── Morax_To_Do.py
├── Morax_To_Do.json
└── README.md
```

## Funcionamiento

Las tareas se almacenan en el archivo:

```text
Morax_To_Do.json
```

Cada tarea se guarda con la siguiente estructura:

```json
{
    "descripcion": "[aqui poner la tarea]",
    "completada": false
}
```

## Menú Principal

```text
====================== Morax To Do ======================

1. Ver tareas
2. Agregar tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir

=========================================================
```

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/Morax-To-Do.git
```

2. Entrar a la carpeta:

```bash
cd Morax-To-Do
```

3. Ejecutar el programa:

```bash
python Morax_To_Do.py
```

## Conceptos Practicados

Este proyecto fue desarrollado como ejercicio para reforzar conceptos fundamentales de Python:

* Funciones
* Listas
* Diccionarios
* Manejo de archivos
* Persistencia de datos
* JSON
* Manejo de excepciones
* Bucles y estructuras de control

## Posibles Mejoras Futuras

* Fechas límite para tareas.
* Prioridades (Alta, Media, Baja).
* Búsqueda de tareas.
* Interfaz gráfica.
* Estadísticas de productividad.
* Sincronización con base de datos.
