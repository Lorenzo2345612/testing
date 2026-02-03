# language: es

Característica: Marcar tareas como completadas
    Como usuario del gestor de tareas
    Quiero poder marcar tareas como completadas
    Para llevar un control del progreso de mis tareas

    Escenario: Marcar una tarea pendiente como completada
        Dado que el gestor tiene una tarea con nombre "Comprar pan" y descripción "Comprar pan en la panadería"
        Cuando marco la tarea con ID 1 como completada
        Entonces la tarea se marca como completada exitosamente
        Y la operación devuelve True
        Y 1 tarea está completada
        Y la tarea con ID 1 está en la lista de tareas completadas
        Y la tarea con ID 1 tiene estado "completada"

    Escenario: Marcar una tarea ya completada como completada
        Dado que el gestor tiene una tarea con ID 1 y estado "completada"
        Cuando marco la tarea con ID 1 como completada
        Entonces la tarea se marca como completada exitosamente
        Y la operación devuelve True
        Y 1 tarea está completada

    Escenario: Intentar marcar una tarea inexistente como completada
        Dado que el gestor de tareas está vacío
        Cuando intento marcar la tarea con ID 999 como completada
        Entonces se produce un error con mensaje "No se encontró una tarea con ID 999"

    Escenario: Marcar múltiples tareas como completadas
        Dado que el gestor tiene 3 tareas
        Cuando marco la tarea con ID 1 como completada
        Y marco la tarea con ID 3 como completada
        Entonces 2 tareas están completadas
        Y la tarea con ID 1 está en la lista de tareas completadas
        Y la tarea con ID 3 está en la lista de tareas completadas

    Escenario: Verificar que solo la tarea marcada cambia de estado
        Dado que el gestor tiene 2 tareas
        Cuando marco la tarea con ID 1 como completada
        Entonces la tarea con ID 1 tiene estado "completada"
        Y la tarea con ID 2 tiene estado "pendiente"