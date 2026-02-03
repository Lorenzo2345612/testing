# language: es

Característica: Eliminar tareas del gestor
    Como usuario del gestor de tareas
    Quiero poder eliminar tareas
    Para mantener el gestor organizado y sin tareas obsoletas

    Escenario: Eliminar una tarea existente
        Dado que el gestor tiene una tarea con nombre "Comprar pan" y descripción "Comprar pan en la panadería"
        Cuando elimino la tarea con ID 1
        Entonces la tarea se elimina exitosamente
        Y la operación devuelve True
        Y el gestor tiene 0 tareas
        Y la tarea con ID 1 ya no está en el gestor

    Escenario: Intentar eliminar una tarea inexistente
        Dado que el gestor de tareas está vacío
        Cuando intento eliminar la tarea con ID 999
        Entonces se produce un error con mensaje "No se encontró una tarea con ID 999"

    Escenario: Eliminar una tarea cuando hay varias
        Dado que el gestor tiene 3 tareas
        Cuando elimino la tarea con ID 2
        Entonces la tarea se elimina exitosamente
        Y el gestor tiene 2 tareas
        Y la tarea con ID 1 permanece en el gestor
        Y la tarea con ID 3 permanece en el gestor
        Y la tarea con ID 2 ya no está en el gestor

    Escenario: Eliminar todas las tareas una por una
        Dado que el gestor tiene 2 tareas
        Cuando elimino la tarea con ID 1
        Y elimino la tarea con ID 2
        Entonces el gestor tiene 0 tareas

    Escenario: Intentar eliminar la misma tarea dos veces
        Dado que el gestor tiene una tarea con nombre "Tarea única" y descripción "Descripción"
        Cuando elimino la tarea con ID 1
        Y intento eliminar la tarea con ID 1
        Entonces se produce un error con mensaje "No se encontró una tarea con ID 1"

    Escenario: Eliminar tarea completada
        Dado que el gestor tiene una tarea con ID 1 y estado "completada"
        Cuando elimino la tarea con ID 1
        Entonces la tarea se elimina exitosamente
        Y el gestor tiene 0 tareas