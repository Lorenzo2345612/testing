# language: es

Característica: Obtener tareas por estado
    Como usuario del gestor de tareas
    Quiero poder filtrar tareas por estado
    Para ver fácilmente qué tareas están pendientes, en progreso o completadas

    Escenario: Obtener tareas pendientes cuando hay tareas mixtas
        Dado que el gestor tiene 3 tareas
        Cuando marco la tarea con ID 1 como completada
        Y obtengo las tareas con estado "pendiente"
        Entonces obtengo 2 tareas
        Y la lista contiene la tarea con ID 2
        Y la lista contiene la tarea con ID 3
        Y la lista no contiene la tarea con ID 1
        Y todas las tareas tienen estado "pendiente"

    Escenario: Obtener tareas completadas cuando hay tareas mixtas
        Dado que el gestor tiene 3 tareas
        Cuando marco la tarea con ID 1 como completada
        Y obtengo las tareas con estado "completada"
        Entonces obtengo 1 tarea
        Y la lista contiene la tarea con ID 1
        Y la lista no contiene la tarea con ID 2
        Y la lista no contiene la tarea con ID 3
        Y todas las tareas tienen estado "completada"

    Escenario: Obtener tareas con cantidades específicas
        Dado que el gestor tiene 2 tareas pendientes y 1 tareas completadas
        Cuando obtengo las tareas con estado "pendiente"
        Entonces obtengo 2 tareas
        Y todas las tareas tienen estado "pendiente"

    Escenario: Obtener tareas cuando todas están completadas
        Dado que el gestor tiene 0 tareas pendientes y 3 tareas completadas
        Cuando obtengo las tareas con estado "pendiente"
        Entonces obtengo una lista vacía

    Escenario: Obtener tareas cuando todas están pendientes
        Dado que el gestor tiene 3 tareas pendientes y 0 tareas completadas
        Cuando obtengo las tareas con estado "completada"
        Entonces obtengo una lista vacía

    Escenario: Intentar obtener tareas con estado inválido
        Dado que el gestor de tareas está vacío
        Cuando intento obtener las tareas con estado "invalido"
        Entonces se produce un error con mensaje "Estado inválido"

    Escenario: Obtener tareas en progreso (actualmente ninguna)
        Dado que el gestor tiene tareas con diferentes estados
        Cuando obtengo las tareas con estado "en progreso"
        Entonces obtengo 0 tareas

    Escenario: Obtener tareas de un gestor vacío
        Dado que el gestor de tareas está vacío
        Cuando obtengo las tareas con estado "pendiente"
        Entonces obtengo una lista vacía

    Escenario: Verificar que el filtrado no modifica las tareas
        Dado que el gestor tiene una tarea con nombre "Tarea 1" y descripción "Descripción 1"
        Cuando marco la tarea con ID 1 como completada
        Y obtengo las tareas con estado "completada"
        Y obtengo las tareas con estado "pendiente"
        Y obtengo las tareas con estado "completada"
        Entonces obtengo 1 tarea
        Y la lista contiene la tarea con ID 1